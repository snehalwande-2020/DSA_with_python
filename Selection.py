def selection(arr,size):
    for j in range(0,size-1):
        min=j
        for i in range(j+1,size):
            if(arr[min]>arr[i]):
                min=i
               
   #swapping
            temp=arr[j]
            arr[j]=arr[min]
            arr[min]=temp


    return arr


size=int(input("enter the size:"))
arr=[]
for i in range(0,size):
    arr.append(int(input()))
print(selection(arr,size))                    
    