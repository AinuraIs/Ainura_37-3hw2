import asyncio
import logging
from aiogram import types
from bot import dp, bot
from db.quries import init_db, create_tables
from handlers import start_router

async def on_startapp():
    init_db()
    create_tables()
    # fill_db()
    print('база данных подключена')


async def main():
    await bot.set_my_commands([
    types.BotCommand(command="start", description="Начало"),

    ])
    dp.include_router(start_router)
    dp.startup.register(on_startapp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())