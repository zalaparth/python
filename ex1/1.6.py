"""
    count the total number of digit in a number using a while loop

    for example:
        Number is 1234
        output is 4
"""
num = int(input("Enter any number :- "))

count = 0
while num>0:
    num = int(num/10)
    count += 1
print(count)
    
