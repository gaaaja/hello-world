a = int(input("enter the number of lines : "))

for i in range  (1, a + 1 , 2  ) :
 space = (a -i ) //2
 print( " " * (space ) + '*' * i)
for y in range(a-2 , 0, -2): 
 space = (a -y ) //2
 print( " " * (space ) + '*' * y)
              
