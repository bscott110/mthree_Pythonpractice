#Blake Scott 08/10/2021
import json as j
from pprint import pprint

import numpy

data = []
for line in open('C:/Users/blake/Documents/restaurant.json',"r"):
    data.append(j.loads(line))

ri=[]

for rest_id in data:
    ri.append([rest_id['restaurant_id']])
    score=[]
    for s in rest_id['grades']:
        score.append(s['score'])

    ri.append(score)
    ri.append(numpy.average([x for x in score if x != None]))


pprint(ri)

