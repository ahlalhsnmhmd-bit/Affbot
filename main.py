import asyncio
from telegram import Bot

TELEGRAM_TOKEN= "9280313528:AAGKM4PthnlqvA0hjgMTz3Z8vjMvwe3sfmw"

CHANNEL_ID = "@mhn123mhn"

DEALS_DATABASE = [
{
"title": "🔥 خصم خاص على منتجات التقنية!",
"description": "استفد من تخفيض مميز اليوم.",
"link": "https://your-affiliate-link.com",
"image": "https://picsum.photos/600/400"
}
]

async def send_affiliate_post():
bot = Bot(token=TELEGRAM_TOKEN)
for deal in DEALS_DATABASE:
message = f"{deal['title']}\n\n{deal['description']}\n\n🔗 اضغط هنا"
try:
await bot.send_photo(chat_id=CHANNEL_ID, photo=deal['image'], caption=message, parse_mode="Markdown")
print("✅ تم النشر")
except Exception as e:
print(f"❌ خطأ: {e}")
await asyncio.sleep(10800)

if name == "main":
asyncio.run(send_affiliate_post())

