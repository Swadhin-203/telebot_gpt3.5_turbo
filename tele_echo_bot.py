import logging
from aiogram import Bot, Dispatcher,executor ,types
from dotenv import load_dotenv
import os
load_dotenv()
API_TOKEN=os.getenv("TOKEN")
print(API_TOKEN)
logging.basicConfig(level=logging.INFO)

bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['hello','help'])
async def command_start_handler(message:types.message):
    """
    This handler receives messages with '/start','help'
    """
    await message.reply("🌟 Welcome to our little corner of joy,  Dugunu😚😚😚! 🌈 Your presence just made this place brighter and sweeter. 🌸 Get ready for a daily dose of love, laughter, and special moments. 💖 Thank you for being the sunshine in my digital world! ☀️ Let the adventures begin! 🚀✨ please press '/dahu'")

@dp.message_handler(commands=['dahu','help'])
async def command_start_handler(message:types.message):
    """
    This handler receives messages with '/start','help'
    """
    await message.reply("I Love you dudunu😚😚😚 , hihi😁😁 , please type '/kalia'")

@dp.message_handler(commands=['kalia','help'])
async def command_start_handler(message:types.message):
    """
    This handler receives messages with '/start','help'
    """
    await message.reply("🎉 Happy Birthday, my love! 🎂✨ On this special day, I wish you all the joy, laughter, and incredible moments that life has to offer. May this year be filled with dreams realized and adventures embraced. You deserve nothing but the absolute best, and I'm here to make sure every moment is as wonderful as you are. Cheers to another year of love and shared memories! 🥳💖")

@dp.message_handler(commands=['dahu','help'])
async def echo(message:types.Message):
    """
    This handler receives messages with '/start','help'
    """
    await message.answer(message.text)

if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)