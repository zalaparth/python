# display all prime numbers within a range

start = int(input("Enter starting value:- "))
end = int(input("Enter Ending Value:- "))

for n in range(start,end+1):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n)
