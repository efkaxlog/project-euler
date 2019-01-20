"""
HTML fetching and parsing script to automate the creation of
directories and filesfor problems from the Project Euler website.
https://projecteuler.net/

Usage: fetch 4
Results in creating a directory for the problem  4 with a readme
file containing a description.
"""

import sys
import os

from urllib.request import urlopen
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print("Usage: fetch.py <problem>")
    sys.exit()

problem = sys.argv[1]
problem_url = "https://projecteuler.net/problem=" + problem

url_archives = "https://projecteuler.net/archives"
html_problem = urlopen(problem_url).read()
soup = BeautifulSoup(html_problem, "html.parser")
title = soup.find("h2").get_text()
info = soup.find_all("p")

title = "Problem " + problem + " - " + title
description = ""
for i, p in enumerate(info):
    description += p.get_text()
    if i != len(info) - 1: # avoids whitespace at end of string
        description += "\n\n"

ready_string = title + "\n\n" + description

problem_dir = "problems\\" + title
if os.path.isdir(problem_dir):
    print("Problem already exists")
    sys.exit()
else:
    os.mkdir(problem_dir)
    readme = open(problem_dir + "\\readme.md", "w+")
    readme.write(ready_string)
    readme.close()
    
print(ready_string)
