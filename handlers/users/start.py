import os

from aiogram import types
from pytube import YouTube

from loader import bot, dp


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom men muzanova.com saytidan Musiqa izlab sizga tasab beraman")


@dp.message_handler()
async def text_message(message: types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == "https://www.youtube.com/" or 'http://www.youtube.com':
        await bot.send_message(chat_id, f"*yuklanmoqda*: *{yt.title}*\n "  f"*©Manba*: [{yt.author}]({yt.channel_url})",
                               parse_mode="Markdown")
        await download_youtube_video(url, message, bot)


async def download_youtube_video(url, message, bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4')
    stream.get_highest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')
    with open(f"{message.chat.id}/{message.chat.id}_{yt.title}", 'rb') as video:
        await bot.send_video(message.chat.id, video, caption='botimiz orqali yuklab olindi', parse_mode='Markdown')
        os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}")