
num=int(input())
temp=num
rev=0
while(num!=0):
    rev=rev*10+num%10
    num=num//10
if temp ==rev:
    print("the number is palendrome")
else:
    print("the number is not a palendrome")