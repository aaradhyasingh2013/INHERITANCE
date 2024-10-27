class person(object):
    def __init__(self,name):
        self.name= name
    def display(self):
        print(self.name)
class child(person):
    def __init__(self, name,salary):
        super().__init__(name)
        self.salary= salary
a= child("Kenisha agrawal", 90000000)
a.display()

            