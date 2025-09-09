class Atm:
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def displayProperties(self):
        print(self.pinNumber, self.cardNumber)

    def cashWithdrawal(self):
        print("You've successfully withdrawn money from your account.")

    def balanceEnquiry(self):
        print("Your balance is 1,100,749,324. That's a lot of money!") 


Account = Atm(4596232585365696, 2487)

Account.displayProperties()
Account.cashWithdrawal()
Account.balanceEnquiry()







