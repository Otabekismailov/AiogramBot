from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_category(category):
    keyboard_inline = InlineKeyboardMarkup()
    if len(category) % 2 == 0:
        category_ = None
    else:
        category_ = category.pop()
    for i in range(0, len(category) - 1, 2):
        keyboard_inline.add(InlineKeyboardButton(
            category[i].get("name"), callback_data=f'category_{category[i].get("id")}'
        ),
            InlineKeyboardButton(
                category[i + 1].get("name"), callback_data=f'category_{category[i + 1].get("id")}'
            ))

    if category_:
        keyboard_inline.add(
            InlineKeyboardButton(category_.get("name"), callback_data=f'category_{category_.get("id")}')
        )
    return keyboard_inline


def inline_category_parent(category_parent):
    keyboard_inline = InlineKeyboardMarkup()
    if len(category_parent) % 2 == 0:
        category_ = None
    else:
        category_ = category_parent.pop()
    for i in range(0, len(category_parent) - 1, 2):
        keyboard_inline.add(InlineKeyboardButton(
            category_parent[i].get("name"), callback_data=f'parent_{category_parent[i].get("id")}'
        ),
            InlineKeyboardButton(
                category_parent[i + 1].get("name"), callback_data=f'parent_{category_parent[i + 1].get("id")}'
            ))

    if category_:
        keyboard_inline.add(
            InlineKeyboardButton(category_.get("name"), callback_data=f'parent_{category_.get("id")}')
        )
    return keyboard_inline
