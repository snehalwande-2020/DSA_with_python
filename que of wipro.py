#3521
#2452
#1352
I1=int(input())
I2=int(input())
I3=int(input())
sum1=0
sum2=0
largest=0
small=9999
while(I1!=0):
    temp=I1%10
    
    I1//=10
    if largest<temp:
        largest=temp
    if small>temp:
        small=temp
sum1+=largest
sum2+=small

largest=0
small=9999
while(I2!=0):
    temp=I2%10
    
    I2//=10
    if largest<temp:
        largest=temp
    if small>temp:
        small=temp
sum1+=largest
sum2+=small


largest=0
small=9999
while(I3!=0):
    temp=I3%10
    
    I3//=10
    if largest<temp:
        largest=temp
    if small>temp:
        small=temp
sum1+=largest
sum2+=small

print(sum1-sum2)

#3521
#2452
#1352