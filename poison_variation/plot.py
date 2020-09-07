import pdb
import sys
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

rates = ['0.05', '0.10', '0.15', '0.20', '0.25', '0.30', '0.35', '0.40', '0.45', '0.50']
all_lines = []
fig, ax = plt.subplots(figsize=(5, 2))

to_plot = np.zeros((10, 102))
row = 0

for rate in rates:
	
	df = pd.read_csv(f'poison_{rate}.csv', header=None)
	to_plot[row] = df[2].values
	row += 1

for i in range(1, 10, 2):
	plt.plot(np.arange(102), to_plot[i], linewidth=3, linestyle='-', label=f'{rates[i]}% poison')

# l1 = mlines.Line2D(np.arange(102), to_plot[0], color='black',
# 	linewidth=3, linestyle='-', label="0.05")

# l2 = mlines.Line2D(np.arange(102), to_plot[1], color='black',
# 	linewidth=3, linestyle='-', label="0.10")

# ax.add_line(l1)
# ax.add_line(l2)

#plt.legend(loc='best', fontsize=18)
plt.legend(loc='upper center', fontsize=18, ncol=2)

axes = plt.gca()
axes.set_ylim([0, 1.5])

plt.xlabel("Training Iterations", fontsize=22)
plt.ylabel("Attack Rate", fontsize=22)

plt.setp(ax.get_xticklabels(), fontsize=18)
plt.setp(ax.get_yticklabels(), fontsize=18)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

fig.tight_layout(pad=0.1)
fig.savefig("eval_varying_poison_rate.pdf")
