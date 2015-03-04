import argparse

parser = argparse.ArgumentParser(add_help=True, description="A simple static site generator")

parser.add_argument("-i", "--initialize", action="store", default=None, dest="dirname",
                    help="Initialize the directory structure inside DIRNAME")

args = parser.parse_args()


