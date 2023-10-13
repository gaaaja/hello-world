# exercice conditional variable mutation 
a=24
output1 = 0
if a % 2 ==0 : 
  output1 += 1
  print (output1 )

b = 13
output2=" "
if b > 10 and b < 20: 
  output2 = "sweet"
elif b < 10 :
  output2= "Less"
elif b > 20 :
  output2 ="More"
print(output2)

c=123
credits=100
is_bonus= False
if credits >= 50 and not is_bonus: 
  c -=2
elif credits < 50 and not is_bonus:
  c -=1
else: c=c
print (c)  

d = 8
time = 120
output3= ""
if d % 4 ==0 and time < 200:
  output3="check"
elif time > 200:
  output3="Time out"
else: output3 = "Run forest Run!"
print(output3 )  

