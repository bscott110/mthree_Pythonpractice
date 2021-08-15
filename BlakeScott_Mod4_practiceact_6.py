#Blake Scott 08/10/2021
import json as j
from pprint import pprint

import numpy

data = []
for line in open('C:/Users/blake/Documents/restaurant.json',"r"):
    data.append(j.loads(line))

bor=[]

for br in data:
    bor.append([br['borough'],br['cuisine']])
    score = []
    for s in br['grades']:
        score.append(s['score'])

    pprint(score)
    try:
        pprint(max(score))
    except (ValueError, TypeError):
        print('empty list or invalid input')