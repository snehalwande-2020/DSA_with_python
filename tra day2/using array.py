
#(imp)how to find second largest & smallest number based on even/odd index
list=[]
size=int(input("enter the size of array"))
for i in range(0,size):
    list.append(int(input()))

even=[]
odd=[]
for i in range(0,size):
    if i%2==0:                    #if i
        even.append(list[i])
    else:
        odd.append(list[i]) 

even.sort()
odd.sort()
print(f'second largest number={even[len(even)-2]}')
print(f'second smallest number={odd[1]}')          

