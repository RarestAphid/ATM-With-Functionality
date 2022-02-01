class Atm:
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def displayProperties(self):
        self.cardNumber
        self.pinNumber


def cashWithdrawal():
    print("You've successfully withdrawn money from your account.")

def balanceEnquiry():
    print("Your balance is 1,100,749,324. That's a lot of money!") 


ATM1 = Atm(4596232585365696, 2487)

ATM1.displayProperties()
cashWithdrawal()
balanceEnquiry()






