#def apples and oranges
def getApplesOranges():
    _apples = int(input("How many apples do you want to buy?"))
    _oranges = int(input("How many oranges do you want to buy?"))
    return _apples, _oranges


#def compute
def compute():
    ttlApple = aapple * 20                                          
    ttlOrange = oorange * 25                                        
    ttlPrice = ttlApple + ttlOrange
    return ttlPrice                              

#def display
def display(totalPrice):
    print(f"The total amount is {totalPrice} pesos.")

#variable
aapple, oorange = getApplesOranges ()
totalprice = compute ()

display (totalprice)
