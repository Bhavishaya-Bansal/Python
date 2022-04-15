#EXCEPTION HANDLING

try:
  try to sum this code 
except:
  run it if an exception occurs
else:
  run it if no exception occurs
finally:
  always sum it 

Exceptions are the errors which occur at rum time

Example-

try:
  c=a/b
except:
  print('division not possible')
else:
  print(c)
  
  
Example-
  
try:
  age= int(input("enter the age: "))
  if age<18:
    raise ValueError
  else:
    print("age is valid")
    
except ValueError:
  print("age is not valid")
  
finally:
  print("this is a final clause")
