import os
import logging

from aiogram import Bot, Dispatcher, executor, types

# from config import TOKEN

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f"Hello, {user_name}!"
    logging.info(f"{user_name=} {user_id=} sent message: {message.text}")
    await message.reply(text)

alp = {'A': 'А', 'Б': 'B', 'B': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'ZH', 'З': 'Z', 
       'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 
       'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 
       'SHCH', 'Ъ': 'IE', 'Ы': 'Y', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA',
       'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 
       'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 
       'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 
       'ъ': 'ie', 'ы': 'y', 'э': 'e', 'ю': 'iu', 'я': 'ia'}

@dp.message_handler()
async def send_echo(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text2 = ''
    text2 = ''.join(alp.get(symbol, symbol) for symbol in message.text)
    logging.info(f"{user_name=} {user_id=} sent message: {message.text}")
    await bot.send_message(user_id, text2)



if __name__ == '__main__':
    executor.start_polling(dp)
