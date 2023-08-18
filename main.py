from aiogram import Dispatcher, executor, Bot, types
import os
from dotenv import load_dotenv

load_dotenv()
bot_tooken = os.getenv('TOKKEN_BOT')

bot = Bot(bot_tooken)
db = Dispatcher(bot)


@db.message_handler()
async def send_messages(message: types.Message):
    if message.text.count(' ') >= 1:
        await message.answer(text="Hellow Word")
    else:
        await message.answer(text="Goodbye")


if __name__ == '__main__':
    print("Star Bot .....")
    executor.start_polling(db)
