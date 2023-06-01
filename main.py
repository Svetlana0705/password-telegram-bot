from aiogram import Bot, Dispatcher, executor
from helper import check_pass
from generator_password import generator_pswd

API_TOKEN = '5997325539:AAH5xRsm3FVoG1Bbkskv6DHiOA0lcjEfilU'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    await message.reply("Введите пароль")


@dp.message_handler(commands=['generate'])
async def generate_password(message):
    new_pswd = ''
    counter=0
    while check_pass(new_pswd)!='Пароль идеален':
        new_pswd=generator_pswd()
        counter+=1
    await message.answer(new_pswd)
    await message.answer(f"Пароль подобран с {counter} попытки")


# @dp.message_handler(commands=['hi'])
# async def hi(message):
#     await message.answer('1234')


# @dp.message_handler()
# async def echo(message):
#     if message.text=='2+2':
#         await message.answer('4')
#     elif message.text=='3+3':
#         await message.answer('6')
#     else:
#         await message.answer(message.text)


@dp.message_handler()
async def validate_password(message):
    result=check_pass(message.text)
    await message.answer(result)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
