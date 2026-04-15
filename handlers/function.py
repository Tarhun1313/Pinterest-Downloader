import yt_dlp
import os
import asyncio
from aiogram.types import FSInputFile

# Используй другой прокси из списка Webshare (например, второй по счету)
PROXY_URL = "http://ilxeikof:udka29wavxsw@198.23.239.134:6540" 

async def download_and_send_media(bot, chat_id, url):
    status = await bot.send_message(chat_id, "📌 Обработка Pinterest...")
    video_path = None
    try:
        ydl_opts = {
            'format': 'best', 
            'outtmpl': 'downloads/%(id)s.%(ext)s',
            'proxy': PROXY_URL,
            'nocheckcertificate': True,
            'quiet': True,
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'Referer': 'https://www.pinterest.com/'
            }
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = await asyncio.to_thread(ydl.extract_info, url, download=True)
            video_path = ydl.prepare_filename(info)

        await bot.send_video(chat_id, video=FSInputFile(video_path), caption="✅ Готово!")
    except Exception as e:
        await bot.send_message(chat_id, "❌ Не удалось скачать. Попробуй другую ссылку.")
    finally:
        if video_path and os.path.exists(video_path):
            os.remove(video_path)
        try: await bot.delete_message(chat_id, status.message_id)
        except: pass