# mylist = [1, 3, -9, 1, 1, 3, 9, 3, 81]
# r = 3
# count = 0
# # still need to flatten lists
# for i in range(len(mylist)):
#     for j in range(i+1,len(mylist)):
#         if mylist[i]*r == mylist[j]:
#           print('The common ratio is %d' %r)
#         else:  
#           continue        
#         for k in range(j+1,len(mylist)):
#                 if mylist[i]*r**2 == mylist[k]:
#                   print('begin')
#                   print('index:', i, 'value:', mylist[i])
#                   print('index:', j, 'value:', mylist[j])
#                   print('index:', k, 'value:', mylist[k])
#                   print('end')
#                   count += 1
# print('Total Indices: %d' %count)    
# 

from collections import Counter

testlist = ([1, 1, 1, 1] + [3, 3, 3, 3], 1, 8)

testlist

print(testlist)