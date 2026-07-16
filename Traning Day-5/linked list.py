class node:
    def __init__(self):
        self.data=self.head
        self.next=None
         

class linkedList:
    data=0
    next=0
    head=0


    def InsertAtBeg(self,data):
        if(self.head==None):
            node=node(data)
        else:
            self.next=self.head
            self.head=node

    def display(self):
        if(self.head==None):
            print("EMPTY!!")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end="->")
                temp=temp.next
                print()

                               


choice=1
ll=linkedList()
while choice!=0:
    print("1.insert at begining")
    print("2.display")
    choice=int(input("enter your choice:"))
if(choice==1):
    data=int(input("enter data of node:"))
    ll.InsertAtBeg(data)
if(choice==2): 
    ll.display()   


         














    