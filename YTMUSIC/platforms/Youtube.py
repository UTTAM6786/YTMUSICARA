import asyncio
import aiohttp
import requests
import httpx
import os
import re
from typing import Union

import yt_dlp
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from youtubesearchpython.__future__ import VideosSearch

from YTMUSIC.utils.database import is_on_off
from YTMUSIC.utils.formatters import time_to_seconds, download_file



async def shell_cmd(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    out, errorz = await proc.communicate()
    if errorz:
        if "unavailable videos are hidden" in (errorz.decode("utf-8")).lower():
            return out.decode("utf-8")
        else:
            return errorz.decode("utf-8")
    return out.decode("utf-8")
    
# Netscape HTTP Cookie File
# https://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file! Do not edit.

.youtube.com	TRUE	/	TRUE	0	YSC	4ZlXDbi-LS4
.youtube.com	TRUE	/	TRUE	1740396943	VISITOR_INFO1_LIVE	kDTLqKDC8sc
.youtube.com	TRUE	/	TRUE	1740396943	VISITOR_PRIVACY_METADATA	CgJJThIEGgAgFw%3D%3D
.youtube.com	TRUE	/	TRUE	1724846744	GPS	1
.youtube.com	TRUE	/	TRUE	1756380988	__Secure-1PSIDTS	sidts-CjEBUFGohzWJmyJOT0ex6nBGDiMRoCCASOm1ABXkZbwXkPX1fGV1zNYiyqkK2-LX5qdcEAA
.youtube.com	TRUE	/	TRUE	1756380988	__Secure-3PSIDTS	sidts-CjEBUFGohzWJmyJOT0ex6nBGDiMRoCCASOm1ABXkZbwXkPX1fGV1zNYiyqkK2-LX5qdcEAA
.youtube.com	TRUE	/	FALSE	1787916988	HSID	A1cekU3FdmtWGML4c
.youtube.com	TRUE	/	TRUE	1787916988	SSID	AR5884io3moBK6mBg
.youtube.com	TRUE	/	FALSE	1787916988	APISID	60NLF9KM6AaPpMny/ATCSaMc9IBIo9mJTi
.youtube.com	TRUE	/	TRUE	1787916988	SAPISID	MbvscBjneSu3S7Px/Aoik_JTK4AmGYn9hA
.youtube.com	TRUE	/	TRUE	1787916988	__Secure-1PAPISID	MbvscBjneSu3S7Px/Aoik_JTK4AmGYn9hA
.youtube.com	TRUE	/	TRUE	1787916988	__Secure-3PAPISID	MbvscBjneSu3S7Px/Aoik_JTK4AmGYn9hA
.youtube.com	TRUE	/	FALSE	1787916988	SID	g.a000nQhoYNU7u5lW_DevWVjzDaNeduXmnFVvDCDU8-745s1k8AEMmLOAjbsjTK6pdKQhRFX_OQACgYKAb0SARISFQHGX2MiB6EpJKLqPYVuvvUFoMBYdRoVAUF8yKpK73HSj1mnaP34szI6VUmz0076
.youtube.com	TRUE	/	TRUE	1787916988	__Secure-1PSID	g.a000nQhoYNU7u5lW_DevWVjzDaNeduXmnFVvDCDU8-745s1k8AEMIvIdqvOLM39Z3NgJ4clquwACgYKAYsSARISFQHGX2Miqm-3crnEJMPAu-KRtlVFpxoVAUF8yKpsU3bpihO8Hfa9dlt-ifl-0076
.youtube.com	TRUE	/	TRUE	1787916988	__Secure-3PSID	g.a000nQhoYNU7u5lW_DevWVjzDaNeduXmnFVvDCDU8-745s1k8AEMayqDtbalOa6nAQR4Gpm3pgACgYKAZgSARISFQHGX2Mi__eyr8J3cnEPsBUjPQPcBhoVAUF8yKpFBMGqK9ZQidqJffnThFkD0076
.youtube.com	TRUE	/	TRUE	1787916990	LOGIN_INFO	AFmmF2swRgIhANxFBw_7YM9L-12FXGwK2eyGFhnHXdh2Gwr46IcXZ-U0AiEA5XvgbovHloPwrMlxYOK_rXyGiOyWccm-mjGlC81-8oc:QUQ3MjNmdzY1alY4SnFGcWhYMzJQOFE5T2pQdHdGdk01V3pSSERMa1ZvemVDTlhxWm1pWDd6d3NWLUFBTE9HcEY0NDRmeHdrQWtCWjcyRWRuOWdZWGNxRmR1SU12QmdjT2xrVzVjTjJxWFJicnZjY1kxMU1jWjlrSk5iWHVYRjh3b1g5bDVzdGpra0RHNlU2N01mb0prZDkwZ3ExY0o1aHV3
.youtube.com	TRUE	/	TRUE	1787916989	PREF	f6=40000000&tz=Asia.Kolkata
.youtube.com	TRUE	/	FALSE	1756380994	SIDCC	AKEyXzU9YrVZY3jbcRONvWq-stEPY2XVG4OUQJG_9d20kRjRfKYgBpd8yVI_5_gofOD5_eigPw
.youtube.com	TRUE	/	TRUE	1756380994	__Secure-1PSIDCC	AKEyXzU3WcCim1vsfFV22udm99XB3JGcTN7tlDO2AQXvDSLi5ueV6E1yXWnnKzPKwHAKK0Rs
.youtube.com	TRUE	/	TRUE	1756380994	__Secure-3PSIDCC	AKEyXzXXAPLT_tffN-xdVkFBAT7iVGNlAJV4lTui_ZyM020PLD3PuNra1QTg9BVv4-XfhBphyw

class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.regex = r"(?:youtube\.com|youtu\.be)"
        self.status = "https://www.youtube.com/oembed?url="
        self.listbase = "https://youtube.com/playlist?list="
        self.reg = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    async def exists(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if re.search(self.regex, link):
            return True
        else:
            return False

    async def url(self, message_1: Message) -> Union[str, None]:
        messages = [message_1]
        if message_1.reply_to_message:
            messages.append(message_1.reply_to_message)
        text = ""
        offset = None
        length = None
        for message in messages:
            if offset:
                break
            if message.entities:
                for entity in message.entities:
                    if entity.type == MessageEntityType.URL:
                        text = message.text or message.caption
                        offset, length = entity.offset, entity.length
                        break
            elif message.caption_entities:
                for entity in message.caption_entities:
                    if entity.type == MessageEntityType.TEXT_LINK:
                        return entity.url
        if offset in (None,):
            return None
        return text[offset : offset + length]

    async def details(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            title = result["title"]
            duration_min = result["duration"]
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            vidid = result["id"]
            if str(duration_min) == "None":
                duration_sec = 0
            else:
                duration_sec = int(time_to_seconds(duration_min))
        return title, duration_min, duration_sec, thumbnail, vidid

    async def title(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            title = result["title"]
        return title

    async def duration(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            duration = result["duration"]
        return duration

    async def thumbnail(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        return thumbnail

    async def video(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        proc = await asyncio.create_subprocess_exec(
            "yt-dlp",
            "-g",
            "-f",
            "best[height<=?720][width<=?1280]",
            f"{link}",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        if stdout:
            return 1, stdout.decode().split("\n")[0]
        else:
            return 0, stderr.decode()

    async def playlist(self, link, limit, user_id, videoid: Union[bool, str] = None):
        if videoid:
            link = self.listbase + link
        if "&" in link:
            link = link.split("&")[0]
        playlist = await shell_cmd(
            f"yt-dlp -i --get-id --flat-playlist --playlist-end {limit} --skip-download {link}"
        )
        try:
            result = playlist.split("\n")
            for key in result:
                if key == "":
                    result.remove(key)
        except:
            result = []
        return result

    async def track(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            title = result["title"]
            duration_min = result["duration"]
            vidid = result["id"]
            yturl = result["link"]
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        track_details = {
            "title": title,
            "link": yturl,
            "vidid": vidid,
            "duration_min": duration_min,
            "thumb": thumbnail,
        }
        return track_details, vidid

    async def formats(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        ytdl_opts = {"quiet": True}
        ydl = yt_dlp.YoutubeDL(ytdl_opts)
        with ydl:
            formats_available = []
            r = ydl.extract_info(link, download=False)
            for format in r["formats"]:
                try:
                    str(format["format"])
                except:
                    continue
                if not "dash" in str(format["format"]).lower():
                    try:
                        format["format"]
                        format["filesize"]
                        format["format_id"]
                        format["ext"]
                        format["format_note"]
                    except:
                        continue
                    formats_available.append(
                        {
                            "format": format["format"],
                            "filesize": format["filesize"],
                            "format_id": format["format_id"],
                            "ext": format["ext"],
                            "format_note": format["format_note"],
                            "yturl": link,
                        }
                    )
        return formats_available, link

    async def slider(
        self,
        link: str,
        query_type: int,
        videoid: Union[bool, str] = None,
    ):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        a = VideosSearch(link, limit=10)
        result = (await a.next()).get("result")
        title = result[query_type]["title"]
        duration_min = result[query_type]["duration"]
        vidid = result[query_type]["id"]
        thumbnail = result[query_type]["thumbnails"][0]["url"].split("?")[0]
        return title, duration_min, thumbnail, vidid

    async def download(
        self,
        link: str,
        mystic,
        video: Union[bool, str] = None,
        videoid: Union[bool, str] = None,
        songaudio: Union[bool, str] = None,
        songvideo: Union[bool, str] = None,
        format_id: Union[bool, str] = None,
        title: Union[bool, str] = None,
    ) -> str:
        if videoid:
            link = self.base + link
        loop = asyncio.get_running_loop()

        def audio_dl():
            ydl_optssx = {
                "format": "bestaudio/[ext=m4a]",
                "outtmpl": "downloads/%(id)s.%(ext)s",
                "geo_bypass": True,
                "nocheckcertificate": True,
                "quiet": True,
                "no_warnings": True,
            }
            x = yt_dlp.YoutubeDL(ydl_optssx)
            info = x.extract_info(link, False)
            xyz = os.path.join("downloads", f"{info['id']}.{info['ext']}")
            if os.path.exists(xyz):
                return xyz
            x.download([link])
            return xyz

        def video_dl():
            ydl_optssx = {
                "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])",
                "outtmpl": "downloads/%(id)s.%(ext)s",
                "geo_bypass": True,
                "nocheckcertificate": True,
                "quiet": True,
                "no_warnings": True,
            }
            x = yt_dlp.YoutubeDL(ydl_optssx)
            info = x.extract_info(link, False)
            xyz = os.path.join("downloads", f"{info['id']}.{info['ext']}")
            if os.path.exists(xyz):
                return xyz
            x.download([link])
            return xyz

        def song_video_dl():
            formats = f"{format_id}+140"
            fpath = f"downloads/{title}"
            ydl_optssx = {
                "format": formats,
                "outtmpl": fpath,
                "geo_bypass": True,
                "nocheckcertificate": True,
                "quiet": True,
                "no_warnings": True,
                "prefer_ffmpeg": True,
                "merge_output_format": "mp4",
            }
            x = yt_dlp.YoutubeDL(ydl_optssx)
            x.download([link])

        def song_audio_dl():
            fpath = f"downloads/{title}.%(ext)s"
            ydl_optssx = {
                "format": format_id,
                "outtmpl": fpath,
                "geo_bypass": True,
                "nocheckcertificate": True,
                "quiet": True,
                "no_warnings": True,
                "prefer_ffmpeg": True,
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ],
            }
            x = yt_dlp.YoutubeDL(ydl_optssx)
            x.download([link])

        if songvideo:
            await loop.run_in_executor(None, song_video_dl)
            fpath = f"downloads/{title}.mp4"
            return fpath
        elif songaudio:
            await loop.run_in_executor(None, song_audio_dl)
            fpath = f"downloads/{title}.mp3"
            return fpath
        elif video:
            if await is_on_off(1):
                direct = True
                downloaded_file = await loop.run_in_executor(None, video_dl)
            else:
                proc = await asyncio.create_subprocess_exec(
                    "yt-dlp",
                    "-g",
                    "-f",
                    "best[height<=?720][width<=?1280]",
                    f"{link}",
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE,
                )
                stdout, stderr = await proc.communicate()
                if stdout:
                    downloaded_file = stdout.decode().split("\n")[0]
                    direct = None
                else:
                    return
        else:
            direct = True
            downloaded_file = await loop.run_in_executor(None, audio_dl)
        return downloaded_file, direct

class YTM:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.regex = r"(?:youtube\.com|youtu\.be)"
        self.status = "https://www.youtube.com/oembed?url="
        self.listbase = "https://youtube.com/playlist?list="
        self.reg = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")


    async def download(
        self,
        link: str,
        mystic,
        video: Union[bool, str] = None,
        videoid: Union[bool, str] = None,
        songaudio: Union[bool, str] = None,
        songvideo: Union[bool, str] = None,
        format_id: Union[bool, str] = None,
        title: Union[bool, str] = None,
    ) -> str:
        if videoid:
            vidid =  link
        else:
            pattern = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=|embed\/|v\/|live_stream\?stream_id=|(?:\/|\?|&)v=)?([^&\n]+)"
            match = re.search(pattern, link)
            vidid = match.group(1)
        
        async def download(url, format):
            async with httpx.AsyncClient(http2=True) as client:
                response = await client.get(url)
                file_path = os.path.join("downloads", f"{vidid}.{format}")
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                return file_path
             
        
        '''loop = asyncio.get_running_loop()
        
        if songvideo:
            
            return await loop.run_in_executor(None, download_file,vidid,False)
            
        elif songaudio:
            return await loop.run_in_executor(None, download_file,vidid)
            
        
        elif video:
            direct = True
            downloaded_file = await loop.run_in_executor(None, download_file,vidid,False)

        
        else:
            direct = True
            downloaded_file = await loop.run_in_executor(None, download_file,vidid)
        
        return downloaded_file, direct'''
 
        response =  requests.get(f"https://pipedapi-libre.kavin.rocks/streams/{vidid}").json()
        loop = asyncio.get_running_loop()
        
        if songvideo:
            
            url = response.get("videoStreams", [])[-1]['url']
            fpath = await loop.run_in_executor(None, lambda: asyncio.run(download(url, "mp4")))
            return fpath
            
        elif songaudio:
             return response.get("audioStreams", [])[4]["url"]  
            
        
        elif video:
            url = response.get("videoStreams", [])[-1]['url']
            direct = True
            downloaded_file = await loop.run_in_executor(None, lambda: asyncio.run(download(url, "mp4")))

        
        else:
            direct = True
            downloaded_file = response.get("audioStreams", [])[4]["url"]  
        
        return downloaded_file, direct
       
       
