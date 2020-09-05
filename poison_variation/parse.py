import pdb
import sys
import numpy as np
import csv

rates = ['0.05', '0.10', '0.15', '0.20', '0.25', '0.30', '0.35', '0.40', '0.45', '0.50']

for rate in rates:

	errfile = open(f'poison_{rate}_70_error.log', 'r')
	ratefile = open(f'poison_{rate}_70_rate.log', 'r')
			
	with open(f'poison_{rate}.csv', 'w') as f:	

		writer = csv.writer(f, delimiter=',')

		iteration = 0
		for iteration in range(0, 102):

			errline = errfile.readline()
			rateline = ratefile.readline()
		
			print(iteration)
			print(errline)
			print(rateline)

			timestamp = errline[7:20]

			# errline[55:62]
			# rateline[55:62]

			writer.writerow([iteration, errline[55:62], rateline[55:62], timestamp])

	errfile.close()
	ratefile.close()
