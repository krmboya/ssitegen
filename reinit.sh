#!/usr/bin/env bash
# A wrapper around `ssitegen.py` that reinitializes the site directory
# Preserving the `settings` file and `content` directory
# Invoke the script with the site directory as an argument
# The old stuff is stored in `/tmp`

if [ $# -ne 1 ]; then
    echo "usage: $0 <sitedirectory>"
    exit 1
fi

mv "$1"  /tmp/sitebackup$$
ssitegen.py -i "$1"
mv "$1"/content /tmp/content$$
mv /tmp/sitebackup$$/settings "$1"/settings
mv /tmp/sitebackup$$/content "$1"
