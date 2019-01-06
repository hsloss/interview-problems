mylist = [1,1,5,25,25,125,625]
r = 5

for i in range(len(mylist)):
    for j in range(i, len(mylist)):
        if mylist[i]*r == j:
                continue
        for k in range(j, len(mylist)):
                if mylist[j]*r == k:
                  print('begin')
                  print('index:', i, 'value:', mylist[i])
                  print('index:', j, 'value:', mylist[j])
                  print('index:', k, 'value:', mylist[k])
                  print('end')
                    