
from risk_manager import RiskManager

def test_risk_manager():

    risk = RiskManager(
        take_profit=20,
        stop_loss=10
    )

    assert risk.check_trade(100, 120) == "TAKE_PROFIT"
    assert risk.check_trade(100, 90) == "STOP_LOSS"
    assert risk.check_trade(100, 105) == "HOLD"

    print("🚀 DEXON RISK TEST")
    print("TAKE PROFIT: PASSED")
    print("STOP LOSS: PASSED")
    print("HOLD: PASSED")
    print("✅ RISK MANAGER PASSED")


if __name__ == "__main__":
    test_risk_manager()
