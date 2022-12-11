'''
def area(l,b):
    c=l*b
    return c
def area(size):
    c=size*size
    return c
#print(area(4))
print(area(4,3))'''
class compute:
    def area(self,x=None,y=None):
        if x!=None and y!=None:
            return x*y
        elif x!=None:
            return x*x
        else:
            return 0
obj=compute()
print(obj.area())
print(obj.area(6))
print(obj.area(2,8))
