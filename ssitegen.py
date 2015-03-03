import argparse

parser = argparse.ArgumentParser(add_help=True, description="A simple static site generator")

parser.add_argument("-i", "--init", action="store_true", default=False,
                    help="Initialize the directory structure")

args = parser.parse_args()

