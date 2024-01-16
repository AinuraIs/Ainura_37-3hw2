import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging
from pprint import pprint
from random import choice


load_dotenv()
TOKEN = getenv("Token")
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("pic"))
async def send_pic(message: types.Message):
    photos=["тупо-фотки-кошки-v0-axj9vcottrqb1.jpg",
            "pngtree-blue-bird-is-wearing-sunglasses-image_2583735.jpg",
            "kartinka.jpg"]
    photo = types.FSInputFile(f"images/{choice(photos)}")
    await message.answer_photo(photo=photo)

# обработка команды
# handler
@dp.message(Command("start"))
async def start(message: types.Message):
    pprint(message)
    await message.answer(f"Привет! {message.from_user.full_name}, ваш id: {message.from_user.id}")

@dp.message(Command("my_info"))
async def my_info(message: types.Message):
    pprint(message)
    await message.answer(f"Ваше имя: {message.from_user.full_name}\n"
                         f" ваш id: {message.from_user.id}\n"
                         f" ваш username: {message.from_user.username}")

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    # запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
