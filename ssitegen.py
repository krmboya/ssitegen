import os
import argparse

parser = argparse.ArgumentParser(add_help=True, description="A simple static site generator")

parser.add_argument("-i", "--initialize", action="store", default=None, dest="dirname",
                    help="Initialize the directory structure inside DIRNAME")

args = parser.parse_args()

def ensure_dir_exists(dirname, mode=0o755):
    """Creates a directory with the given name if doesn't already exist"""

    if not os.path.exists(dirname):
        os.mkdir(dirname, mode)
