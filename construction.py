
import math
import os
import random
import re
import sys



def cementDistribution(increaseRate, sites):
    if len(sites) == 1 and len(increaseRate) == 1:
        return [int((((increaseRate[0] ** sites[0])-increaseRate[0])/(increaseRate[0]-1))+1), (increaseRate[0] ** sites[0])]

#logic

if __name__ == '__main__':

    increaseRate_count = int(input().strip())

    increaseRate = []

    for _ in range(increaseRate_count):
        increaseRate_item = int(input().strip())
        increaseRate.append(increaseRate_item)

    sites_count = int(input().strip())

    sites = []

    for _ in range(sites_count):
        sites_item = int(input().strip())
        sites.append(sites_item)

    result = cementDistribution(increaseRate, sites)

str_join = ",".join(map(str, result))
print(str_join)
   
