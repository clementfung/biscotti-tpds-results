import pdb
import sys
import numpy as np
import csv

churns = ['1', '2', '4', '8', '16', '32', '35', '40']

for i in range(1):

	churnfile = open(f'6mil_Bis_error.log', 'r')
			
	with open(f'6mil_biscotti.csv', 'w') as f:	

		writer = csv.writer(f, delimiter=',')
		iteration = 0

		for line in churnfile:

			timestamp = line[7:20]
			error = line[55:62]

			print(timestamp)
			print(error)

			writer.writerow([iteration, error, timestamp])
			iteration += 1

	churnfile.close()
