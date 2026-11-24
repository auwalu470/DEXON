
from solana_connection import check_solana_connection, get_usdc_supply


def test_solana_connection():
    print("🚀 DEXON SOLANA TEST")

    health = check_solana_connection()
    assert health == "ok"

    usdc = get_usdc_supply()
    assert usdc["decimals"] == 6

    print("✅ SOLANA CONNECTION PASSED")
    print("USDC Decimals:", usdc["decimals"])


if __name__ == "__main__":
    test_solana_connection()
  
