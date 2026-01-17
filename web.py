from aiohttp import web
import asyncio

async def ʜᴀɴᴅʟᴇ(ʀᴇǫᴜᴇsᴛ):
    return web.Response(text="ʙᴏᴛ ɪs ʀᴜɴɴɪɴɢ ᴜʟᴛʀᴀ ꜰᴀsᴛ!")

def keep_alive():
    ᴀᴘᴘ = web.Application()
    ᴀᴘᴘ.router.add_get("/", ʜᴀɴᴅʟᴇ)
    ʀᴜɴɴᴇʀ = web.AppRunner(ᴀᴘᴘ)
    ʟᴏᴏᴘ = asyncio.get_event_loop()
    ʟᴏᴏᴘ.run_until_complete(ʀᴜɴɴᴇʀ.setup())
    sɪᴛᴇ = web.TCPSite(ʀᴜɴɴᴇʀ, '0.0.0.0', 8080)
    ʟᴏᴏᴘ.run_until_complete(sɪᴛᴇ.start())
