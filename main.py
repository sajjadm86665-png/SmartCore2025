import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

# توکن ربات تلگرام (اینجا مستقیم گذاشتم)
TOKEN = "8554754667:AAHJLzIkN9I-Wf6I3qJqJMH9cge44PQhZDk"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# هندلر برای دستور /start
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("سلام سجاد 👋 رباتت آنلاین شد!")

# هندلر برای هر پیام متنی
@dp.message()
async def echo_handler(message: Message):
    await message.answer(f"تو گفتی: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
