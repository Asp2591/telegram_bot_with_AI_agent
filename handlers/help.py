from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🤖 *Atharva AI Bot Commands:*\n\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n\n"
        "📸 *How to Use:*\n"
        "1️⃣ Send an image 📷\n"
        "2️⃣ Ask any question about the image ❓\n"
        "3️⃣ Get AI-powered insights 🚀"
    )
