import asyncio
import aiohttp
from pyrogram import Client, filters
from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

db_client = AsyncIOMotorClient(Config.MONGO_URL)
db = db_client["uptime_db"]["urls"]

@Client.on_message(filters.command("add") & filters.private)
async def add_url(client, message):
    if len(message.command) < 2:
        return await message.reply("Please provide a URL. Example: /add https://google.com")
    
    url = message.command[1]
    if not await db.find_one({"url": url}):
        await db.insert_one({"url": url})
        await message.reply(f"Successfully added: {url}\nI will ping it every 5 minutes.")
    else:
        await message.reply("This URL is already in my database.")

async def continuous_pinger():
    while True:
        all_urls = await db.find().to_list(length=1000)
        async with aiohttp.ClientSession(headers={"User-Agent": "Mozilla/5.0"}) as session:
            tasks = []
            for doc in all_urls:
                tasks.append(session.get(doc["url"], timeout=10))
            if tasks:
                results = await asyncio.gather(*tasks, return_exceptions=True)
                print(f"Pinged {len(results)} URLs.")
        await asyncio.sleep(300)
