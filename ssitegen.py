#!/usr/bin/env python
from __future__ import print_function

import io
import os
import argparse
import sys
import shutil
import json
import datetime

# third party libs
import markdown
import jinja2

EXEC_ROOT = os.path.dirname(__file__)
DIR_TEMPLATE_PATH = os.path.join(EXEC_ROOT, "data/source_dir")

parser = argparse.ArgumentParser(add_help=True, 
                                 description="A simple static site generator")

parser.add_argument("-i", "--initialize", action="store", default=None, 
                    dest="dirname",
                    help="Initialize the directory structure inside DIRNAME")

parser.add_argument('--version', action='version', version='%(prog)s 0.1')


def render_template(template_name, context, environment):
    """Renders a jinja2 template"""

    template = environment.get_template(template_name)
    return template.render(context)


def process_file(src, dest, template_name, jinja_env, md_converter):
    """Generates html file named `dest' from `src'

    Returns metadata extracted from `src'"""

    with io.open(src, "rt") as f:
        md_content = f.read()
            
    html_content = md_converter.convert(md_content)
    metadata = md_converter.Meta
    metadata["page_content"] = html_content
    metadata["filename"] = os.path.basename(dest)
    
    # convert date string to date object
    try:
        date_components = metadata["pubdate"][0].replace(' ', '').split("-")
    except KeyError:
        # no pubdate
        pass
    else:
        date_components = [int(v) for v in date_components]
        metadata["pubdate"] = datetime.date(*date_components)

    html_content = render_template(template_name, metadata, jinja_env)
        
    with io.open(dest, "wt") as f:
        f.write(html_content)
            
    md_converter.reset()
    return metadata


def convert_files_to_html(source_dir, dest_dir, template_name, templates_dir):
    """Converts markdown files in source dir to html files in dest dir

    Returns list of metadata extracted from each file"""

    converter = markdown.Markdown(extensions=['markdown.extensions.meta'])
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(templates_dir))

    files = os.listdir(source_dir)
    markdown_files = [fname for fname in files 
                      if fname.rsplit(".", 1)[1] == "md"]

    metadata_list = []
    
    for fname in markdown_files:
        source_file = os.path.join(source_dir, fname)
        dest_file = os.path.join(dest_dir, fname.rsplit(".", 1)[0] + ".html")

        metadata = process_file(source_file, dest_file,
                                template_name, jinja_env, converter)
        metadata_list.append(metadata)
        
    return metadata_list


def main():
    """Starting point of the script"""

    args = parser.parse_args()

    if args.dirname:
        # Initialize a new working directory

        working_dir = args.dirname
        if os.path.exists(working_dir):
            # already exists, print error and exit
            err_msg = "Directory '{0}' already exists\n".format(working_dir)
            sys.stderr.write(err_msg)
            sys.exit(1)

        # Initialize directory contents
        dir_template_loc = os.path.join(EXEC_ROOT, DIR_TEMPLATE_PATH)
        shutil.copytree(dir_template_loc, working_dir)

        
    else:
        # Generate the site from source

        # Read in settings
        with io.open("settings", 'rt') as f:
            settings = json.loads(f.read())
            
        # create a new output directory
        output_dir = settings["output_dirname"]
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)
        os.mkdir(output_dir)

        # copy over static assets
        shutil.copytree('static', output_dir + "/static")
        
        # Generate entries
        entry_metadata = convert_files_to_html("content/entries", 
                                               output_dir, 
                                               template_name="entry.html", 
                                               templates_dir='templates')

        # Generate site pages
        convert_files_to_html("content/pages", output_dir,
                              template_name="page.html",
                              templates_dir='templates')

        # Generate landing page
        jinja_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader('templates'))

        # sort entries in descending order of date
        entry_metadata.sort(key=lambda entry: entry["pubdate"], reverse=True)
        
        context = {"entries": entry_metadata } 
        
        html = render_template("index.html", context, jinja_env)
        dest = os.path.join(output_dir, "index.html")
        with io.open(dest, "wt") as f:
            f.write(html)
    

if __name__ == "__main__":
    main()
