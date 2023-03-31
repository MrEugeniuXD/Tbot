from aiogram import Bot, Dispatcher, executor, types
import os
import key
import random

bot =Bot(key.API_KEY)               #key.API_KEY
dp = Dispatcher(bot)

asd= ("Hi, do you want some anime recomandations?","Bună, vrei să-ți sugestionez un anime?","Hello, mate, want to watch some anime?")
anime = ("Naruto", "One piece", "Vinland Saga", "Demon Slayer: Kimetsu no Yaiba", "Death Note")
@dp.message_handler(commands = ['hello'])
async def hello(message:types.message):
    await message.answer(text=random.choice(asd))     #


@dp.message_handler(commands = ['help'])
async def help(message:types.message):
    await message.answer(text="type in /hello /help or /anime")

@dp.message_handler(commands = ['start'])
async def start(message:types.message):
    await message.answer(text="type in /hello /help or /anime, also if you type something random I will make it uppercase for you x)")
    await message.delete()

@dp.message_handler(commands = ['anime'])
async def anime(message:types.message):
    await message.answer(text=random.choice(anime))

@dp.message_handler(text = ['anime'])
async def animetext(message:types.message):
    await message.answer(text=random.choice(anime))

@dp.message_handler()
async def upper(message:types.message):
    await message.answer(text=message.text.upper())



if __name__ == '__main__':
    executor.start_polling(dp)
