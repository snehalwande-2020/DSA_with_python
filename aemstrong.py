
num=int(input())
temp=num
count=len(str(num))
sum=0
while num!=0:
    sum+= (num%10)**count
    num//=10



if temp==sum:
    print("it is an armstrong")  
else:
    print("it is not an armstrong")