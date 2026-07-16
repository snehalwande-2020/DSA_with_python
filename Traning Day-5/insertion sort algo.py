#sorting of array using insertion

def insertion(arr,size):
     for i in range(1,size):
          temp=arr[i]
          j=i-1
          while j>=0 and temp<=arr[j]:
               arr[j+1]=arr[j]
               j-=1
    # if condition is false
          arr[j+1]=temp
     return arr       


size=int(input())
arr=[]
for i in range(0,size):
    arr.append(int(input()))
print(inse/rtion(arr,size))    


