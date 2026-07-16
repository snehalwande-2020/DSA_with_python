#sorting
# def bubble(arr,size):
    # for i in range(size):
        # print(f'pass{i}:')
        # for i in range(0,size-1):
            # print(f'IT {i}:',end="")
            # print(arr)
            # if(arr[i+1]<arr[i]):
            #    temp=arr[i]
            #    arr[i]=arr[i+1]
            #    arr[i+1]=temp

    # return arr


# size=int(input("enter the size:"))
# arr=[]
# for i in range(0,size):
    # arr.append(int(input()))
# print(bubble(arr,size))                    
    
#optimization of bubble sort
#if there is no swapping between digits for a long time we can break it using below code
def bubble(arr,size):
    for i in range(size):
        flag=False                     #new step
        print(f'pass{i}:')
        for i in range(0,size-1):
            print(f'IT {i}:',end="")
            print(arr)
            if(arr[i+1]<arr[i]):
               flag=True               #new step
               temp=arr[i]
               arr[i]=arr[i+1]
               arr[i+1]=temp
        if flag==False:                #new step
           break                       #new step
    return arr


size=int(input("enter the size:"))
arr=[]
for i in range(0,size):
    arr.append(int(input()))
print(bubble(arr,size))                    
    
