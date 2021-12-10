x= input("Enter the number : ")
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
