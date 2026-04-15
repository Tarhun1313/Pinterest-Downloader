import asyncio
from aiogram import Bot, Dispatcher, F, types
from handlers.function import download_and_send_media

# Твой новый токен для Pinterest
API_TOKEN = '8666841126:AAExc79z5RIuCwMukziPyt7EokvD3MfHnEI'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(F.text.contains("pinterest.com") | F.text.contains("pin.it"))
async def handle_pin(message: types.Message):
    await download_and_send_media(bot, message.chat.id, message.text.strip())

@dp.message(F.command("start"))
async def start(message: types.Message):
    await message.answer("👋 Привет! Просто кинь ссылку на Pinterest.")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
