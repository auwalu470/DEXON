
# DEXON Trading Engine
# Simulation Mode Only

class TradingEngine:

    def __init__(self, balance=100.00):
        self.balance = balance
        self.positions = {}
        self.auto_trading = False

    def buy(self, token, amount):
        if amount <= 0:
            return "Invalid amount"

        if amount > self.balance:
            return "Insufficient USDC balance"

        self.balance -= amount
        self.positions[token] = {
            "entry": amount,
            "amount": amount,
        }

        return f"Simulation BUY: {token} for ${amount:.2f}"

    def sell(self, token):
        if token not in self.positions:
            return "Token not found"

        position = self.positions.pop(token)
        self.balance += position["amount"]

        return f"Simulation SELL: {token}"

    def get_balance(self):
        return round(self.balance, 2)

    def toggle_auto(self):
        self.auto_trading = not self.auto_trading
        return self.auto_trading


    def get_position(self, token):
        return self.positions.get(token, None)
        
