#!/bin/python3

import math
import os
import random
import re
import sys

"""
Solution:
| 0  |   0   |  1   |  0   |  0  | 1  |  0  |
                                                 ^
-------------------------------pos--  (Limit the while loop to length of list -1 as last element does not have pos+1 or pos+2 )
                                          ^
------------------------- pos-------  (This element does not have a pos+2 index)
                   ^
-----------pos---------------------- (If pos=0  for this element pos+2 index = 1 we need to Jump this position  )

"""

n = int(input())

c = list(map(int, input().rstrip().split()))
result=0
pos=0

while pos < (n-1):
   if     c[pos+2] == 1 or pos+2 >=n     :  # if c[pos+2] added in front of pos >2 error
         pos=pos+1
         result=result+1
   else:
        pos=pos+2
        result=result+1
print(result)

    
            
            
            
        
            
        


