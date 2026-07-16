#encapasulation
# class sipna:
    # a=10
    # def demo(self):
        # __b=20             #here b is private member we can't access it directly so we have to call function this is called as encapsulation
        # print(__b)

# obj=sipna()
# print(obj.a)
# obj.demo()

# polymorphism
# class sipna():
    # def add(self,a,b):
        # return a+b
# class sipna1():
    # def add(self,a,b,c):
        # return a+b+c
    
# obj=sipna()
# obj1=sipna1()
# print(obj.add(10,20))
# print(obj1.add(10,20,30))   

#second method
# class sipna():
    # def add(self):
        # print("sipna")
# class sipna1():
    # def add(self):
        # print(sipna1)

# class sipna2():
    # def add(self):
        # print(sipna2)  

# obj=sipna()
# obj1=sipna1()



class add:
    def add(self,x,y):
        return (x+y)

class str1:
    def add(self,x,y):
        return(x+y)
class list:
    def add(self,x,y):
        result=[]
        if len(x)!=len(y):
            return 0
        else:
            for i in range(len(x)):
              result.append(x[i]+y[i])
            return(result)

obj1=add()
obj2=str1()
obj3=list()

print(obj1.add(10,20))
print(obj2.add("snehal","wande"))
obj3.add([10,20,30],[40,50,60])
       