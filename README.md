# NAME
ssitegen - generate a static site

# SYNOPSIS
ssitegen [-h] [-i DIRNAME ]

# DESCRIPTION
ssitegen generates a collection of html files that can be used to serve a website from
input files written using the markdown syntax. It uses an opinionated directory structure
for both the input files and the output html files, plus other static assets like
images and stylesheets. A website can then be served from the output directory depending
on the preferred method of hosting, for example by pointing a webserver to its location or 
uploading it to some other web hosting service.

## Usage

### Initializing the source directory

Running the command `ssitegen -i mysite` will create a directory named `mysite`, if it
doesn't already exist and add the necessary files and directories within it.

Inside `mysite`, are the following:

- settings.py
- static
- templates
- content

### Generating a site

Running the command `ssitegen` while inside the directory created above will create a new
directory named `output`. This directory contains all the necessary files needed to 
serve the website, i.e.

- index.html
- static
- entries
- pages
