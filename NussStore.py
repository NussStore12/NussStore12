from telethon import TelegramClient, events

# Masukkan API ID dan API Hash dari Telegram
API_ID = 21802248  # Ganti dengan API ID Anda
API_HASH = "17ba6f888e41249ae5628f44c9313ea9"  # Ganti dengan API Hash Anda
PHONE_NUMBER = "+6283807568165"  # Ganti dengan nomor Telegram Anda

# Membuat client
client = TelegramClient("bot_session", API_ID, API_HASH)

# Event handler untuk perintah /start
@client.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.reply("Ciao, sono il bel robot assistente di Nuss Store.")

# Menjalankan bot
async def main():
    await client.start(PHONE_NUMBER)  # Login dengan nomor asli
    print("Bot Telegram telah berjalan...")
    await client.run_until_disconnected()

# Memulai event loop
with client:
    client.loop.run_until_complete(main())
