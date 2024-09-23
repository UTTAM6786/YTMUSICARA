from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    ABUTTON = [[InlineKeyboardButton("˹ sᴜᴘᴘᴏꝛᴛ ˼", url="https://t.me/+OL6jdTL7JAJjYzVl")],[InlineKeyboardButton("˹ ᴜᴘᴅᴧᴛᴇ ˼", url="https://t.me/BABY09_WORLD"),
    InlineKeyboardButton("˹ ᴧʟʟ ʙᴏᴛ ˼", url="https://t.me/+tHAENx_r_mtlODZl")],[InlineKeyboardButton("↺ ʙᴧᴄᴋ ↻", callback_data=f"settingsback_helper"),
    ]]

    UBUTTON = [[InlineKeyboardButton("˹ ᴍᴜsɪᴄ ˼", callback_data="settings_back_helper"),InlineKeyboardButton("˹ ᴛᴏᴏʟs ˼", callback_data=f"mbot_cb")],[InlineKeyboardButton("˹ ᴄʀᴇᴀᴛᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ ˼", callback_data="cplus HELP_raid")],[InlineKeyboardButton("↺ ʙᴧᴄᴋ ↻", callback_data=f"settingsback_helper"),
    ]]

    TBUTTON = [[InlineKeyboardButton("˹ ᴀᴄᴛɪᴠᴇ ˼", callback_data="help_callback hb1"),InlineKeyboardButton("˹ ᴀᴜᴛʜ ˼", callback_data="help_callback hb3")],[InlineKeyboardButton("˹ ʙʟᴏᴄᴋ ˼", callback_data="help_callback hb4")],[InlineKeyboardButton("˹ ᴅᴇᴠ ˼", callback_data="help_callback hb6"),
    InlineKeyboardButton("˹ ɢ-ᴄᴀsᴛ ˼", callback_data="help_callback hb7")],[InlineKeyboardButton("↺ ʙᴧᴄᴋ ↻", callback_data="cplus HELP_raid"),
    ]]
