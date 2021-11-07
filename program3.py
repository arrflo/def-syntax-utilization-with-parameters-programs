#for inputs
def getMoneyApple():
    _money = float(input("Amount of money you have:"))
    _applePrice = float (input("Price of apple per piece:"))
    return _money, _applePrice

#for computations
def getAppleMaxChange ():
    _applemax = money / price
    applerounded = int (_applemax)
    ttlPayment = applerounded * price
    _change = money - ttlPayment
    return applerounded, _change

#for results
def display (maxNumberApples,change ):
    print(f"You can buy {maxNumberApples} and your change is {change:.2f} pesos.")

#program
money, price = getMoneyApple ()
appmax, chAnge = getAppleMaxChange ()

display (appmax, chAnge)