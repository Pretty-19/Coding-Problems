testcases=input()
ques=[]
list1=[]
list_ans=[]
for i in range(int(testcases)):
  number_list=list(map(int,input().split()))
  ques.append(number_list)
for itr in range(len(ques)):
  diff=ques[itr][0] - ques[itr][1] 
  if ques[itr][1] < ques[itr][0]:
      list1.append(ques[itr][0])
      if diff>=ques[itr][1] and diff+ques[itr][1]==ques[itr][0]: 
         list1.append([ques[itr][1],diff])
      finalans=0
      ans1=[]
      start=0
      while (finalans<ques[itr][0]):
          finalans+=ques[itr][1]
          start+=1
          if(finalans==ques[itr][0]):
            for i in range(start):
             ans1.append(ques[itr][1])
          elif(finalans>ques[itr][0]):
             break
      list1.append(ans1)
  ans_list=list(filter(lambda x: x, list1))
  new_k = []
  for elem in ans_list :
        if elem not in new_k :
            new_k.append(elem)
  k = new_k
  del list1[:]
  print(len(k)%1000000009)
 


