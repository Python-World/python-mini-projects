# Check Website Connectivity

This directory contains a simple tool to check connectivity to a number of web sites.

The input file `websites.txt` should contain web site URLs, one per line.

The output file `website_status.csv` contains a two-column report with
the URL of each checked site and its status.
The script simply checks whether the web server returns a 200 status code.

The output file will be overwritten each time you run the tool.


## Prerequisites

This project uses the third-party library
[requests](https://requests.readthedocs.io/)
as well as the `csv` module from the Python standard library.


## How to run the Script

To run this script, type

```
python check_connectivity.py
```
in the directory where you have checked out these files.
(If you have an IDE which lets you run Python files,
and prefer to use that instead,
make sure you configure it to set the working directory to
the one which contains the input file.)


## Development ideas

The CSV should perhaps contain a date stamp, too.

Perhaps add the `logging` library and optionally print progress information.
