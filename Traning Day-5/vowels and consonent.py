str1=" snehal wande"
var1=0
var2=0
vowels="aeiouAEIOU"
for i in str1:
     if i not in vowels:
          var1+=1
     else:var2+=1

print(f'vowels={var2}')
print(f'consonenta={var1}')          
