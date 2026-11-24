
from trading import TradingEngine
from risk_manager import RiskManager


class AutoTrader:

    def __init__(self, bot, trade_amount=10.00):
        self.bot = bot
        self.risk = RiskManager(
            take_profit=20,
            stop_loss=10
        )
        self.trade_amount = trade_amount
        self.entry_prices = {}

    def process_trade(self, token, current_price, signal="HOLD"):

        if current_price <= 0:
            return {"status": "error", "message": "Invalid price"}

        position = self.bot.get_position(token)

        # Check existing position
        if position:
            entry_price = self.entry_prices.get(
                token,
                position["invested"] / position["quantity"]
            )

            decision = self.risk.check_trade(
                entry_price,
                current_price
            )

            if decision in ["TAKE_PROFIT", "STOP_LOSS"]:
                result = self.bot.sell(
                    token,
                    position["quantity"],
                    current_price
                )

                if result["status"] == "success":
                    self.entry_prices.pop(token, None)

                return result

            return {
                "status": "success",
                "action": "HOLD",
                "decision": decision
            }

        # Buy when signal is BUY
        if signal.upper() == "BUY":
            result = self.bot.buy(
                token,
                self.trade_amount,
                current_price
            )

            if result["status"] == "success":
                self.entry_prices[token] = current_price

            return result

        return {
            "status": "success",
            "action": "WAIT"
          }
          
