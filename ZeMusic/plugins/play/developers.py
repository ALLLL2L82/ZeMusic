import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
  
@app.on_message(filters.command(["مودي","المبرمج حمد","مبرمج السورس","مبرمج"],"")
               )                   
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/018bff5d227366a421b6f.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[𝐘 𝐙 𝐍](https://t.me/CZCRR)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @O_U_QA ❫
◉ 𝙸𝙳      : ❪ `6189288231` ❫
◉ 𝙱𝙸𝙾    : ❪ for me حقاً لَن تصبح مَثلي ❴ @CZCRR0 ❵ ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝐘 𝐙 𝐍", url=f"https://t.me/CZCRR"), 
                 ],[
                   InlineKeyboardButton(
                        "𝐘 𝐙 𝐍", url=f"https://t.me/CZCRR"),
                ],

            ]

        ),

    )
