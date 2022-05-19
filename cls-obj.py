#pogram to demonstrate objects and use of _init_() function
class emp:
    def __init__(self,name,sal,id):
        self.name=name
        self.sal=sal
        self.id=id
        print(self.name,self.sal,self.id)
        print(self.name,self.sal,self.id)
p1=emp('name',34,3)

print(id(p1))
class emp1(emp):
    def _init_(self,id,sal):
        emp.__init__(self,sal,id)
        
p2=emp('mamtha',4,4555)
print(p1.name)
print(p2.id)
print(p2.sal)

