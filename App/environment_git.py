#!/usr/bin/env python3

from github import Github
import os
from pprint import pprint

token = os.getenv('GITHUB_TOKEN', '729007dddd1a6a01fcf8314e93b5e20ac349793b')
g = Github(token)
repo = g.get_repo("pierrefrancoisvocat/HelloWorld")
file_path = "/conf/helloworld.conf"

file = repo.get_contents(file_path, ref="main")  # Get file from branch
data = file.decoded_content.decode("utf-8")  # Get raw string data

print(data)

data = "pytest==5.3.2"  # Modify/Create file

print(data)

def push(path, message, content, branch, update=False):        
    contents = repo.get_contents(path, ref=branch)  # Retrieve old file to get its SHA and path
    repo.update_file(contents.path, message, content, contents.sha, branch=branch)  # Add, commit and push branch

push(file_path, "Edit Envirionments", data, "main", update=True)