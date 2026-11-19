# "Duck typing means Python cares about what an object can do, not what the object is."
import random
class GooglePay:
    def pay(self):
        print("Payement made through Google pay")

class Phonepay:
    def pay(self):
        print("Payement made through Phonepay")

class Bharatpay():
    def pay(self):
        print("Payement made through Bharatpay")

def makepayment(payment_method):
    payment_method.pay()

obj = GooglePay()
obj.pay()
obj2 = Phonepay()
obj2.pay()
obj3 = Bharatpay()
obj3.pay()
l = (obj, obj2, obj3)
c = random.choice(l)
c.pay()