from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    ABUTTON = [[InlineKeyboardButton("˹ sᴜᴘᴘᴏꝛᴛ ˼", url="https://t.me/+OL6jdTL7JAJjYzVl")],[InlineKeyboardButton("˹ ᴜᴘᴅᴧᴛᴇ ˼", url="https://t.me/BABY09_WORLD"),
    InlineKeyboardButton("˹ ᴧʟʟ ʙᴏᴛ ˼", url="https://t.me/+tHAENx_r_mtlODZl")],[InlineKeyboardButton("↺ ʙᴧᴄᴋ ↻", callback_data=f"settingsback_helper"),
    ]]

    UBUTTON = [[InlineKeyboardButton("˹ ᴍᴜsɪᴄ ˼", callback_data="settings_back_helper"),InlineKeyboardButton("˹ ᴛᴏᴏʟs ˼", callback_data=f"tbot_cb")],[InlineKeyboardButton("˹ ᴄʀᴇᴀᴛᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ ˼", callback_data="dplus HELP_host")],[InlineKeyboardButton("↺ ʙᴧᴄᴋ ↻", callback_data=f"settingsback_helper"),
    ]]

    TBUTTON = [[InlineKeyboardButton("˹ ᴀᴄᴛɪᴠᴇ ˼", callback_data="cplus HELP_active"),InlineKeyboardButton("˹ ᴀᴜᴛʜ ˼", callback_data="cplus HELP_auth")],[InlineKeyboardButton("˹ ʙʟᴏᴄᴋ ˼", callback_data="cplus HELP_block")],[InlineKeyboardButton("˹ ᴅᴇᴠ ˼", callback_data="cplus HELP_dev"),
    InlineKeyboardButton("˹ ɢ-ᴄᴀsᴛ ˼", callback_data="cplus HELP_gcast")],[InlineKeyboardButton("↺ ʙᴧᴄᴋ ↻", callback_data=f"ubot_cb"),
    ]]
