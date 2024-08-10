from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from YTMUSIC import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text="𝐂ʟᴏsᴇ", callback_data=f"close")]
    second = [
        InlineKeyboardButton(
            text="𝐁ᴀᴄᴋ",
            callback_data=f"settingsback_helper",
        ),
       
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="𝐀ᴄᴛɪᴠᴇ",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="𝐀ᴅᴍɪɴ",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="𝐀ᴜᴛʜ",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝐁ʟᴏᴄᴋ",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="𝐁ᴏᴛ",
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text="𝐃ᴇᴠ",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝐆-ᴄᴀsᴛ",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="𝐏-ʟɪsᴛ",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="𝐏ʟᴀʏ",
                    callback_data="help_callback hb9",
                ),
            ], 
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="𝐁ᴀᴄᴋ",
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(text="𝐂ʟᴏsᴇ", callback_data=f"close"),
            ],
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐎ᴘᴇɴ ɪɴ ᴘʀɪᴠᴀᴛᴇ ", url=f"https://t.me/{app.username}?start=help"
            ),
        ],
    ]
    return buttons
