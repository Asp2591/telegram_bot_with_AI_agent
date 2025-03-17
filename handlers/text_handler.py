from telegram import Update
from telegram.ext import ContextTypes
from ai_agent import image_text_agent
from handlers.image_handler import user_images

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    user_message = update.message.text

    if user_id in user_images:
        image_path = user_images[user_id]
        try:
            response = image_text_agent.run(user_message, images=[image_path]).content
            await update.message.reply_text(response)
        except Exception:
            await update.message.reply_text("Error processing your request.")
    else:
        await update.message.reply_text("Please send an image first, then ask a question about it.")
