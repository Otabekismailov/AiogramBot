import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

from bot.api import user_create, get_category, get_category_parent, get_course_video
from button import inline_category, inline_category_parent

load_dotenv()

bot_token = os.getenv('TOKKEN_BOT')
bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_create(message.from_user.username, message.from_user.first_name, message.from_user.id)
    await message.answer(f"Welcome, {message.from_user.first_name}!")


@dp.message_handler(commands=['course'])
async def course(message: types.Message):
    category_list = get_category()
    await message.answer(f"Here's the course information.", reply_markup=inline_category(category_list))


# @dp.message_handler(text="video")
# async def course(message: types.Message):
#     # category_list = get_category()
#     await bot.send_video(chat_id=message.chat.id, video='BAACAgIAAxkBAAIBFmTkujhQrB9O909KniuACSmIBFMYAALtMwACtLooS0-VhdZZWMsWMAQ')
#     # await message.answer(f"Here's the course information.", reply_markup=inline_category(category_list))


@dp.callback_query_handler(lambda c: c.data.startswith("category_"))
async def course_category_parent(callback_query: types.CallbackQuery):
    category_id = callback_query.data.split('_')[1]
    category_parent = get_category_parent(category_id)
    await callback_query.message.answer(text="Course", reply_markup=inline_category_parent(category_parent))
    await callback_query.answer(cache_time=4)


@dp.callback_query_handler(lambda c: c.data.startswith("parent_"))
async def course_video(callback_query: types.CallbackQuery):
    course_id = callback_query.data.split('_')[1]
    data = get_course_video(course_id)
    for i in data:
        with open(f"../media/{i}", 'rb') as video:
            print(video)
            await callback_query.bot.send_video(chat_id=callback_query.message.chat.id, video=video)


@dp.message_handler(commands=['help'])
async def course(message: types.Message):
    await message.answer(f"I can help with that\n/start\n/course")


async def setup_bot_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("course", "Course"),
        # types.BotCommand("form", "Форма"),
        # types.BotCommand("menu", "Меню"),
    ])


if __name__ == '__main__':
    print("Start Bot ......")
    executor.start_polling(dp, skip_updates=True, on_startup=setup_bot_commands)
