from aiogram.types import InlineKeyboardMarkup

from bot.api import get_category

category = get_category()
category_ = ""
for i in category:
    category_ = InlineKeyboardMarkup(text=f"{i['name']}", callback_data=f"button_{i['id']}")
keyboard_inline = InlineKeyboardMarkup().add(category_)
