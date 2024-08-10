from pyrogram.types import InlineKeyboardButton

import config
from YTMUSIC import app
from config import SUPPORT_CHAT, SUPPORT_CHANNEL, OWNER_ID

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="𝐒ᴇᴛᴛɪɴɢ", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="𝐒ɢʀᴏᴜᴘ", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons
    
def private_panel(_):
    buttons = [
        [InlineKeyboardButton(text="𝐇ᴏᴡ ᴛᴏ 𝐔sᴇ? 𝐂ᴏᴍᴍᴀɴᴅ 𝐌ᴇɴᴜ", callback_data="settings_back_helper")]
    ]
    if SUPPORT_CHANNEL and SUPPORT_CHAT:
        buttons.append(
            [
                InlineKeyboardButton(text="𝐂ʜᴀɴɴᴇʟ", url=f"{SUPPORT_CHANNEL}"),
                InlineKeyboardButton(text="𝐒ᴜᴘᴘᴏʀᴛ", url=f"{SUPPORT_CHAT}"),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [InlineKeyboardButton(text="𝐂ʜᴀɴɴᴇʟ", url=f"{SUPPORT_CHANNEL}")]
            )
        if SUPPORT_CHAT:
            buttons.append(
                [InlineKeyboardButton(text="𝐒ᴜᴘᴘᴏʀᴛ", url=f"{SUPPORT_CHAT}")]
            )
    buttons.append(
        [
            InlineKeyboardButton(
                text= "𝐀ᴅᴅ 𝐌ᴇ 𝐁ᴀʙʏ ",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ]
    )
    buttons.append(
        [
            InlineKeyboardButton(text="𝐎ᴡɴᴇʀ", user_id=OWNER_ID),
        ]
    )
    return buttons
