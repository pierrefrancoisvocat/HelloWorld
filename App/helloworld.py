#!/usr/bin/env python3

import logging
import sys 
from github import Github
import os
from pprint import pprint

#logging 

logging.basicConfig(filename='/var/log/helloworld/helloworld.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.info('- Starting up Hello World reader')

#git
#git_token = input("Please enter git token: ")
token = os.getenv('GITHUB_TOKEN', '123git_token321')
g = Github(token)
repo = g.get_repo("pierrefrancoisvocat/HelloWorld")
file_path = "/conf/helloworld.conf"
file = repo.get_contents(file_path, ref="main")
environment = file.decoded_content.decode("utf-8") 

def push(path, message, content, branch, update=False):        
    contents = repo.get_contents(path, ref=branch) 
    repo.update_file(contents.path, message, content, contents.sha, branch=branch) 

print("Environment stored in Git is - ", environment)
logging.info('- Initiating environment variable from git with a value of ' + environment )

try: 

	for arg in sys.argv:

		if arg != "helloworld.py" :
			if arg != "/home/vagrant/helloworld/App/helloworld.py" : # ugly line of code should be using string in arg comparison nut this works so moving on
				logging.info('- ' + arg + ' Environment has been updated using a call with parameters')
				push(file_path, "Edit Envirionments", arg, "main", update=True)
				exit()

	while True:

		print("Type Exit to quit")
		
		# Get environment name 
		environment = input("Please enter environment name: ") 

		# Check if we're done
		if environment == "Exit" :
			logging.info('- Exiting helloworld listener')
			break

		# If not done write environment to git, the console and the log file 
		push(file_path, "Edit Envirionments", environment, "main", update=True)
		print(environment)
		logging.info('- ' + environment + ' has been read')

	print("Bye")

except Exception as e:
   logging.error('Error at %s', exc_info=e)





