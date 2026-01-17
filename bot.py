import asyncio
import aiohttp
from pyrogram import Client, filters
from motor.motor_asyncio import AsyncIOMotorClient
from web import keep_alive

# ᴄᴏɴꜰɪɢᴜʀᴀᴛɪᴏɴ
API_ID = 23903140
API_HASH = "579f1bcf3eac1660d81ef34b09906012"
BOT_TOKEN = "8592003697:AAEYGaFeYVLofUXegjE5tUwqbstMDM0ACZM"
MONGO_URL = "YOUR_MONGODB_URL_HERE"

# ɪɴɪᴛɪᴀʟɪᴢᴇ ᴄʟɪᴇɴᴛs
app = Client("ᴜᴘᴛɪᴍᴇʙᴏᴛ", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, workers=100)
db_client = AsyncIOMotorClient(MONGO_URL)
db = db_client["ᴜᴘᴛɪᴍᴇ_ᴅʙ"]["ᴜʀʟs"]

async def ᴘɪɴɢᴇʀ():
    while True:
        ᴜʀʟ_ʟɪsᴛ = await db.find().to_list(length=1000)
        if ᴜʀʟ_ʟɪsᴛ:
            async with aiohttp.ClientSession() as sᴇssɪᴏɴ:
                ᴛᴀsᴋs = []
                for doc in ᴜʀʟ_ʟɪsᴛ:
                    ᴛᴀsᴋs.append(sᴇssɪᴏɴ.get(doc["url"], timeout=15))
                ʀᴇsᴜʟᴛs = await asyncio.gather(*ᴛᴀsᴋs, return_exceptions=True)
                print(f"ᴘɪɴɢᴇᴅ {len(ʀᴇsᴜʟᴛs)} ᴜʀʟs sᴜᴄᴄᴇssꜰᴜʟʟʏ.")
        await asyncio.sleep(300)

@app.on_message(filters.command("start"))
async def sᴛᴀʀᴛ(c, m):
    await m.reply_text("👋 ʜᴇʟʟᴏ! ɪ ᴀᴍ ᴀɴ ᴀɪ-ᴘᴏᴡᴇʀᴇᴅ ᴜᴘᴛɪᴍᴇ ᴘɪɴɢᴇʀ.\n\nsᴇɴᴅ /ᴀᴅᴅ [ᴜʀʟ] ᴛᴏ ᴋᴇᴇᴘ ʏᴏᴜʀ ᴀᴘᴘ ᴀʟɪᴠᴇ 24/7.")

@app.on_message(filters.command("add"))
async def ᴀᴅᴅ_ᴜʀʟ(c, m):
    if len(m.command) < 2:
        return await m.reply("❗ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ ᴜʀʟ.")
    ᴜʀʟ = m.command[1]
    if not await db.find_one({"url": ᴜʀʟ}):
        await db.insert_one({"url": ᴜʀʟ})
        await m.reply(f"🚀 ᴀᴅᴅᴇᴅ ᴛᴏ sʏsᴛᴇᴍ: `{ᴜʀʟ}`")
    else:
        await m.reply("ℹ️ ᴛʜɪs ᴜʀʟ ɪs ᴀʟʀᴇᴀᴅʏ ɪɴ ᴏᴜʀ ᴅᴀᴛᴀʙᴀsᴇ.")

if __name__ == "__main__":
    keep_alive()
    loop = asyncio.get_event_loop()
    loop.create_task(ᴘɪɴɢᴇʀ())
    app.run()
