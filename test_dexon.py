from trading import TradingEngine

def test_dexon():
    bot = TradingEngine(100.00)

    print("🚀 DEXON SYSTEM TEST")
    print("Starting balance:", bot.get_balance())

    assert bot.get_balance() == 100.00

    print("✅ DEXON TEST PASSED")

if __name__ == "__main__":
    test_dexon()
