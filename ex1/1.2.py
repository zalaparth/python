"""
Print the folowing pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""
for a in range(1,6):

    for b in range(1,a+1):
        print(b , end=" ")
    print()    
