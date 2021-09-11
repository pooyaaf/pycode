class person:
    #constructor
    def __init__(self,name) :
        self.name=name  #attribute
        self.balance = 0
    def add(self,amount:int): #method
        self.balance += amount


#object
person1 = person("ali") #instantiate
person2 = person("mohammad")
print(person1.name,person2.name)