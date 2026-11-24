
# DEXON Trading Engine
# Simulation Mode Only

class TradingEngine:

    def __init__(self, initial_balance=100.00):
        self.balance = float(initial_balance)
        self.positions = {}
        self.auto_trading = False
        self.mode = "SIMULATION"

    def get_balance(self):
        return round(self.balance, 6)

    def get_position(self, token):
        return self.positions.get(token, None)

    def buy(self, token, amount_usdc, price):

        if amount_usdc <= 0 or price <= 0:
            return {
                "status": "error",
                "message": "Invalid amount or price"
            }

        if amount_usdc > self.balance:
            return {
                "status": "error",
                "message": "Insufficient USDC"
            }

        quantity = amount_usdc / price

        self.balance -= amount_usdc

        if token not in self.positions:
            self.positions[token] = {
                "quantity": 0.0,
                "invested": 0.0
            }

        self.positions[token]["quantity"] += quantity
        self.positions[token]["invested"] += amount_usdc

        return {
            "status": "success",
            "action": "BUY",
            "token": token,
            "quantity": quantity,
            "spent": amount_usdc
        }

    def sell(self, token, quantity, price):

        if quantity <= 0 or price <= 0:
            return {
                "status": "error",
                "message": "Invalid quantity or price"
            }

        if token not in self.positions:
            return {
                "status": "error",
                "message": "Token not found"
            }

        position = self.positions[token]

        if quantity > position["quantity"]:
            return {
                "status": "error",
                "message": "Insufficient token balance"
            }

        average_cost = (
            position["invested"] / position["quantity"]
        )

        cost = quantity * average_cost
        received = quantity * price
        pnl = received - cost

        self.balance += received

        position["quantity"] -= quantity
        position["invested"] -= cost

        if position["quantity"] < 0.000000001:
            del self.positions[token]

        return {
            "status": "success",
            "action": "SELL",
            "token": token,
            "received": round(received, 6),
            "pnl": round(pnl, 6)
        }

    def toggle_auto(self):
        self.auto_trading = not self.auto_trading
        return self.auto_trading

    def get_mode(self):
        return self.mode
            
