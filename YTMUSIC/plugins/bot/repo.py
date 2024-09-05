from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from BABYMUSIC import app
from config import BOT_USERNAME
from BABYMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ╼⃝𖠁 𝐁ʌʙʏ ꭙ 𝐌ᴜsɪᴄ 𖠁⃝╾ ʙᴏᴛ ✪
 
 ➲ ʙsᴅᴋ ʀᴇᴘᴏ ʟᴇɢᴀ ◉‿◉ ✰
 
 ➲ ᴘᴇʜʟᴇ ᴜᴛᴛᴀᴍ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟ ✰
 
 ➲ ᴄʜᴜᴘ ᴄʜᴜᴘ ʙᴏᴛ ʟᴇᴋᴇ ɴɪᴋᴀʟ ✰
 
 ➲ ʀᴇᴘᴏs ᴛᴏ ɴᴀʜɪ ᴍɪʟᴇɢᴀ ʙᴇᴛᴀ ⊂◉‿◉ ✰
 
 ➲ ᴀɢʀ ᴄʜᴀʜɪʏᴇ ᴛᴏ ᴜᴛᴛᴀᴍ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟɴᴀ ᴘᴀᴅᴇɢᴀ ✰
 
 ► ʀᴀᴅʜᴇ ʀᴀᴅʜᴇ ฅ( ̳• ◡ • ̳)ฅ
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("•ᴀᴅᴅ ᴍᴇ•", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("•sᴜᴘᴘᴏʀᴛ•", url="https://t.me/+j6FO8pK8IIkxZDU1"),
          InlineKeyboardButton("•ᴏᴡɴᴇʀ•", url="https://t.me/UTTAM470"),
          ],
               [
                InlineKeyboardButton("•ᴜᴘᴅᴀᴛᴇs•", url="https://t.me/BABY09_WORLD"),

],
[
              InlineKeyboardButton("•ʙᴀɴᴀʟʟ•", url=f"https://t.me/SATYABANALL_ROBOT"),
              InlineKeyboardButton("︎•ʏᴛ-ᴍᴜsɪᴄ•", url=f"https://t.me/YOUTUBE_RROBOT"),
              ],
              [
              InlineKeyboardButton("•ᴅᴇᴇᴘ ᴍᴜsɪᴄ•", url=f"https://t.me/DEEP_MUSIC_ROBOT"),
InlineKeyboardButton("•ᴄʜᴀᴛ ʙᴏᴛ•", url=f"https://t.me/RADHIKA_CHAT_RROBOT"),
],
[
InlineKeyboardButton("•sᴛʀɪɴɢ-ɢᴇɴ•", url=f"https://t.me/STRING_BABYGEN_BOT"),
InlineKeyboardButton("•ᴍᴀɴᴀɢᴍᴇɴᴛ•", url=f"https://t.me/SATYA_HELP97_BOT"),
],
[
              InlineKeyboardButton("•sᴘᴀᴍ-ʙᴏᴛ•", url=f"https://t.me/SATYASPAMROBOT"),
              InlineKeyboardButton("•ᴀᴘɴᴀ-ᴍᴜsɪᴄ•︎", url=f"https://t.me/MUSIC_OO_ROBOT"),
              ],
              [
              InlineKeyboardButton("•sᴛʀɪɴɢ ʜᴀᴄᴋ•", url=f"https://t.me/BABYSTRINGROBOT"),
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/a24eaa37b36f38695aba2.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/BABY-MUSIC/BABYTUNE/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[•ʙᴏᴛ-ᴏᴡɴᴇʀ•](https://t.me/UTTAM470) | [•ᴜᴘᴅᴀᴛᴇs•](https://t.me/BABY09_WORLD)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
