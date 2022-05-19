class emp1:
    def __init__(self,name,id):
        self.name=name
        self.id=id
o1=emp1('xyz',8484)
print(o1.name,o1.id)
class emp2(emp1):
    def __init__(self, sal, id):
        super().__init__(self, id)
        self.sal=sal
        self.id=id
o2=emp2(78878,4759)
print(o1.name,o2.id,o2.sal)
