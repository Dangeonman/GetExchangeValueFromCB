import datetime
class Human:

    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    
    def getYB(my) -> int:
        today = datetime.date.today()
        yearB = today.year - my.age
        return yearB
    
    def setCredit(self, number, date,cvc):
         self.credit = CreditCard(number,date,cvc)

    def addChildLess3Y(self, child):
         if child.age < 3:
              self.addChild(child)
         
    def addChild(self, child):
        self.child = child
    
    def getPravuk(self):
         return self.child.child
#--------------------        
class CreditCard:
    def __init__(self,number,date,cvc) -> None:
            self.number = number
            self.date = date
            self.cvc = cvc
    def valid(self) -> bool:
         if self.date == "2222":
              return True
         return False

#--------------------    
papa = Human("Kirill",37)
sin = Human("Sergey",18)
pravnul = Human("mini kirill", 2)
sin.addChildLess3Y(pravnul)

papa.addChild(sin)


print(papa.getYB())
print(papa.child.getYB())
print(papa.getPravuk().name)
