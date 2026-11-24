
from trading import TradingEngine
from auto_trader import AutoTrader


def test_auto_trader():

    bot = TradingEngine(100.00)
    auto = AutoTrader(bot, trade_amount=10.00)

    print("🚀 DEXON AUTO TRADER TEST")

    # Test automatic buy
    buy = auto.process_trade(
        "BONK", 0.00002, "BUY"
    )

    assert buy["status"] == "success"
    assert bot.get_balance() == 90.00

    print("BUY TEST: PASSED")

    # Test Take Profit
    sell = auto.process_trade(
        "BONK", 0.000024
    )

    assert sell["status"] == "success"
    assert sell["action"] == "SELL"
    assert bot.get_balance() > 100.00

    print("TAKE PROFIT TEST: PASSED")
    print("FINAL BALANCE:", bot.get_balance())
    print("✅ AUTO TRADER PASSED")


if __name__ == "__main__":
    test_auto_trader()
  
