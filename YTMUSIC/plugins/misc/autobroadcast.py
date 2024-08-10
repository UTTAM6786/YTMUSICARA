import asyncio

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from pyrogram.errors import FloodWait

from YTMUSIC import app
from YTMUSIC.utils.database import get_served_users, delete_served_user


from config import OWNER_ID

MESSAGES = f"""๏ ᴛʜɪs ɪs {app.mention}!
 
 ➻ ᴀ ғᴀsᴛ & ᴘᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.
 
 Sᴜᴘᴘᴏʀᴛᴇᴅ Pʟᴀᴛғᴏʀᴍs : ʏᴏᴜᴛᴜʙᴇ, sᴘᴏᴛɪғʏ, ʀᴇssᴏ, ᴀᴘᴘʟᴇ ᴍᴜsɪᴄ ᴀɴᴅ sᴏᴜɴᴅᴄʟᴏᴜᴅ."""

BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "Αɗɗ ϻε ʈσ γσμɾ ɠɾσμρ",
                url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users",
            )
        ]
    ]
) 
 

async def send_message_to_chats():

    susers = await get_served_users()
    su = 0
    for user in susers:
        user_id = int(user["user_id"])
        if isinstance(user_id, int):
            try:
                await app.send_message(user_id, MESSAGES, reply_markup=BUTTONS)
                su+=1
            except FloodWait as e:
                await asyncio.sleep(e.value)
            except Exception as e:
                pass
    if su !=0:
        await app.send_message(OWNER_ID,f"Auto Broadcast Broadcasted the message to {su} users")


async def continuous_broadcast():
    while True:
        try:
            await send_message_to_chats()
        except Exception:
            pass
        await asyncio.sleep(100000)



asyncio.create_task(continuous_broadcast())
