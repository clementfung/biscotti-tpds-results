import pdb
import sys
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from datetime import datetime, timedelta

rates = ['0.05', '0.10', '0.15', '0.20', '0.25', '0.30', '0.35', '0.40', '0.45', '0.50']
all_lines = []
fig, ax = plt.subplots(figsize=(10, 5))

to_plot = np.zeros((10, 102))

completion_times = np.zeros(10)
final_error = np.zeros(10)
final_rate = np.zeros(10)

for i in range(10):
	
	rate = rates[i]
	df = pd.read_csv(f'poison_{rate}.csv', header=None)
	startTime = datetime.strptime(df[3].values[0], "%H:%M:%S.%f")
	endTime = datetime.strptime(df[3].values[101], "%H:%M:%S.%f")

	if endTime < startTime:
		endTime += timedelta(days=1)

	timeToComplete = endTime - startTime
	
	completion_times[i] = timeToComplete.seconds
	final_error[i] = df[1].values[101]
	final_rate[i] = df[2].values[101]

width = 0.35
rects1 = ax.bar(np.arange(10) - width/2, completion_times / np.max(completion_times), width, label='Training Time')
rects2 = ax.bar(np.arange(10) + width/2, final_rate, width, label='Final Attack Rate')

# l1 = mlines.Line2D(np.arange(102), to_plot[0], color='black',
# 	linewidth=3, linestyle='-', label="0.05")

# l2 = mlines.Line2D(np.arange(102), to_plot[1], color='black',
# 	linewidth=3, linestyle='-', label="0.10")

# ax.add_line(l1)
# ax.add_line(l2)

plt.legend(loc='best', fontsize=18)
#plt.legend(loc='upper center', fontsize=18, ncol=2)

axes = plt.gca()
axes.set_ylim([0, 1.09])

plt.xlabel("Poisoning Proportion", fontsize=22)
plt.ylabel("Training Time/Attack Rate", fontsize=22)

plt.xticks(np.arange(10), rates, fontsize=18)
plt.setp(ax.get_yticklabels(), fontsize=18)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

fig.tight_layout(pad=0.1)
fig.savefig("eval_varying_poison_bar.pdf")
