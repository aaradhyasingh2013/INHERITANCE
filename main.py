class bus(object):
    def __init__(self,name):
        self.name= name
    def display(self):
        print(self.name)
class bus(object):
    def __init__(self, name,petrol):
        super().__init__(name)
        self.petrol= petrol
a= ("bus", "petrol")
a.display()

            