import asyncio
import logging
from bot import bot, dp
from handlers import start_router, pic_router, shop_router




async def main():
    # запуск бота
    dp.include_router(pic_router)
    dp.include_router(shop_router)
    dp.include_router(start_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
