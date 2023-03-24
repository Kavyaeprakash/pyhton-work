class A:
    def __init__(self,x):
        # print('parent class A')
        self.message=x
    
    def printmessage(self):
        print(self.message)
    def display2(self):
        print('hello display2')
    def display3(self):
        print('hello display3')

class B(A):

    def __init__(self,x):
        print('parent class B')
        # super().__init__(x)
        
    
    def display4(self):
        print('hello display4')
class C(B):
    def __init__(self):
        print('parent class C')
obj1=B('hello')
obj1.message
print(obj1.message)