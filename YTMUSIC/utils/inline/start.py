from pyrogram.types import InlineKeyboardButton

import config
from YTMUSIC import app
from config import SUPPORT_CHAT, SUPPORT_CHANNEL, OWNER_ID

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="˹ sᴇᴛᴛɪɴɢ ˼", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="˹ sᴜᴘᴘᴏꝛᴛ ˼", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons
    
def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["❖ ᴛᴧᴘ тᴏ sᴇᴇ ᴍᴧɢɪᴄ ❖"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["˹ ❍ᴡɴᴇꝛ ˼"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["˹ ᴍᴏᴅᴇ ˼"], callback_data=f"modebot_cb"),
        ],
        [
            InlineKeyboardButton(text=_["˹ ᴧʙᴏᴜᴛ ˼"], callback_data=f"abot_cb"),
        ],
    ]
    return buttons
