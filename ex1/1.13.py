# use the loop to find the factorial of a given number
num = int(input("Enter any number :- "))

fact = 1

for i in rang(num,0,-1):
    fact *= i

else:
    print("Factorial of",num,"is : ",fact)
    
