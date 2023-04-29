#TOKEN = "5831659737:AAEc0ezpjR8lkQYor4J2uxn5aui1Q8b5A9c"
import aiogram
#import logging
from googletrans import Translator
from aiogram import types
from aiogram import Dispatcher, executor, Bot
translator = Translator()

bot = aiogram.Bot(token= "5831659737:AAEc0ezpjR8lkQYor4J2uxn5aui1Q8b5A9c")
dp = aiogram.Dispatcher(bot)

@dp.message_handler(commands=("start"))
async def start(message: types.Message):
    await message.answer("Привет. Я умею переводить с русского на английский. Напиши /translate, чтобы узнать много нового.")

@dp.message_handler(commands=("translate"))
async def trans(message: types.Message):
    translated_text = translator.translate(message.text, dest='en').text
    await message.answer(f'{translated_text}')

if __name__ == '__main__':
    executor.start_polling(dp)