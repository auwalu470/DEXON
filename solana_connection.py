
import json
from urllib.request import Request, urlopen

SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"

USDC_MINT = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"


def rpc_call(method, params=None):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params or []
    }

    request = Request(
        SOLANA_RPC_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    with urlopen(request, timeout=20) as response:
        result = json.loads(response.read().decode("utf-8"))

    if "error" in result:
        raise RuntimeError(result["error"])

    return result["result"]


def check_solana_connection():
    return rpc_call("getHealth")


def get_usdc_supply():
    result = rpc_call(
        "getTokenSupply",
        [USDC_MINT, {"commitment": "confirmed"}]
    )

    return result["value"]


if __name__ == "__main__":
    print("DEXON SOLANA CONNECTION")

    print("Network:", check_solana_connection())

    usdc = get_usdc_supply()

    print("USDC Mint:", USDC_MINT)
    print("USDC Decimals:", usdc["decimals"])

    print("SOLANA USDC CONNECTION SUCCESSFUL")
  
