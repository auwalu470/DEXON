
class RiskManager:

    def __init__(self, take_profit=20, stop_loss=10):
        self.take_profit = take_profit
        self.stop_loss = stop_loss

    def check_trade(self, entry_price, current_price):

        if entry_price <= 0 or current_price <= 0:
            return "INVALID_PRICE"

        change = (
            (current_price - entry_price)
            / entry_price
        ) * 100

        if change >= self.take_profit:
            return "TAKE_PROFIT"

        if change <= -self.stop_loss:
            return "STOP_LOSS"

        return "HOLD"
      
