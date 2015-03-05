# NAME
ssitegen - generate a static site

# SYNOPSIS
ssitegen [-h] [-i DIRNAME ]

# DESCRIPTION
ssitegen generates html files that can be used to serve a website from files written in 
markdown. It uses the directory structure created initialization to generate an output
directory containing the necessary html files and other static assets needed to render the
site on a web browser. The website can then be served from this directory, or it can be 
uploaded to some other web host, depending on the preferred hosting method.


## Usage

### Initialization

Running the command `ssitegen -i mysite` will create a directory named `mysite` if it doesn't
already exist and add the necessary files and directories within it.

Inside `mysite`, are the following files and directories:

- settings.py
- static
- templates
- content

### Generating a site

Running the command `ssitegen` while inside the directory created above will create a new
directory named `output`. This directory contains all the necessary files needed to 
render the website. It contains the following files and directories:

- index.html
- static
- entries
- pages
