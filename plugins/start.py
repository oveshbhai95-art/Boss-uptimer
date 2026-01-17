from pyrogram import Client, filters
from config import Config

@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
    user = message.from_user
    # Logging in small caps as per instructions
    log_msg = f"ᴜsᴇʀ {user.first_name} [ `{user.id}` ] sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ."
    await client.send_message(Config.LOG_CHANNEL, log_msg)
    
    await message.reply_text(
        f"Hello {user.mention},\n\nI am a Powerful URL Uptime Bot. "
        "I can keep your web apps alive 24/7.\n\n"
        "Use /add [url] to start."
    )
