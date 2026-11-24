
import os
import logging

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

from trading import TradingEngine

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN not found")

bot = TradingEngine(100.00)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 WELCOME TO DEXON BOT!\n\n"
        "Solana USDC Trading System\n"
        "Mode: SIMULATION ONLY\n\n"
        "Commands:\n"
        "/balance - Check USDC\n"
        "/buy TOKEN AMOUNT PRICE\n"
        "/sell TOKEN QUANTITY PRICE\n"
        "/positions - Open positions\n"
        "/auto - Toggle auto mode\n"
        "/help - Commands"
    )


async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"💰 DEXON USDC Balance: ${bot.get_balance():.2f}"
    )


async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        token = context.args[0].upper()
        amount = float(context.args[1])
        price = float(context.args[2])

        result = bot.buy(token, amount, price)

        if result["status"] == "success":
            await update.message.reply_text(
                f"✅ SIMULATION BUY\n"
                f"Token: {token}\n"
                f"Spent: ${amount:.2f}\n"
                f"Quantity: {result['quantity']:.4f}\n"
                f"Balance: ${bot.get_balance():.2f}"
            )
        else:
            await update.message.reply_text(
                f"❌ {result['message']}"
            )

    except (IndexError, ValueError):
        await update.message.reply_text(
            "Usage: /buy BONK 10 0.00002"
        )


async def sell(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        token = context.args[0].upper()
        quantity = float(context.args[1])
        price = float(context.args[2])

        result = bot.sell(token, quantity, price)

        if result["status"] == "success":
            await update.message.reply_text(
                f"✅ SIMULATION SELL\n"
                f"Token: {token}\n"
                f"Received: ${result['received']:.2f}\n"
                f"PnL: ${result['pnl']:.2f}\n"
                f"Balance: ${bot.get_balance():.2f}"
            )
        else:
            await update.message.reply_text(
                f"❌ {result['message']}"
            )

    except (IndexError, ValueError):
        await update.message.reply_text(
            "Usage: /sell BONK 100000 0.000025"
        )


async def positions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not bot.positions:
        await update.message.reply_text("No open positions.")
        return

    message = "📊 DEXON POSITIONS\n\n"

    for token, position in bot.positions.items():
        message += (
            f"Token: {token}\n"
            f"Quantity: {position['quantity']:.4f}\n"
            f"Invested: ${position['invested']:.2f}\n\n"
        )

    await update.message.reply_text(message)


async def auto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status = bot.toggle_auto()

    message = "🟢 AUTO MODE ON" if status else "🔴 AUTO MODE OFF"

    await update.message.reply_text(
        message + "\nSimulation only. Live price monitoring is not connected."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("balance", balance))
    app.add_handler(CommandHandler("buy", buy))
    app.add_handler(CommandHandler("sell", sell))
    app.add_handler(CommandHandler("positions", positions))
    app.add_handler(CommandHandler("auto", auto))
    app.add_handler(CommandHandler("help", help_command))

    print("🚀 DEXON TELEGRAM BOT STARTED")

    app.run_polling()


if __name__ == "__main__":
    main()
