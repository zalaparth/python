""" calculate the sum of  all number from 1 to a given number

 Enter number 10
 Sum is : 55

 """
num = int(input("Enter any number :- "))
ans = 0
for i in range(1,num+1):
    ans += i
print("sum of 1 to ",num," : ",ans)
    
