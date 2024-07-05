import numpy as np
import matplotlib.pyplot as plt
import statistics
from CSV_parser import parse_CSV



print("BRAKING SCENARIO. 480 vehicles. packet collisions per second \n")
print("\n ...")

desired_nodes = []

collisions_means = []

collisions_means_static = []
collisions_means_slotted = []
collisions_means_dynB1 = []
collisions_means_dynB2 = []
collisions_means_platoonB = []
collisions_means_platoonBE = []

schemes = ['Static', 'Slotted', 'DynB1', 'DynB2', 'PlatoonB', 'PlatoonBE']

for scheme in schemes:
    for i in range(0, 10):

        collisions  = parse_CSV(f'braking_480/{scheme}_Braking_480_{i}.csv', "collisions", desired_nodes, True)
        mean_value = statistics.mean(collisions)
        collisions_means.append(mean_value)


    if scheme == 'Static':
        collisions_means_static = collisions_means
    
    if scheme == 'Slotted':
        collisions_means_slotted = collisions_means

    if scheme == 'DynB1':
        collisions_means_dynB1 = collisions_means

    if scheme == 'DynB2':
        collisions_means_dynB2 = collisions_means

    if scheme == 'PlatoonB':
        collisions_means_platoonB = collisions_means

    if scheme == 'PlatoonBE':
        collisions_means_platoonBE = collisions_means


    collisions_means = []


# plotting
plt.figure(figsize=(10, 6))
box = plt.boxplot([collisions_means_static, collisions_means_slotted, collisions_means_dynB1, collisions_means_dynB2, collisions_means_platoonB, collisions_means_platoonBE], labels=['Static', 'Slotted', 'DynB1', 'DynB2', 'PlatoonB', 'PlatoonBE'], patch_artist=True)

colors = ['#FF9999', '#99CC99', '#66B2FF','#FFCC99', '#CCCCFF', '#FFF799']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.ylabel("Avg. # of Collisions/s", fontsize=28)
plt.yticks(fontsize=30)
plt.xticks(fontsize=28, rotation=30) 
plt.ylim(0,1000)
plt.tight_layout()
#plt.savefig('/home/hassan/output/braking_480_collisions.eps')
#plt.grid(True)
plt.show()