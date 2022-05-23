
class Cart:
    def __init__(self, num:str = None, symbol:str = None):
        self.__num:int = num
        self.__symbol:str = symbol

    def get_num(self):
        """Returns the num of the cart."""
        return self.__num

    def get_symbol(self):
        """Returns the symbol of the cart."""
        return self.__symbol

    def __str__(self):
        return f"num: {self.__num}, symbol: {self.__symbol}"

    def __json__(self):
        return str(self.__dict__())

    def __dict__(self):
        return {'num':self.__num, 'symbol':self.__symbol}

    def __gt__(self, Cart):
        return self.__num > Cart.get_num()

    def __lt__(self, Cart):
        return self.__num < Cart.get_num()

    def __ge__(self, Cart):
        return self.__num >= Cart.get_num()

    def __le__(self, Cart):
        return self.__num <= Cart.get_num()

    def __eq__(self, Cart):
        return self.__num == Cart.get_num()

    def __ne__(self, Cart):
        return self.__num != Cart.get_num()

    def equal(self, cart):
        """Returns if this cart is equal to other."""
        return self.__num == cart.get_num() and self.__symbol == cart.get_symbol()

class Deck:
    __symbols = ["clubs", "diamonds", "hearts", "spades"]
    __unused = []

    #trebol, diamante, corazon, picas

    def __init__(self, carts:list = None, unused_carts:list = None):
        self.carts = carts
        if unused_carts != None: self.__unused = unused_carts
        if carts == None: self.__generate_carts()
        self.num = self.__count()
            

    def __generate_carts(self, restore:bool = True):
        """Generates the carts of the deck. (If restore = True, then will ignore the unused carts.)"""
        __new_carts = []
        if restore:
            for symbol in self.__symbols:
                for num in range(1, 14):
                    __new_carts.append(Cart(num, symbol))
            self.__carts = __new_carts
        else:
            pass
        self.__drop_unused()

    def __drop_unused(self):
        for cart in self.__unused:
            if cart in self.__carts:
                self.__carts.remove(cart)

    def get_carts(self):
        return self.__carts

    def __count(self):
        return len(self.__carts)

    def __add__(self, deck):
        new_deck = self.__carts + deck.get_carts()
        return Deck(carts = new_deck)
