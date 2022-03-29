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

