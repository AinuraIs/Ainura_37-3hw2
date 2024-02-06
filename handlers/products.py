from aiogram import types, Router, F
from aiogram.filters import Command
from bot import bot
from db.quries import get_products

start_router = Router()

@pro_router.massege(Command('start'))
async def start(massage : types.Massage):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='shop', callback_data="shop")
    ]
  )

    await message.answer( text: f"привет" {message.from_user.username}", reply_markup=kb"


@start.router.callback_query(F.data == 'shop')
async def products(call: types.CallbackQuery):
        products = get_products()
        mes = ''
        for product in products:
            mes += (f"название {product[1]}\n"
                  f"цена {product[2]}")
            await message.answer(mes)

@start_router.message()
async def product(message: types.Message):
    pro=get_product(int(message.text))
    mes= (f"название" {pro[1]}\n"
          f"цена" {pro[2]}")
    await message.answer(mes)

