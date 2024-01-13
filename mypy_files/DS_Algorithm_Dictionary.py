import math

print(math.e)# mathematical constant e
print(math.pi)
print(math.tau) #the ratio of the circumference to the radius of a circle

print (math.inf) # positive and negative infinity
print (-math.inf)

#comapring the values of infinty with maximum floating point value
print (math.inf > 10e108)
print (-math.inf < -10e108)

# NaN values (Not a Number ) value is not a legal number
print(math.nan)

a = 2.3
print(f"ceil of 2.3 is :{math.ceil(a)}\nfloor of 2.3 is :{math.floor(a)}")

#factorial
print(f"factorial of a :",math.factorial(5))

# gcd() function is used to find the greatest common divisor of two numbers passed as the arguments.

a = 15
b = 5
print ("The gcd of 5 and 15 is : ", (math.gcd(b, a)))

# fabs() function returns the absolute value of the number.
a = -10
print(f"absolute value of {a} : {math.fabs(a)}")

# exp() method is used to calculate the power of e i.e. e^y or we can say exponential of y.
test_int = 13
test_negative_int = -13
test_float = 13.13
print(f"exponentioal is {math.exp(test_int)}")
print(f"exponentioal is {math.exp(test_negative_int)}")


