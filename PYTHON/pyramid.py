number_lines = int(input("enter the number of lines "))
for i in range  (1,  number_lines +1 ) :
 print(" " * (number_lines - i) + '*' * (2 * i- 1))