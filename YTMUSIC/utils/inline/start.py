from pyrogram.types import InlineKeyboardButton

import config
from YTMUSIC import app
from config import SUPPORT_CHAT, SUPPORT_CHANNEL, OWNER_ID

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="• sᴇᴛᴛɪɴɢ •", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="• sᴜᴘᴘᴏꝛᴛ •", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons
    
def private_panel(_):
    buttons = [
        [InlineKeyboardButton(text="• ʜᴏᴡ ᴛᴏ ᴜsᴇ? ᴄᴏᴍᴍᴀɴᴅ ᴍᴇɴᴜ •", callback_data="settings_back_helper")]
    ]
    if SUPPORT_CHANNEL and SUPPORT_CHAT:
        buttons.append(
            [
                InlineKeyboardButton(text="• ᴄʜᴀɴɴᴇʟ •", url=f"{SUPPORT_CHANNEL}"),
                InlineKeyboardButton(text="• sᴜᴘᴘᴏꝛᴛ •", url=f"{SUPPORT_CHAT}"),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [InlineKeyboardButton(text="• ᴄʜᴀɴɴᴇʟ •", url=f"{SUPPORT_CHANNEL}")]
            )
        if SUPPORT_CHAT:
            buttons.append(
                [InlineKeyboardButton(text="• sᴜᴘᴘᴏꝛᴛ •", url=f"{SUPPORT_CHAT}")]
            )
    buttons.append(
        [
            InlineKeyboardButton(
                text= "• ᴧᴅᴅ мᴇ ʙᴧʙʏ •",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ]
    )
    buttons.append(
        [
            InlineKeyboardButton(text="• ❍ᴡɴᴇꝛ •", user_id=OWNER_ID),
        ]
    )
    return buttons
