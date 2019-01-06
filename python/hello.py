mylist = [1,1,5,25,25,125,625]
r = 5
count = 0

for i in range(len(mylist)):
    for j in range(i+1,len(mylist)):
        if mylist[i]*r == mylist[j]:
          print('not geometric')
        else:  
          continue        
        for k in range(j+1,len(mylist)):
                if mylist[i]*r**2 == mylist[k]:
                  print('begin')
                  print('index:', i, 'value:', mylist[i])
                  print('index:', j, 'value:', mylist[j])
                  print('index:', k, 'value:', mylist[k])
                  print('end')
                  count += 1
print('Total Indices: %d' %count)                  
                    