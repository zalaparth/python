"""
    use for loop to print the following reverse number pattent

    5 4 3 2 1
    4 3 2 1
    3 2 1
    2 1
    1
"""
for a in range(5,0,-1):

    for b in range(a,0,-1):
        print(b,end=" ")
    print()
    
