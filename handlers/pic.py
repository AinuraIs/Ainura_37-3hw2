from aiogram import Router, F, types
from aiogram.filters import Command
from pprint import pprint
from random import choice

pic_router = Router()

@pic_router.message(Command("pic"))
async def send_pic(message: types.Message):
    photos=["тупо-фотки-кошки-v0-axj9vcottrqb1.jpg",
            "pngtree-blue-bird-is-wearing-sunglasses-image_2583735.jpg",
            "kartinka.jpg"]
    photo = types.FSInputFile(f"images/{choice(photos)}")
    await message.answer_photo(photo=photo)



