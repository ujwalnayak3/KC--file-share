from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT
from datetime import datetime
from helper_func import get_readable_time

@Bot.on_message(filters.command('status') & filters.private & is_admin)
async def info(client: Bot, message: Message):   
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("★ Cʟᴏsᴇ ★", callback_data = "close")]])
    
    start_time = time.time()
    temp_msg = await message.reply("<b><i>Pʀᴏᴄᴇssɪɴɢ....</i></b>", quote=True)  # Temporary message
    end_time = time.time()
    
    # Calculate ping time in milliseconds
    ping_time = (end_time - start_time) * 1000
    
    users = await full_userbase()
    now = datetime.now()
    delta = now - bot.uptime
    bottime = get_readable_time(delta.seconds)
    
    await temp_msg.edit(f"🫂 : <b>{len(users)} USERS\n\n🚀 UPTIME » {uptime}\n\n📡 PING » {ping_time:.2f} ms\n\n<u>👨‍💻 Developer : @PythonBotz</u></b>", reply_markup = reply_markup,)



@Bot.on_message(filters.private & filters.incoming)
async def useless(_,message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)
