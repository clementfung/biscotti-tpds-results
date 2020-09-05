import pdb
import sys
import numpy as np
import csv

churns = ['1', '2', '4', '8', '16', '32', '35', '40']

for rate in churns:

	churnfile = open(f'churn_{rate}.log', 'r')
			
	with open(f'churn_{rate}.csv', 'w') as f:	

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
