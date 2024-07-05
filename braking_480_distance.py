import numpy as np
import matplotlib.pyplot as plt

from CSV_parser import parse_CSV, get_filtered_minimums

print("BRAKING SCENARIO. 480 vehicles. minimum inter-vehicle distance \n")
print("\n ...")

desired_nodes = []

min_distances = []

min_distances_static = []
min_distances_slotted = []
min_distances_dynB1 = []
min_distances_dynB2 = []
min_distances_platoonB = []
min_distances_platoonBE = []


schemes = ['Static', 'Slotted', 'DynB1', 'DynB2', 'PlatoonB', 'PlatoonBE']

for scheme in schemes:
    for i in range(0, 10):

        distances  = parse_CSV(f'braking_480/{scheme}_Braking_480_{i}.csv', "distance", desired_nodes, False)
        distance_minimums = get_filtered_minimums(distances) # between 0 and 20
        # remove empty/none
        cleaned_minimums = [x for x in distance_minimums if np.isfinite(x)]
        min_value = min(cleaned_minimums)
        min_distances.append(min_value) 



    if scheme == 'Static':
        min_distances_static = min_distances
    
    if scheme == 'Slotted':
        min_distances_slotted = min_distances

    if scheme == 'DynB1':
        min_distances_dynB1 = min_distances

    if scheme == 'DynB2':
        min_distances_dynB2 = min_distances

    if scheme == 'PlatoonB':
        min_distances_platoonB = min_distances

    if scheme == 'PlatoonBE':
        min_distances_platoonBE = min_distances

    min_distances = []  


# plotting

plt.figure(figsize=(10, 6))

box = plt.boxplot([min_distances_static, min_distances_slotted, min_distances_dynB1, min_distances_dynB2, min_distances_platoonB, min_distances_platoonBE], labels=['Static', 'Slotted', 'DynB1', 'DynB2', 'PlatoonB', 'PlatoonBE'], patch_artist=True)

colors = ['#FF9999', '#99CC99', '#66B2FF','#FFCC99', '#CCCCFF', '#FFF799']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# title and labels

plt.ylabel("Min. Distance to Front (m)", fontsize=25, labelpad=15)
plt.yticks(fontsize=30)
plt.xticks(fontsize=28, rotation=30)
plt.ylim(0,8)
plt.axhline(y=5, color='red', linestyle='--')
plt.tight_layout()
#plt.savefig('/home/hassan/output/braking_480_distance.eps')
#plt.grid(True)
plt.show()