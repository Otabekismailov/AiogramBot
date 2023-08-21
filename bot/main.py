from aiogram import Dispatcher, executor, Bot, types
import os
from dotenv import load_dotenv

from bot.api import user_create
from aiogram.types import MenuButtonCommands
load_dotenv()
bot_tooken = os.getenv('TOKKEN_BOT')

bot = Bot(bot_tooken)
db = Dispatcher(bot)


@db.message_handler(commands="start")
async def add_user(message: types.Message):
    user_create(message.from_user.username, message.from_user.first_name, message.from_user.id, )
    await message.answer(text=f"Welcom {message.from_user.first_name}")


@db.message_handler(commands="/curse")
async def get_course(message: types.Message):
    user_create(message.from_user.username, message.from_user.first_name, message.from_user.id, )
    await message.answer(text=f"Welcom {message.from_user.first_name}")

async def setup_bot_commands():
    bot_commands = [
        types.BotCommand(command="/help", description="Get info about me"),
        types.BotCommand(command="/qna", description="set bot for a QnA task"),
        types.BotCommand(command="/chat", description="set bot for free chat")
    ]
    await bot.set_my_commands(bot_commands)

if __name__ ==  '__main__':
    print("Star Bot .....")
    executor.start_polling(db, skip_updates=True,on_startup=setup_bot_commands)
    # executor.start_polling(db)
