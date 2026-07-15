def demo(str1):
    str2=""
    for i in str1:
        if i not in str2:
            if str1.count(i)>1:
                str2+=i
                str2+=str(str1.count(i))
            else:
                str2+=i


    print(str2)
str1=input("enter")
demo(str1)