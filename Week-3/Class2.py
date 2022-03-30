# oops in python
class sample:
     data1= 10
     data2= 'abc'
def show(self):
    print(self.data1, self.data2)
def putdata1(self, data1):
    self.data1 = data1
def putdata2(self.data2):
    self.data2 = data2
    
s1 = sample()
s1.show()
s1.putdata1(25)
s1.show()
print(s1.data1)
    
# in this as we can see that the data is public but if we put double underscore ( __ ) this makes the data to be private

class sample:
     __data1= 10
     __data2= 'abc'
def show(self):
    print(self.__data1, self.__data2)
def putdata1(self, data1):
    self.__data1 = data1
def putdata2(self.data2):
    self.__data2 = data2
    
s1 = sample()
s1.show()
s1.putdata1(25)
s1.show()
print(s1.__data1)

# Create a class with two private members feet and inches. Write member functions set()--> sets values in program     show()--> display with sign of feet and inches like: 7'9"    inp()-->  keyboard input

# class Distance:
#      __feet=0
#      __inches=0
#      def set(self,feet,inches):
#           self.__feet= feet
#           self.__inches= inches
#      def show(self):
#           print(self.__feet,"'",self.inches,'"')
#      def input1(self):
#           self.__feet= int(input("enter feet: ")
#           self.__inches= int (input("enter inches: ")
 
#  d1 = Distance()
#  d1.set(5,7.5)
#  d2 = distance()
#  d2 = input1()                      

# solving the above code using construtors
                              
 class Distance:
     __feet = 0
     __inches = 0
     def __init__(self, *args):  # as in c++ and java we define constructors similarly to declare construtor in python we use ( __init__ ) 
          if len(args)==1: # if only one value is givenn it means the value is given in metres therefore following functions would take place
               ft = int(ags[0] *3.2808) # to convert metre in feet 
               inch = (args[0] *3.2808 - ft) *12 # to convert metre in inches
               self.__feet = ft
               self.__inches = inch
          if len(args) == 2 # if 2 argumnets are given it means both feet and inches value is provided therefore we assign the respective values in feet and inches
          self.__feet = args[0]
          self.__inches = args[1]
          
     def set(self,feet,inches):
          self.__feet = feet
          self.__inches = inches
     def show(self):
          print(self.__feet,"'",self.__inches.'"')
     def input1(self):
          self.__feet=int(input("enter feet: "))
          self.__inches= int(input("enter inches: "))
     def add(self,x):
          self.__inches+=x.__inches 
          self.__feet+=x.__feet
          if self.__inches>=12 # if value of inches is given is given more than 12 then we will shift inches in feet and increase number of feet by one
               self.__inches-=12
               self.__feet+=1
     def add1(x,y):
          pass
     
d1 = Distance(5,7.5) # both values of feet and inches are given 
d2 = Distance() # input value ar emeant to be taken here
d2= input1()
d3= Distance(3.08) # single value is given it might be in metres so we have to convert it in feet and inches look at the upper part (if one there it is converted)
       
# Create a class "Counter" with a single member data 'count. Use Constructor to initialize count to zero. Write 2 fnction in the class 'inc for incrementing 'count' and show to display count.

