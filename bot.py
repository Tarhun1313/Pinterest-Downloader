import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from handlers.function import download_and_send_media

# Твой токен для Pinterest
API_TOKEN = '8666841126:AAExc79z5RIuCwMukziPyt7EokvD3MfHnEI'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Реагирует на ссылки Pinterest
@dp.message(F.text.contains("pinterest.com") | F.text.contains("pin.it"))
async def handle_pin_link(message: types.Message):
    await download_and_send_media(bot, message.chat.id, message.text.strip())

@dp.message(F.command("start"))
async def cmd_start(message: types.Message):
    await message.answer("📌 Привет! Пришли ссылку на пин, и я попробую его скачать.")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
