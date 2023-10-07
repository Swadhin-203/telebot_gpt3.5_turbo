from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
import openai
import sys

class Reference:
    """
    A class to store preiviously respone from the Api
    """
    def __init__(self)->None:
        self.response=""

load_dotenv()
openai.api_key=os.getenv("OpenAI_API_KEY")  
reference=Reference() 
TOKEN=os.getenv('TOKEN')

#model name
MODEL_NAME="gpt-3.5-turbo"

bot= Bot(token=TOKEN)
dp=Dispatcher(bot)

def clear_past():
    """ 
    This function is used to clear the previous conversation
    """
    reference.response=""

@dp.message_handler(commands=['start'])
async def welcome(message:types.Message):
    await message.reply("Hi \n This is Swadhin's Jojo Bot. How can I assist you?😁😁")

@dp.message_handler(commands=['clear'])
async def clear(message: types.Message):
    clear_past()
    await message.reply("I've sucessfully cleared the past conversation and context")

@dp.message_handler(commands=['help'])
async def helper(message:types.Message):
    help_command="""
    Hi, This is Swadhin's jojo Bot ! Please Follow these commands-
    /start- To start the Conversation
    /clear- To clear the conversation
    /help- To get this help menu
    I hope this helps :)
    """
    await message.reply(help_command)

@dp.message_handler()
async def chatgpt(message: types.Message):
    print(f">>> USER: \n\t{message.text}")

    response=openai.ChatCompletion.create(

        model =MODEL_NAME,
        messages= [
            {"role": "assistant", "content":reference.response},
            {"role":"user","content":message.text} #our Query
        ]
    )

    reference.response=response['choices'][0]['message']['content']
    print(f">>>chatGPT: \n\t{reference.response}")
    await bot.send_message(chat_id=message.chat.id, text=reference.response)

if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)