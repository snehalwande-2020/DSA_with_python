class stack:
 size=5
 top=0-1
 stack=[0]*size

 def overflow(self):
    if(self.top==self.size-1):
        return True
    return False

 def UnderFlow(self):
    if(self.top==-1):
        return True
    return False


 def push(self,data):
    if(self.overflow()):
        print("overFlow!")
    else:
        self.top+=1
        self.stack[self.top]=data

 def pop(self):
    if(self.UnderFlow()):
        print("Underflow!")
    else:
        self.top-=1    


 def Display(self):
    for i in range(self.top,-1,-1):
        print(self.stack[i])


s=stack()
choice=1
while choice!=0:
    print("1.push()")
    print("2.pop()")
    print("3.Display()")
    choice=int(input("enter thr choice:"))

    if(choice==1):
        data=int(input("enter the data"))
        s.push(data)
    elif(choice==2):
        s.pop()
    elif(choice==3):
        s.Display()
       

