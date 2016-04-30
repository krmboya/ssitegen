# NAME
ssitegen - generate a static site

# SYNOPSIS
ssitegen [-h] [-i DIRNAME ]

# DESCRIPTION
ssitegen generates a collection of html files that can be used to serve a website from
input files written in markdown. It uses an opinionated directory structure
for both the input files and the output html files, plus other static assets like
images and stylesheets. A website can then be served from the output directory depending
on the preferred method of hosting, for example by pointing a webserver to its location or 
uploading it to some other web hosting service.

## Basic Usage

Running the command `ssitegen -i mysite` will create a directory named `mysite`, if it
doesn't already exist and add the necessary files and directories within it.

Inside `mysite`, are the following:

- settings - site specific configuration file
- static - directory containing static assets like images, JavaScript, css etc
- templates - directory containing templates for common parts of the html pages
- content - directory containing the actual blog entry/page as markdown files

Change the following in `settings` according to your preferences:

- blog_title
- blog_description
- blog_image (this should be a link to a publicly accessible image stored 
  somewhere on the web e.g. gravatar)

Put something descriptive in your about page: `content/pages/about.md`

The directory `content/entries` contains your blog entries. Any files that end
with `.md` here will be converted to html entries. Use `sample_entry.md.draft` 
as a template for new entries. `first_entry.md` has been provided as an example.

Running the command `ssitegen` while directly inside the `mysite` created above 
will create a new directory named `output`. This directory contains all the 
necessary files needed to serve the website, i.e.

- index.html - the site's landing page
- static - contains the site's static assets
- a html file for each blog entry/page

## Development

Trello board: https://trello.com/b/qBxOPk1y/ssitegen
