from aiogram import Router, F, types
from aiogram.filters import Command
from pprint import pprint

shop_router = Router()

@shop_router.callback_query(F.data == 'shop')
async def shop(call: types.CallbackQuery):
    await call.answer()
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Books"),
                types.KeyboardButton(text="Manga"),
                types.KeyboardButton(text="Comics"),
            ],

        ]
    )
    await call.message.answer(f"Вот наши товары", reply_markup=kb)

@shop_router.message(F.text == 'Books')
async def book(message: types.Message):
    await message.answer(f"Книга источник знаний")

@shop_router.message(F.text == 'Manga')
async def manga(message: types.Message):
    await message.answer(f"Манга это японский комикс")

@shop_router.message(F.text == 'Comics')
async def comics(message: types.Message):
    await message.answer(f"Комиксы это книги с картинками")


