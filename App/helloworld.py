#!/usr/bin/env python3

import logging
import sys 

#logging 

logging.basicConfig(filename='../log/helloworld.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.info('- Starting up Hello World reader')

try: 

	for arg in sys.argv:

		if arg != "helloworld.py" :
			logging.info('- ' + arg + ' has been called')
			exit()

	while True:

		print("Type Exit to quit")
		# Get environment name 
		
		environment = input("Please enter environment name: ") 

		# Check if we're done

		if environment == "Exit" :
			logging.info('- Exiting helloworld listener')
			break

		# If not done print environment 

		print(environment)
		logging.info('- ' + environment + ' has been read')

	print("Bye")

except Exception as e:
   logging.error('Error at %s', exc_info=e)