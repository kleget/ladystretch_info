import os

from importt import *
from button import *



@dp.message_handler(commands="start")
async def start_command(message: types.Message):
    global chat_id
    chat_id= message.chat.id
    await message.answer("Hello!", reply_markup=greet_kb)
    await process_start_command()


@dp.message_handler(commands=['reset', 'обновить'])
async def start_command(message: types.Message):
    global chat_id
    chat_id= message.chat.id
    await process_start_command()

@dp.message_handler()
async def process_start_command():
    main_parse()
    f = open('text1.txt', 'r')
    f = f.read()
    s = f.replace("['", "")
    s = s.replace("']", '')
    s = s.replace("', '", '$')
    s = s.split('$')

    keyboard = InlineKeyboardMarkup(row_width=1) #кол-во кнопок в строке
    button_list = [types.InlineKeyboardButton(text=x,  callback_data=x) for x in s]
    keyboard.add(*button_list)#добавляем кнопки в клавиатуру
    await bot.send_message(text='Select', chat_id=chat_id, reply_markup=keyboard)
    os.system(['clear', 'cls'][os.name == 'nt'])
    print('ok')

@dp.callback_query_handler(lambda c: c.data != ' ')
async def to_query(call: types.callback_query):
    f = open('text1.txt', 'r')
    f = f.read()
    s = f.replace("['", "")
    s = s.replace("']", '')
    s = s.replace("', '", '$')
    s = s.split('$')
    word = call.data
    index = s.index(word)
    if index == 0:
        i_1 = 0
        i_2 = 1
    else:
        i_1 = index * 2
        i_2 = index * 2 + 1
    await process_start_command_2(message=word, a = i_1, b = i_2, chat_id = call.from_user.id)

    await bot.answer_callback_query(call.id)

@dp.message_handler()
async def process_start_command_2(message, a, b, chat_id):
    main_2_parse(a, b)
    j = open('text2_2.txt', 'r')  # ссылка
    j = j.read()
    if j == '[]':
        await bot.send_message(text='Пусто', chat_id=chat_id)
        os.system(['clear', 'cls'][os.name == 'nt'])
        print('ok')
    else:
        z = j.replace("['", "")
        z = z.replace("']", '')
        z = z.replace("', '", '$')
        z = z.split('$')
        f = open('text2.txt', 'r')#левая колонка
        f = f.read()
        s = f.replace("['", "")
        s = s.replace("']", '')
        s = s.replace("', '", '$')
        s = s.split('$')
        keyboard = InlineKeyboardMarkup(row_width=1)  # кол-во кнопок в строке
        button_list = [types.InlineKeyboardButton(text=s[x], url=z[x], callback_data=s[x]) for x in range(len(s))]
        keyboard.add(*button_list)  # добавляем кнопки в клавиатуру
        await bot.send_message(text=message, chat_id=chat_id, reply_markup=keyboard)  # выводим клавиатуру

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
