import os
from telegram import PhotoSize, Bot

async def save_image(bot: Bot, photo: PhotoSize, user_id: int) -> str:
    """Downloads and saves the user's uploaded image to the 'images/' folder."""
    os.makedirs("images", exist_ok=True)
    image_path = f"images/user_{user_id}.jpg"
    
    # Download image
    file = await bot.get_file(photo.file_id)
    await file.download_to_drive(image_path)

    return image_path
