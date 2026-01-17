import asyncio
from pyrogram import Client
from config import Config
from web import keep_alive
from plugins.pinger import continuous_pinger

app = Client(
    "UptimeBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)

async def main():
    keep_alive()
    await app.start()
    print("Bot is running...")
    await continuous_pinger()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
