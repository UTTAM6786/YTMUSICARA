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
    
def private_panel(is_owner):
    buttons = []
    
    buttons.append(
        [InlineKeyboardButton(text="❖ ᴛᴧᴘ тᴏ sᴇᴇ ᴍᴧɢɪᴄ ❖", url=f"https://t.me/{app.username}?startgroup=true")]
    )
    
    if is_owner:
        buttons.append(
            [
                InlineKeyboardButton(text="˹ ❍ᴡɴᴇꝛ ˼", user_id=OWNER_ID),
                InlineKeyboardButton(text="˹ ᴍᴏᴅᴇ ˼", callback_data="ubot_cb"),
            ]
        )
    else:
        buttons.append(
            [InlineKeyboardButton(text="˹ ᴧʙᴏᴜᴛ ˼", callback_data=f"abot_cb")]
        )
        
    return buttons
