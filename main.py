from aiogram import types,Bot,Dispatcher,executor
from my_buttons import main_menu
from example import send_qrcode
api = '7724125921:AAHmLaRimw7X1QU2ipqoIZZpA4JrDu5XWuA'
bot = Bot(api)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_hi(sms:types.Message):
    await sms.answer(text='Salem')

@dp.message_handler(text='Qrcode')
async def qrcode_sends(sms:types.Message):
    file = open(file='38.png',mode='rb')
    await sms.answer_photo(
        photo=file,
        caption='bul sizdin qrcode'
    )

@dp.message_handler()
async def save_qrcode(sms:types.Message):
    await send_qrcode(sms.text)
    await sms.answer(text='qrcode saqlandi',
    reply_markup=main_menu)

if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)
