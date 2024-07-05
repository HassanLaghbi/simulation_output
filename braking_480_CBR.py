import matplotlib.pyplot as plt
import statistics
from CSV_parser import parse_CSV



print("BRAKING SCENARIO. 480 vehicles. Channel busy ratio - busyTime (CBR) \n")
print("\n ...")

desired_nodes = []

busy_times_means = []

busy_times_means_static = []
busy_times_means_slotted = []
busy_times_means_dynB1 = []
busy_times_means_dynB2 = []
busy_times_means_platoonB = []
busy_times_means_platoonBE = []

schemes = ['Static', 'Slotted', 'DynB1', 'DynB2', 'PlatoonB', 'PlatoonBE']

for scheme in schemes:
    for i in range(0, 10):
        busy_times  = parse_CSV(f'braking_480/{scheme}_Braking_480_{i}.csv', "busyTime", desired_nodes, True)
        mean_value = statistics.mean(busy_times)
        busy_times_means.append(mean_value)

    

    if scheme == 'Static':
        busy_times_means_static = busy_times_means
    
    if scheme == 'Slotted':
        busy_times_means_slotted = busy_times_means

    if scheme == 'DynB1':
        busy_times_means_dynB1 = busy_times_means

    if scheme == 'DynB2':
        busy_times_means_dynB2 = busy_times_means

    if scheme == 'PlatoonB':
        busy_times_means_platoonB = busy_times_means
        
    if scheme == 'PlatoonBE':
        busy_times_means_platoonBE = busy_times_means
        

    busy_times_means = []


# plotting
plt.figure(figsize=(10, 6))
box = plt.boxplot([busy_times_means_static, busy_times_means_slotted, busy_times_means_dynB1, busy_times_means_dynB2, busy_times_means_platoonB, busy_times_means_platoonBE], labels=['Static', 'Slotted', 'DynB1', 'DynB2', 'PlatoonB', 'PlatoonBE'], patch_artist=True)

colors = ['#FF9999', '#99CC99', '#66B2FF','#FFCC99', '#CCCCFF', '#FFF799']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.ylabel("Channel Busy Ratio", fontsize=28)
plt.yticks(fontsize=30)
plt.xticks(fontsize=28, rotation=30)

plt.ylim(0,1)
plt.tight_layout()
#plt.savefig('/home/hassan/output/braking_480_CBR.eps')
plt.grid(True)
plt.show()
