# Swapping numbers in python

a = 4
b = 5

temp = a
a = b
b = temp

print(a, b)

# another way of swapping

a = 4
b = 5

def swap(x, y):
  temp = x
  x = y
  y = temp

swap(a,b)
print(a, b)

# lambda function - incline function 

def charline(char, times):
  print(times*char)
charline('*', 20)  # prints * 20 times
charline('@', 30)  # prints @ 30 times
charline('$', 40)  # prints $ 40 times

#  we can write it in lambda function as:

cline = lambda char, times: print(times*char)
cline('*', 20)  # prints * 20 times
cline('@', 30)  # prints @ 30 times
cline('$', 40)  # prints $ 40 times

#  convert "rfactorial" function to a lambda funtion

factorial= lambda x: 1 if x<=1 else x*factorial(x-1)
factorial(5) # factorial of 5

def maker(n):
  def action(x):
    return x**n
  return action 

sqr = maker(2)
cub = maker(3)

sqr(3), cub(3) # called the function to find the sqr and cube of 3.

# A function for factorial and a function defining ncr i.e. n! / (n-r)! * r!

def factorial(x):
  if x<=1:
    return 1 
  else:
    return x*factorial(x-1)
  
def ncr(n, r):
  return(facorial(n)) / (factorial(n-r) * factorial(r))
