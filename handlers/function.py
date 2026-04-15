import yt_dlp
import os
import asyncio
import random
from aiogram.types import FSInputFile

PROXIES = [
    "http://ilxeikof:udka29wavxsw@198.23.239.134:6540",
    "http://ilxeikof:udka29wavxsw@31.59.20.176:6754",
    "http://ilxeikof:udka29wavxsw@31.58.9.4:5392",
    "http://ilxeikof:udka29wavxsw@142.111.67.146:5867",
    "http://ilxeikof:udka29wavxsw@172.245.158.151:6558"
]

async def download_and_send_media(bot, chat_id, url):
    status = await bot.send_message(chat_id, "⏳ Подбираю рабочий канал скачивания...")
    video_path = None
    random.shuffle(PROXIES)

    for proxy in PROXIES:
        try:
            ydl_opts = {
                'format': 'bestvideo[height<=720]+bestaudio/best' if "youtube" in url else 'best',
                'outtmpl': f'downloads/%(id)s_{random.randint(1,1000)}.%(ext)s',
                'proxy': proxy,
                'nocheckcertificate': True,
                'quiet': True,
                'extractor_args': {'youtube': {'player_client': ['android', 'ios']}},
                'addheaders': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0.0.0 Safari/537.36'}
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = await asyncio.to_thread(ydl.extract_info, url, download=True)
                video_path = ydl.prepare_filename(info)
            
            if video_path and os.path.exists(video_path):
                await bot.send_video(chat_id, video=FSInputFile(video_path), caption="🎬 Готово!")
                break
        except Exception as e:
            print(f"Ошибка прокси {proxy}: {e}")
            continue
    else:
        await bot.send_message(chat_id, "❌ Все доступные способы временно заблокированы. Попробуй другую ссылку позже.")

    if video_path and os.path.exists(video_path):
        os.remove(video_path)
    try:
        await bot.delete_message(chat_id, status.message_id)
    except:
        pass
