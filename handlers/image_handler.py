from telegram import Update
from telegram.ext import ContextTypes
from utils.download import save_image

# Store user image paths
user_images = {}

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    photo = update.message.photo[-1]  # Get highest resolution image

    # Download and save image
    image_path = await save_image(context.bot, photo, user_id)
    user_images[user_id] = image_path

    await update.message.reply_text("✅ Image received! Now, ask any question about it.")
