# simple triangle
# rows=int(input("enter the rows"))
# for i in range(1,rows+1):
    # for j in range(1,i+1):
    #   print("*",end=" ")
    # print()

#inverted triangle
# rows=int(input("enter the rows"))
# for i in range(1,rows+1):
    #  for j in range(rows,i,-1):
    #    print("*",end=" ")
    #  print()


#triangle pattern
# rows=int(input("enter the rows"))
# for i in range(1,rows+1):
    # for k in range(rows,i-1,-1):
        # print(" ",end="")
    # for j in range(1,i+1):
            # print("*",end=" ")
    # print()
      
#diamond pattern
# rows=int(input("enter the rows"))
# for i in range(1,rows+1):
    # for j in range(rows,i,-1):
        # print(" ",end="")
    # for k in range(1,i+1):
                # print("* ",end="")
    # print()


# for i in range(1,rows+1):
    #  for j in range(1,i+1,1):
        #   print(" ",end="")
    #  for k in range(rows,i,-1):
        #    print("*",end=" ")

    #  print()           




#hallow square
# rows=int(input())
# for i in range(1,rows+1):
    # if i==1 or i==rows:
    #    for j in range(1,rows+1):
            # print("* ",end="")
    #    print()

    # else:
        #  for j in range(1,rows+1):
            #  if j==1 or j==rows:
                # print("* ",end="")
            #  else:
                # print("  ",end="") # in "" in between them we have to give two spaces
        #  print()



# hallow diamond
# rows=int(input("enter the rows"))
# for i in range(1,rows+1):
    # for j in range(rows,i,-1):
        # print(" ",end="")
    # for k in range(1,i+1):
        # if k==1 or k==i:       
        #    print("* ",end="")
        # else:
            # print("  ",end="")   

    # print()


# for i in range(1,rows+1):
    #  for j in range(1,i):
        #   print(" ",end="")
    #  for k in range(rows,i-1,-1):
        #  if k==rows or k==i:  
        #    print("* ",end=" ")
        #  else:
            #  print("  ",end="")  
# 
    #  print()           


# kite pattern

rows=int(input("enter the rows"))
for i in range(1,rows+1):
    for j in range(rows,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        if i!=rows:
           if k==1 or k==i:       
              print("* ",end="")
           else:
            print("  ",end="")   

        else:
            print("  ",end="")

    print()


for i in range(1,rows+1):
     for j in range(1,i):
          print(" ",end="")
     for k in range(rows,i-1,-1):
         if k==rows or k==i:  
           print("* ",end=" ")
         else:
             print("  ",end="")  

     print()           


for i in range(1,4+1):
    for k in range(rows,i,-1):
        print("*",end="")
    for j in range(1,i+1):
        print("*",end=" ")

    print()    
    



           


            
           


            