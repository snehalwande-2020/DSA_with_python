class node:
    def __init__(self,data):
        self.data=data
        self.next=next

class Linkedlist:
        
     head=None    
     def InsertAtBeg(self,data):
         newnode=node(data)
         if(self.head==None):
            self.head=newnode
            newnode.next=None
         else:
            newnode.next=self.head
            self.head=newnode

     def display(self,data):
        if(self.head==None):
            print("EMPTY!!")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end="->")
                temp=temp.next
            print()


     def InsertAtEnd(self,data):
        newnode=node(data)
        if(self.head==None):
            self.head=newnode
            newnode.next=None
        else:
            temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=newnode      
        newnode.next=None
          

     def InsertAtPosition(self,pos,data):
        newNode=node(data)
        if(pos==1):
            self.InsertAtBeg(data)
        else:
            if(self.head==None):
                print("list is empty!")
            else:
                temp=self.head
                i=1
                while i<pos-1:
                    if temp!=None:
                        temp=temp.next
                        i+=1
                    else:
                        print("invalid pos!!")
                        break 
                newNode.next=temp.next
                temp.next=newNode                          
#for deleting
     def DeleteAtBeg(self):
      if(self.head==None):
        print("empty")
      else:
        self.head=self.head.next


     def DeleteAtEnd(self):
         if(self.head==None):
             print("empty")
         else:
             temp=self.head
             while(temp.next.next!=None):
                 temp=temp.next    
             temp.next=None         
         
     def DeleteAtPosition(self,pos):
           if(pos==1):
            self.DeleteAtBeg(data)
           else:
            if(self.head==None):
                print("list is empty!")
            else:
                temp=self.head
                i=1
                while i<pos-1:
                    if temp!=None:
                        temp=temp.next
                        i+=1
                    else:
                        print("invalid pos!!")
                        break 
            temp.next=temp.next.next    
                      
                 
         

                               


choice=1
ll=Linkedlist()
while choice!=0:
    print("1.insert at begining")
    print("2.display")
    print("3.insert at end")
    print("4.InsertAtPosition:")
    print("5.DeleteAtBeg:")
    print("6.DeleteAtEnd:")
    print("7.DeleteAtPosition:")

    choice=int(input("enter your choice:"))
    if(choice==1):
     data=int(input("enter data of node:"))
     ll.InsertAtBeg(data)
    elif(choice==2): 
     ll.display(data)
    elif(choice==3):
     data=int(input("enter data of node:"))
     ll.InsertAtEnd(data)
    elif(choice==4):
     data=int(input("enter data of node:"))
     pos=int(input("enter the position:"))
     ll.InsertAtPosition(pos,data)    
    elif(choice==5):
     ll.DeleteAtBeg()
    elif(choice==6):
     ll.DeleteAtEnd()
    elif(choice==7):
     pos=int(input("enter position:"))
     ll.DeleteAtPosition(pos)    

         














    