import pdb
import sys
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from datetime import datetime, timedelta

def plot(header_string, numRuns,  time=True):

    fig, ax = plt.subplots(figsize=(10, 5))
    toplot = np.zeros((2, 102))

    ###########################################
    across_runs = np.zeros((numRuns, 102))
    completionTimes = np.zeros(numRuns)
    for i in range(0, numRuns):
        
        df = pd.read_csv(f"{header_string}_federated_{i}.csv", header=None)
        across_runs[i] = df[1].values
        startTime = datetime.strptime(df[2].values[0], "%H:%M:%S.%f")
        endTime = datetime.strptime(df[2].values[101], "%H:%M:%S.%f")
        if endTime < startTime:
            endTime += timedelta(days=1)
        timeToComplete = endTime - startTime
        completionTimes[i] = timeToComplete.seconds

    avgFedSysCompletionTime = np.mean(completionTimes, axis=0)

    toplot[0] = np.mean(across_runs, axis=0)
    print("Fedsys: ")
    print(toplot[0])
    print(completionTimes)
    print(f"Completion Time: {avgFedSysCompletionTime}")
    
    ###########################################
    across_runs = np.zeros((numRuns, 102))
    completionTimes = np.zeros(numRuns)
    for i in range(0, numRuns):
        df = pd.read_csv(f"{header_string}_biscotti_{i}.csv", header=None)
        across_runs[i] = df[1].values
        startTime = datetime.strptime(df[2].values[0], "%H:%M:%S.%f")
        endTime = datetime.strptime(df[2].values[101], "%H:%M:%S.%f")
        if endTime < startTime:
            endTime += timedelta(days=1)
        timeToComplete = endTime - startTime
        completionTimes[i] = timeToComplete.seconds

    avgDistSysCompletionTime = np.mean(completionTimes, axis=0)

    toplot[1] = np.mean(across_runs, axis=0)
    print("DistSys: ")
    print(toplot[1])
    print(f"Completion Time: {avgDistSysCompletionTime}")
    ##########################################

    pdb.set_trace()

    total_nodes = 100

    if time:

        l1 = mlines.Line2D(avgFedSysCompletionTime * np.arange(102) / 100, toplot[0], color='black',
                           linewidth=3, linestyle='-', label="Federated Learning " + str(total_nodes) + " nodes")

        l2 = mlines.Line2D(avgDistSysCompletionTime * np.arange(102) / 100, toplot[1], color='red',
                           linewidth=3, linestyle='--', label="Biscotti " + str(total_nodes) + " nodes")

    else:

        l1 = mlines.Line2D(np.arange(102), toplot[0], color='black',
                           linewidth=3, linestyle='-', label="Federated Learning " + str(total_nodes) + " nodes")

        l2 = mlines.Line2D(np.arange(102), toplot[1], color='red',
                           linewidth=3, linestyle='--', label="Biscotti " + str(total_nodes) + " nodes")

    ax.add_line(l1)
    ax.add_line(l2)

    plt.legend(handles=[l1, l2], loc='right', fontsize=18)

    axes = plt.gca()

    axes.set_ylim([0, 1])

    if time:
        plt.xlabel("Time (s)", fontsize=22)
        axes.set_xlim([0, 1000* (int(avgDistSysCompletionTime/1000)+1)])
    else:
        plt.xlabel("Training Iterations", fontsize=22)
        axes.set_xlim([0, 100])

    plt.ylabel("Test Error", fontsize=22)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    plt.setp(ax.get_xticklabels(), fontsize=18)
    plt.setp(ax.get_yticklabels(), fontsize=18)

    fig.tight_layout(pad=0.1)

    if time:
        fig.savefig(f"eval_{header_string}convrate_time.pdf")
    else:
        fig.savefig(f"eval_{header_string}convrate.pdf")

if __name__ == '__main__':

	plot("600K", 3, True)
	#plot("600K", 3, False)

	plot("6mil", 1, True)
	#plot("6mil", 1, False)

# churns = ['1', '2', '4', '8', '16', '32', '35']
# all_lines = []
# fig, ax = plt.subplots(figsize=(15, 5))

# to_plot = np.zeros((8, 102))
# row = 0

# completion_times = np.zeros(7)
# final_error = np.zeros(7)

# for i in range(7):

# 	rate = churns[i]
# 	df = pd.read_csv(f'churn_{rate}.csv', header=None)
# 	startTime = datetime.strptime(df[2].values[0], "%H:%M:%S.%f")
# 	endTime = datetime.strptime(df[2].values[100], "%H:%M:%S.%f")

# 	if endTime < startTime:
# 		endTime += timedelta(days=1)

# 	timeToComplete = endTime - startTime
# 	completion_times[i] = timeToComplete.seconds
# 	final_error[i] = df[1].values[100]

# #final_error[7] = 0.00124
# #completion_times[7] = 9999

# # for rate in churns:

# # 	df = pd.read_csv(f'churn_{rate}.csv', header=None)
# # 	potential_row = df[1].values

# # 	while len(potential_row) < 102:
# # 		potential_row = np.append(potential_row, 0)

# # 	to_plot[row] = potential_row
# # 	row += 1

# width = 0.35
# #rects1 = ax.bar(np.arange(7), completion_times, width, label='Completion Time')
# rects1 = ax.bar(np.arange(7) - width/2, completion_times / np.max(completion_times), width, label='Completion Time')
# rects2 = ax.bar(np.arange(7) + width/2, final_error, width, label='Final Test Error')

# # plt.bar(np.arange(8), completion_times)
# # plt.bar(np.arange(8), final_error)
# # l1 = mlines.Line2D(np.arange(102), to_plot[0], color='black',
# # 	linewidth=3, linestyle='-', label="0.05")

# # l2 = mlines.Line2D(np.arange(102), to_plot[1], color='black',
# # 	linewidth=3, linestyle='-', label="0.10")

# # ax.add_line(l1)
# # ax.add_line(l2)

# plt.legend(loc='best', fontsize=18, ncol=2)
# #plt.legend(loc='upper center', fontsize=18, ncol=2)

# axes = plt.gca()
# #axes.set_ylim([0, 9999])

# plt.xlabel("Churn Rate (nodes/minute)", fontsize=22)
# plt.ylabel("Total Execution Time (s)", fontsize=22)

# plt.xticks(np.arange(7), churns, fontsize=18)
# plt.setp(ax.get_yticklabels(), fontsize=18)

# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)

# fig.tight_layout(pad=0.1)
# fig.savefig("eval_churn_time.pdf")
