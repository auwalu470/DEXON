
# DEXON Wallet Manager
# Safe wallet configuration

import os

class WalletManager:

    def __init__(self):
        self.network = "solana"
        self.currency = "USDC"
        self.wallet_address = os.getenv("SOLANA_WALLET_ADDRESS")

    def get_wallet_address(self):
        if not self.wallet_address:
            return "Wallet not connected"
        return self.wallet_address

    def get_network(self):
        return self.network

    def get_currency(self):
        return self.currency

    def wallet_status(self):
        return "Simulation Mode - No real funds connected"
