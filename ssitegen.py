#!/usr/bin/env python
from __future__ import print_function

import os
import argparse
import sys
import shutil
import json

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


def convert_files_to_html(source_dir, dest_dir, templates_dir, template_name):
    """Converts markdown files in source dir to html files in dest dir

    Uses template filename to as a jinja2 template"""

    files = os.listdir(source_dir)
    markdown_files = [fname for fname in files 
                      if fname.rsplit(".", 1)[1] == "md"]
    
    converter = markdown.Markdown()
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(templates_dir))
    template = jinja_env.get_template(template_name)

    for fname in markdown_files:
        source_file = os.path.join(source_dir, fname)
        dest_file = os.path.join(dest_dir, fname.rsplit(".", 1)[0] + ".html")
        
        with open(source_file, "r") as f:
            md_content = f.read()
        
        html_content = converter.convert(md_content)
        
        with open(dest_file, "w") as f:
            f.write(template.render(entry=html_content, title="foo"))
            
        converter.reset()

if __name__ == "__main__":
    args = parser.parse_args()
    if args.dirname:
        # Initializing

        # Create directory
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
        # Generating site

        # read in settings
        with open("settings") as f:
            settings = json.loads(f.read())
            
        # generate fresh output directory
        output_dir = settings["output_dirname"]
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)
        os.mkdir(output_dir)

        # copy over static assets
        shutil.copytree('static', output_dir + "/static")
        
        # Generate entries
        convert_files_to_html("content/entries", output_dir, 'templates',
                              "entry.html")
