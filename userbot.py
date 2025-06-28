from telethon import TelegramClient, events

api_id = 29592352
api_hash = d24354f0c941dfe03ecaf3ca09e0953c

client = TelegramClient('session_akun', api_id, api_hash)

@client.on(events.NewMessage(pattern='/ping'))
async def ping(event):
    await event.reply('🏓 Pong! Userbot aktif.')

print("🔁 Menjalankan Userbot...")
client.start()
client.run_until_disconnected()
