import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

from bot.api import user_create
from button import category_, keyboard_inline

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
    user_create(message.from_user.username, message.from_user.first_name, message.from_user.id)
    await message.answer(f"Here's the course information.", reply_markup=keyboard_inline)


@dp.message_handler(commands=['help'])
async def course(message: types.Message):
    user_create(message.from_user.username, message.from_user.first_name, message.from_user.id)
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
