

import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube)
from AnonXMusic import app
from random import  choice, randint



@app.on_message(filters.command(["مميزات","✨مميزات"], ""))
async def mmmezat(client, message):
        await message.reply_text(f"""**مرحبآ بك عزيزي » {message.from_user.mention}**في قسم مميزات سورس ســــيزر ميوزك\n
⋖━━❲𖣂❳━━●○𝚂𝙴𝚉𝙰𝚁○●━━❲𖣂❳━━⋗

♡♕قايمه مميزات سورس ســــيزر 

♡♕ميزه ⦂ المطور بيجيب المطور البوت 
♡♕ميزه ⦂ تبيه بفتح+قفل الكول
♡♕ميزه ⦂ ترحيب دخول و خروج الاعضاء 
♡♕ميزه ⦂ جروب بيجيب الجروب+الرابط+ايدي
♡♕ميزه ⦂ قول البوت بيقول بالكلمه اللي بتقولها 
♡♕ميزه ⦂ الالعاب +كت+تويت+العاب متطوره
♡♕ميزه ⦂ تلغراف ميديا بردعالصوره
♡♕ميزه ⦂ ايدي بالرد بالصوره
♡♕ميزه ⦂ جمالي برد بالصوره ونسبه
♡♕ميزه ⦂ اذاعه خاص+بالتثبيت+بالمساعد+عام
♡♕ميزه ⦂ الصوتيه..ف كول
♡♕ميزه ⦂ نزول تلقائي للمساعد لعدم وجود حد فالكول
♡♕ميزه ⦂ بث مباشر للقنوات 
♡♕ميزه ⦂ اسمي بيجب الاسم
♡♕ميزه ⦂ سورس بيجب السورس
♡♕ميزه ⦂ حظر+كتم ميوزك
♡♕ميزه ⦂ كشف
♡♕ميزه ⦂ تاك لكل الاعضاء
♡♕ميزه ⦂ انا مين
♡♕ميزه ⦂ رتبتي
♡♕ميزه ⦂ مبرمج
♡♕ميزه ⦂ المنشئ+المالك
♡♕ميزه ⦂ الاحصائيات
♡♕ميزه ⦂ كيب المطور من خلاله تتحكم في الحساب المساعد
♡♕ميزه ⦂ الاذكار
♡♕ميزه ⦂ تبيه بوقت صلاه
♡♕ميزه ⦂ دعوه في كول
♡♕ميزه ⦂  دعوه فالخاص بتاع البوت
♡♕ميزه ⦂ تنبيه..بانضمام بوت في الجروبات
♡♕ميزه ⦂ غنيلي 
♡♕ميزه ⦂ بايو
♡♕ميزه ⦂ خروج المساعد من جروبات لعدم تقطيع صوت..البوت
♡♕ميزه ⦂ اسال/اصراحه
♡♕ميزه ⦂ نكت
♡♕ميزه ⦂ زخرفه 
♡♕ميزه ⦂ مميزات. بيجبلك مميزات موجوده فسورس 
♡♕ميزه ⦂ رفع و تنزيل مطور 
♡♕ميزه ⦂ افلام
♡♕ميزه ⦂ مكالمات النشطه+مجموعات البوت شغال فيها
♡♕ميزه ⦂ اساله دينيه
♡♕ميزه ⦂ مين فالكول+بتعرف مين فكول و عددهم
♡♕ميزه ⦂ انا فين+بتجلك جروب
♡♕ميزه ⦂ الرابط+رابط مجموعه
♡♕ميزه ⦂ فنان+اكتب اسم فنان و هتجبلك اغانيه
♡♕ميزه ⦂ اصدار+حول

⋖━━❲𖣂❳━━●○𝚂𝙴𝚉𝙰𝚁○●━━❲𖣂❳━━⋗""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗘𝗭𝗔𝗥", url=f"https://t.me/UIU_II"),                        
                 ],[
                InlineKeyboardButton(
                        "◁", callback_data="close"),
               ],
          ]
        ),
    )
