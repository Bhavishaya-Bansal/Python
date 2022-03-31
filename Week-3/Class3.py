# Create a class "Counter" with a single data "count". Use a constructor to initialize "count" as 0. Use a function "inc()" to increament "count" a function "show()" to display "count"

class Counter:
  def __init__(self):
    self._count=0 # we know that (__) makes data private and typews without underscore are public so we have to make a function with single underscore (_) which makes the data protected and remains between private and public
  def inc(self):
    self._count+=1
  def show(self):
    print(self._count)
class Countdn(Counter):
  def dec(self):
    self._count-=1
    
c1= Counter()
c1.inc()
c1.inc()
c1.show()

c2= Countdn()
c2.inc()
c2.inc()
c2.dec()
c2.show()

# INHERITANCE (syntax)

class super_class:
  <statements>
class sub_class(super_class):
  <statements>
  
# Types of inheritance:
# 1. single --> child from single parent 
# 2. multiple --> single child from multiple parents 
# 3. multi level --> like grandparent then parent then child then grandchild and so on 
# 4. heirarical --> inheritance in tree like structure 
# 5. hybrid --> 
  
# Derive a class "DistSign" from "Distance". "DistSign" has an additional member "sign" that contains "+" or "-" [ we are required to make suitable changes in "Distance"]

