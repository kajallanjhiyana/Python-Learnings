
from abc import ABC, abstractmethod

#Abstract base class
class ATM(ABC):

    @abstractmethod
    def pay(self):
        print("Payment processing")

#Concrete class 1
#A concrete class implements all the 
class UPI(ATM):

    def pay(self):
        print("Payment made through UPI.")

#Concrete class 2
class Netbanking(ATM):

    def pay(self):
        print("Payment made through Netbanking.")

#Concrete class 3
class Phonepay(ATM):

    def pay(self):
        print("Payment made through Phonepay.")

obj1 = UPI()
obj1.pay()
obj2 = Netbanking()
obj2.pay()
obj3 = Phonepay()
obj3.pay()