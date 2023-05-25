from aiogram import Bot, Dispatcher, executor
from helper import check_pass

API_TOKEN = '5997325539:AAH5xRsm3FVoG1Bbkskv6DHiOA0lcjEfilU'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    await message.reply("Введите пароль")


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
