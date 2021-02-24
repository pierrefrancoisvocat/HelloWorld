#!/usr/bin/env python3

from github import Github
import os
from pprint import pprint

token = os.getenv('GITHUB_TOKEN', '...')
g = Github(token)
repo = g.get_repo("MartinHeinz/python-project-blueprint")
issues = repo.get_issues(state="open")
pprint(issues.get_page(0))
