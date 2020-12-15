#!/bin/python3

import math
import os
import random
import re
import sys




def fittingAnalysis(height_of_locker ,length_of_locker,width_of_locker,length_of_magic_stick):

        if height_of_locker length_of_magic_stick:

        digonal = pow(height_of_locker, 2) + pow(length_of_locker, 2)+ pow(width_of_locker,2)
        cuboid_digonal=math.sqrt(digonal)
        return cuboid_digonal


if __name__ == '__main__':
    height_of_locker,length_of_locker,width_of_locker,length_of_magic_stick= map(int,input().split())

    result = fittingAnalysis(height_of_locker ,length_of_locker,width_of_locker,length_of_magic_stick)
    print(result)



    
    
 

    
    
