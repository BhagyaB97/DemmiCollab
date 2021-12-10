x= int(input("Enter the number : "))
print ("The Number is:", x)
flag = False
if x > 1:
    # check for factors
    for i in range(2, x):
        if (x % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(x, "is not a prime number")
else:
    print(x, "is a prime number")
    
# Python program to find the factorial of a number provided by the user.
# check if the number is negative, positive or zero
factorial=1
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
  
