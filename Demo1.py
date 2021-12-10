
x= int(input("Enter the number : "))
print ("The Number is:", x)
# Python program to find the factorial of a number provided by the user.
# check if the number is negative, positive or zero
if x < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif x == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,x + 1):
       factorial = factorial*i
   print("The factorial of",x,"is",factorial)
  
  if (x %2 )==0:
  print ( x,"The Number is even")
else:
  print (x,"The Number is odd")
  
