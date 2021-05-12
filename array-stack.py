arr = [1,2,3,4]
arr3 = []
arr2 = []
for i in range (len(arr)):
        #print(i)
        for j in range (i, len(arr)):
               #print(j)
                arr2.append(arr[j])
                arr3.append(arr2)

print(arr2)
print(arr3)