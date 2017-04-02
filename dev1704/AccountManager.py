

class AccountManager():

    def __init__(self, max_stock, data_manager):
        self.data_manager = data_manager
        self.max_stock = int(max_stock)
        self.hold_stock = {} # 내가 보유하고 있는 자신 {code, stock_price}
        self.cash = 10000000
        self.rate = 0.99

    def get_buy_quantity(self, code, date):
        # (최대 금액 - 보유가격) / adj_close
        if code in self.hold_stock:
            stock_price = self.hold_stock[code]
        else:
            stock_price = 0

        adj_close = self.data_manager.get_adj_close(code, date)
        diff = self.max_stock - stock_price
        if diff < 0:
            return 0
        elif self.cash < diff:
            return int(self.cash / adj_close)
        else:
            return int(diff / adj_close)

    def buy(self, code, price, count):
        if code in self.hold_stock:
            stock_price = self.hold_stock[code]
        else:
            stock_price = 0

        buy_price = price * count
        stock_price += buy_price
        self.hold_stock[code] = stock_price
        self.cash -= buy_price

    def sell(self, code):
        if code in self.hold_stock:
            stock_price =  self.hold_stock[code]
        else:
            stock_price = 0

        self.cash += stock_price * self.rate
        self.hold_stock[code] = 0

        return stock_price * self.rate

    def get_stock_price(self, code):
        """보유주 금액을 반환한다"""
        return self.hold_stock[code]

    def get_cash(self):
        """보유 현금을 반환한다"""
        return self.cash
