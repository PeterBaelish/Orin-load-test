import sys
import os
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

with open('./timer/timer.json') as fp:
    json_data = json.load(fp)

thread = json_data['thread'] #rt prio: 99~0
min_time = []
max_time = []
avg_time = []

for key in thread:
    min_time.append(thread[key]['min'])
    max_time.append(thread[key]['max'])
    avg_time.append(thread[key]['avg'])

y1 = []
y2 = []
for x in range(100): #0~99
    y1.append(99-x)
    y2.append(avg_time[x])

y1points = np.array(y1)
y2points = np.array(y2)

plt.bar(y1points, y2points, label='')
plt.xlim(99,0)
#plt.figure(figsize=(30,15))
#plt.yscale("log")

plt.xlabel("realtime thread priority")
plt.ylabel("latency")
plt.title("average latency of hard interrupt load")

plt.show()