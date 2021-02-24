#!/usr/bin/env python3

from github import Github
import os
from pprint import pprint

token = os.getenv('GITHUB_TOKEN', '96832b2330adcb00ff3ff829ab167f21d15c24ca')
g = Github(token)
repo = g.get_repo("MartinHeinz/python-project-blueprint")
issues = repo.get_issues(state="open")
pprint(issues.get_page(0))