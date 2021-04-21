#!/bin/python3

import math
import os
import random
import re
import sys

"""
Round the Grades to th nearest multiple of 5 
2 steps up from the existing number
--> 84  to 85
-->57 do not round as 60 is 3 steps higher 
--> 38 can be  rounded to 40
-->29 do not round as lower than 38
"""

def gradingStudents(grades):
    list1=[]
    for no in grades:
     if no >= 38:
       if no % 5==3:    # Eg: 73 is 2 steps down from 75 .Hence 73 % mod 5 = 3 increament by 2 ,giving 75 
         no+=2
         list1.append(no)
       elif no%5==4:  # Eg: 74 is 1 steps down from 75 .Hence 74 % mod 5 = 4 increament by 1 ,giving 75 
         no+=1
         list1.append(no)
       else:
         list1.append(no)    
     else:
         list1.append(no)
    return list1
        
         
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    
    result= gradingStudents(grades)
    
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
