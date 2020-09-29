"""

iter is an onestep incremental tool for list of items
"""
#example1 iter on list

a=["sunday","monday", "Tuesday","wedsday","friday","saturday","sunday"]
i = iter(a)
print(i)#iterator object
print(next(i))#the first startrs from index o
print(next(i))

#iter with classes
#iter gives __iter___ and __next__ magic methods for writing the code
#iter to generate fibonocci seris upto given length
class fibonocii(object):
    def __init__(self,number):
        super().__init__()
        self.number = number
        self.start,self.end=1,2
        self.count =0

    def __iter__(self):#defines the iter object

        self.sum =0
        return self.sum
    def __next__(self): # returns the next immediate yield
       if self.count <=self.number:
           self.sum = self.start+self.end
           self.start = self.end
           self.end = self.sum
           self.count= self.count+1

       else:
           raise StopIteration
       return self.sum


five=fibonocii(5)
print(next(five))
print(next(five))

print(next(five))
print(next(five))

print(next(five))
print(next(five))

print(next(five))
print(next(five))