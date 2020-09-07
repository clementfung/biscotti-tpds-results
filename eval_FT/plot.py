import pdb
import sys
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from datetime import datetime, timedelta

churns = ['1', '2', '4', '8', '16', '32', '35']
all_lines = []
fig, ax = plt.subplots(figsize=(15, 5))

to_plot = np.zeros((8, 102))
row = 0

completion_times = np.zeros(7)
final_error = np.zeros(7)

for i in range(7):

	rate = churns[i]
	df = pd.read_csv(f'churn_{rate}.csv', header=None)
	startTime = datetime.strptime(df[2].values[0], "%H:%M:%S.%f")
	endTime = datetime.strptime(df[2].values[100], "%H:%M:%S.%f")

	if endTime < startTime:
		endTime += timedelta(days=1)

	timeToComplete = endTime - startTime
	completion_times[i] = timeToComplete.seconds
	final_error[i] = df[1].values[100]

#final_error[7] = 0.00124
#completion_times[7] = 9999

# for rate in churns:

# 	df = pd.read_csv(f'churn_{rate}.csv', header=None)
# 	potential_row = df[1].values

# 	while len(potential_row) < 102:
# 		potential_row = np.append(potential_row, 0)

# 	to_plot[row] = potential_row
# 	row += 1

width = 0.4
#rects1 = ax.bar(np.arange(7), completion_times, width, label='Completion Time')
rects1 = ax.bar(np.arange(7) - width/2, completion_times / np.max(completion_times), width, label='Completion Time')
rects2 = ax.bar(np.arange(7) + width/2, final_error, width, label='Final Test Error')

# plt.bar(np.arange(8), completion_times)
# plt.bar(np.arange(8), final_error)
# l1 = mlines.Line2D(np.arange(102), to_plot[0], color='black',
# 	linewidth=3, linestyle='-', label="0.05")

# l2 = mlines.Line2D(np.arange(102), to_plot[1], color='black',
# 	linewidth=3, linestyle='-', label="0.10")

# ax.add_line(l1)
# ax.add_line(l2)

plt.legend(loc='best', fontsize=20, ncol=2)
#plt.legend(loc='upper center', fontsize=18, ncol=2)

#axes = plt.gca()
#axes.set_ylim([0, 9999])

plt.xlabel("Churn Rate (nodes/minute)", fontsize=24)
plt.ylabel("Total Execution Time (s)", fontsize=24)

plt.xticks(np.arange(7), churns, fontsize=20)
plt.setp(ax.get_yticklabels(), fontsize=20)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

fig.tight_layout(pad=0.1)
fig.savefig("eval_churn_time.pdf")
