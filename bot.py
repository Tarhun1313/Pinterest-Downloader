import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from handlers.function import download_and_send_media

# Вставляем твой новый токен
API_TOKEN = '8666841126:AAExc79z5RIuCwMukziPyt7EokvD3MfHnEI'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(F.text.contains("pinterest.com") | F.text.contains("pin.it"))
async def handle_pinterest_links(message: types.Message):
    url = message.text.strip()
    # Вызываем функцию из папки handlers
    await download_and_send_media(bot, message.chat.id, url)

@dp.message(F.text == "/start")
async def start_command(message: types.Message):
    await message.answer("👋 Привет! Пришли мне ссылку на Pinterest (видео или фото), и я скачаю её для тебя.")

async def main():
    # Удаляем вебхуки, чтобы не было конфликтов при запуске
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Бот остановлен")