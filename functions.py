A=int(input())
def diff(start,end,num):
    divsum=0
    nondivsum=0
    for i in range(start,end+1):
        if i%num==0:
            divsum+=i
        else:
            nondivsum+=i

        diff=abs(divsum-nondivsum)
        return diff
    

start=int(input("star:"))
end=int(input("end:"))
num=int(input("num:"))
print(diff(start,end,num))

