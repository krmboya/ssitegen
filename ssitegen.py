#!/usr/bin/env python
import os
import argparse
import sys
import shutil

EXEC_ROOT = os.path.dirname(__file__)

SOURCE_SUBDIRS = ('static', 'templates', 'content/entries', 'content/pages')

parser = argparse.ArgumentParser(add_help=True, description="A simple static site generator")

parser.add_argument("-i", "--initialize", action="store", default=None, dest="dirname",
                    help="Initialize the directory structure inside DIRNAME")

def ensure_dir_exists(dirname, mode=0o755):
    """Creates a directory with the given name if doesn't already exist"""

    if not os.path.exists(dirname):
        os.makedirs(dirname, mode)


if __name__ == "__main__":
    args = parser.parse_args()
    if args.dirname:
        source_dir = args.dirname
        if os.path.exists(source_dir):
            # already exists, print error and exit
            err_msg = "Directory '{0}' already exists\n".format(source_dir)
            sys.stderr.write(err_msg)
        else:
            # create directory and subdirectories
            ensure_dir_exists(source_dir)
            for subdir in SOURCE_SUBDIRS:
                path = os.path.join(source_dir, subdir)
                ensure_dir_exists(path)

            # create settings from template
            settings_template = os.path.join(EXEC_ROOT, "data", "settings_template")            
            settings_path = os.path.join(source_dir, "settings")

            shutil.copyfile(settings_template, settings_path)
            
    else:
        print "generating output"
