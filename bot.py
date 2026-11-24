
"""
DEXON - Solana USDC DEX Trading Bot
Version 1.0
Simulation Mode
"""

import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "PASTE_YOUR_TELEGRAM_BOT_TOKEN_HERE"

keyboard = [
    ["📊 Balance", "🔎 Scan Tokens"],
    ["🟢 Manual Trade", "🤖 Auto Trade"],
    ["📈 My PnL", "⚙️ Settings"],
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply = ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True
    )
    await update.message.reply_text(
        "🚀 Welcome to DEXON!\n"
        "Solana USDC Trading Bot\n\n"
        "⚠️ Simulation Mode: No real trades.",
        reply_markup=reply,
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    choice = update.message.text

    responses = {
        "📊 Balance": "💵 Simulation USDC Balance: $100.00",
        "🔎 Scan Tokens": "🔎 Token scanner is under development.",
        "🟢 Manual Trade": "🟢 Manual trading is in simulation mode.",
        "🤖 Auto Trade": "🤖 Auto trading is not activated yet.",
        "📈 My PnL": "📈 Simulation PnL: $0.00",
        "⚙️ Settings": "⚙️ DEXON Settings",
    }

    await update.message.reply_text(
        responses.get(choice, "Choose an option from the menu.")
    )

def main():
    if BOT_TOKEN == "PASTE_YOUR_TELEGRAM_BOT_TOKEN_HERE":
        raise ValueError("Please configure your Telegram bot token.")

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, menu)
    )
    app.run_polling()

if __name__ == "__main__":
    main()
