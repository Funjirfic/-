from aiogram import Bot, types, executor, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from fun_predprof import *
from aiogram.types import InputFile

bot = Bot(token='6464623550:AAHFIp_P-BSgK8S4v-vY8ObooYusMm1d3Dk')
dp = Dispatcher(bot)

ikb1 = InlineKeyboardMarkup()
i1 = InlineKeyboardButton(text='Курс валют ЦБ РФ',
                          callback_data='parse')
i2 = InlineKeyboardButton(text='Прогноз курса на 2024',
                          callback_data='prognoz')
ikb1.add(i1, i2)

ikb2 = InlineKeyboardMarkup()
ii1 = InlineKeyboardButton(text='USD🇺🇸',
                           callback_data='USDp')
ii2 = InlineKeyboardButton(text='EUR🇪🇺',
                           callback_data='EURp')
ii3 = InlineKeyboardButton(text='CNY🇨🇳',
                           callback_data='CNYp')
ii4 = InlineKeyboardButton(text='GBP🇬🇧',
                           callback_data='GBPp')

ikb2.add(ii1, ii2, ii3, ii4)

ikb3 = InlineKeyboardMarkup()
iii1 = InlineKeyboardButton(text='USD🇺🇸',
                            callback_data='USDpr')
iii2 = InlineKeyboardButton(text='EUR🇪🇺',
                            callback_data='EURpr')
iii3 = InlineKeyboardButton(text='CNY🇨🇳',
                            callback_data='CNYpr')
iii4 = InlineKeyboardButton(text='GBP🇬🇧',
                            callback_data='GBPpr')

ikb3.add(iii1, iii2, iii3, iii4)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer('Привет, выбери что тебе нужно',
                         reply_markup=ikb1)


@dp.callback_query_handler(text='parse')
async def process_callback_info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer('Выбери нужную валюту:',
                                        reply_markup=ikb2)


@dp.callback_query_handler(text='USDp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    await callback_query.message.answer(f'Доллар США\nЕдиниц: 1\nКурс ЦБ РФ: {USD()}',
                                        reply_markup=ikb1)
    await message_to_delete.delete()


@dp.callback_query_handler(text='EURp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    await callback_query.message.answer(f'Евро\nЕдиниц: 1\nКурс ЦБ РФ: {EUR()}',
                                        reply_markup=ikb1)
    await message_to_delete.delete()


@dp.callback_query_handler(text='CNYp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    await callback_query.message.answer(f'Китайский юань\nЕдиниц: 1\nКурс ЦБ РФ: {CNY()}',
                                        reply_markup=ikb1)
    await message_to_delete.delete()


@dp.callback_query_handler(text='GBPp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    await callback_query.message.answer(f'Фунт стерлингов Соединенного королевства\nЕдиниц: 1\nКурс ЦБ РФ: {GBP()}',
                                        reply_markup=ikb1)
    await message_to_delete.delete()


@dp.callback_query_handler(text='prognoz')
async def process_callback_info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer('Выбери нужную валюту:',
                                        reply_markup=ikb3)


@dp.callback_query_handler(text='USDpr')
async def process_callback_info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    photo = InputFile('USD.PNG')
    await callback_query.message.answer('Прогноз курса Доллара:')
    await callback_query.message.answer_photo(photo,
                                              reply_markup=ikb1)


@dp.callback_query_handler(text='EURpr')
async def process_callback_info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    photo = InputFile('EUR.PNG')
    await callback_query.message.answer('Прогноз курса Евро:')
    await callback_query.message.answer_photo(photo,
                                              reply_markup=ikb1)


@dp.callback_query_handler(text='CNYpr')
async def process_callback_info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    photo = InputFile('CNY.PNG')
    await callback_query.message.answer('Прогноз курса Юаня:')
    await callback_query.message.answer_photo(photo,
                                              reply_markup=ikb1)


@dp.callback_query_handler(text='GBPpr')
async def process_callback_info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    photo = InputFile('GBP.PNG')
    await callback_query.message.answer('Прогноз курса Фунта:')
    await callback_query.message.answer_photo(photo,
                                              reply_markup=ikb1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
