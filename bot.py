
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import BOT_TOKEN, STARTING_BALANCE
from trading import TradingEngine
from scanner import scan_tokens

logging.basicConfig(level=logging.INFO)

engine = TradingEngine(STARTING_BALANCE)

keyboard = [
    ["📊 Balance", "🔎 Scan Tokens"],
    ["🟢 Manual Trade", "🤖 Auto Trade"],
    ["📈 My PnL", "⚙️ Settings"],
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    menu = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "🚀 Welcome to DEXON!\n"
        "Solana USDC Trading Bot\n"
        "Simulation Mode Only.",
        reply_markup=menu,
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    choice = update.message.text

    if choice == "📊 Balance":
        await update.message.reply_text(
            f"💵 Simulation Balance: ${engine.get_balance():.2f} USDC"
        )

    elif choice == "🔎 Scan Tokens":
        tokens = scan_tokens()

        if isinstance(tokens, dict):
            await update.message.reply_text("Scanner error. Try again later.")
        elif not tokens:
            await update.message.reply_text("No Solana tokens found.")
        else:
            message = "🔎 DEXON SOLANA SCANNER\n\n"
            for token in tokens[:10]:
                message += (
                    f"Token: {token['address']}\n"
                    f"Chart: {token['url']}\n\n"
                )
            await update.message.reply_text(message)

    elif choice == "🟢 Manual Trade":
        await update.message.reply_text(
            "Manual trading is in development.\n"
            "Simulation mode only."
        )

    elif choice == "🤖 Auto Trade":
        status = engine.toggle_auto()
        await update.message.reply_text(
            f"Auto Trading: {'ON' if status else 'OFF'}\n"
            "Simulation only."
        )

    elif choice == "📈 My PnL":
        await update.message.reply_text(
            "📈 Simulation PnL: $0.00"
        )

    elif choice == "⚙️ Settings":
        await update.message.reply_text(
            "DEXON Settings\n"
            "Network: Solana\n"
            "Currency: USDC\n"
            "Mode: Simulation"
        )

    else:
        await update.message.reply_text("Choose an option from the menu.")

def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is missing. Configure it securely.")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    print("DEXON is starting...")
    app.run_polling()

if __name__ == "__main__":
    main()
    
