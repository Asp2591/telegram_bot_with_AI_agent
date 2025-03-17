import config
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from handlers.start import start
from handlers.help import help_command
from handlers.image_handler import handle_image
from handlers.text_handler import handle_text

def main() -> None:
    bot_app = Application.builder().token(config.TOKEN).build()

    # Register handlers
    bot_app.add_handler(CommandHandler("start", start))
    bot_app.add_handler(CommandHandler("help", help_command))
    bot_app.add_handler(MessageHandler(filters.PHOTO, handle_image))
    bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    print("AI-Enabled Telegram Bot (Image + Questions) is running... ✅")
    
    # Start bot
    bot_app.run_polling()

if __name__ == "__main__":
    main()
