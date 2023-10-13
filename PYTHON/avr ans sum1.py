number_1 = int(input("enter a number :"))
number_2 = int(input("enter another number :"))
number_3 = int(input("enter a third number :"))
number_4 = int(input("enter a fourth number :"))
number_5 = int(input("enter a fifth number :"))
sum = number_1 + number_2 + number_3 + number_4 + number_5
average = sum / 5
print (sum , average )

#exercice odd even
user_name = int(input("enter a number: "))
if user_name % 2 == 0:
  print("even")
else: 
  print("odd")

#exercie one two a lot 
number_10 =int(input("enter a number please: ")) 
if number_10 <=0 :
 print ("Not enough") 
elif  number_10 == 1 :
 print("one")
elif  number_10 == 2 : 
 print ("two")
else: 
   number_10 >= 2
   print("a lot")

#exercice print bigger 
number_6 = int(input("enter the first number: "))
number_7 = int(input("enter a second number:")) 
if number_6 > number_7 : 
  print( "the bigger number :", number_6)
else :
  print ("the biggest number:", number_7)    

# exercice party indicator:
girls_number = int(input("enter the number of girls: "))                              
boys_number = int(input("enter the number of boys: "))
party_number = girls_number + boys_number 
if girls_number == boys_number and party_number >= 20 :
 print ("the party is excellent") 
elif party_number >= 20 and boys_number < girls_number:
  print("Quite a cool party")
elif party_number < 20 :
  print ("Average party")
else: print ("sausage party")  

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

