from datetime import datetime
from optparse import Values
from pydoc import text
import random
from re import S
from time import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, Update
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegram import chat,User

bot = Bot(token='4h8...')
dp = Dispatcher(bot)

button1 = InlineKeyboardButton(text="SALUD", callback_data="SALUD1")
button2 = InlineKeyboardButton(text="EDUCACION", callback_data="EDUCACION1")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("EDUCACION", " SALUD")

"""#InlineKeyboardButton (En texto)
@dp.message_handler(content_types=['text'])
async def random_answer(message: types.Message):
    await message.reply("Te has contactado con mesa de ayuda... \n \n ¿Desde donde te comunicas? \n \n 1) EDUCACION \n 2) SALUD", reply_markup=keyboard_inline)
"""
#Time Data
dia = (datetime.today().weekday())

date = datetime.now()
print(date)

break_1 = "2"#str([1,3])
break_2 = "5"#str([1,5])
end_break_1 = "16"

#KeyboardButton (Barra)
@dp.message_handler(commands=['start', 'help' , 'INICIO', 'Inicio', 'inicio'])
async def welcome(message: types.Message):
    await message.reply("Bienvenido al toma turno de Mesa de Ayuda... \n \n ¿En que dependencia vas a realizar tu instalación? \n \n 1) EDUCACION \n 2) SALUD", reply_markup=keyboard1)

"""#Validacion (Buttons)
@dp.callback_query_handler(text=["SALUD1", "EDUCACION1"])
async def random_value(call: types.CallbackQuery):
    argumento = types.Message
    if call.data == 'SALUD1':
        argumento.text = 'SALUD' 
        await kb_answer(argumento)
    elif call.data == 'EDUCACION1':
        argumento.text = 'EDUCACION' 
        await kb_answer(argumento)
    else:
        await call.message.answer("\t ¡Bienvenido!... \n\n Escriba o presione ---> /Inicio <--- para poder comenzar")
"""

#Validacion (Mensaje)
@dp.message_handler()
async def kb_answer(message: types.Message):
    
    if message.text == 'EDUCACION' or message.text == 'EDUCACION'  or message.text == 'EDUCACION' or message.text == '1':
        await message.reply("Escribe el ID de la Escuela donde te encuentras:")

    elif message.text == 'SALUD' or message.text == 'SALUD'  or message.text == 'SALUD' or message.text == '2':
        await message.reply("Escribe el ID del Centro de salud donde te encuentras:")

    else:
        if len(message.text) <= 6:
            await message.reply("\t ¡Bienvenido al toma turno de Mesa de ayuda!... \n\n Escribe o presiona ---> /Inicio <--- para asignarte un agente")
        else:
            await message.reply(f"El ID Ingresado es: {message.text}")
            if message.text == 'no':
                await message.reply("\t ¡Bienvenido al toma turno de Mesa de ayuda!... \n\n Escribe o presiona ---> /Inicio <--- para asignarte un agente")
                
            id1 = {message.text}
            await message.reply("Da click en el link para hablar con el Agente de Mesa de Ayuda... \n \n ")
            
            if (dia == 0):

                for x in operator_list:
                    monday.append(x)
                print(monday)
                n = monday.pop(0)    
                print(f'TURNO: {n}')
                operador = n
            
            elif (dia == 1):
                date = datetime.now()
                time = str(date.time())
                i = 5
                j = 6
                if time[j] == break_1 :#and time[j] == break_2:
                    for x in save:
                        tuesday.append(x)
                        print(friday)
                        n = tuesday.pop(0)    
                        print(f'TURNO: {n}')
                        operador = n
                else:
                    for x in operator_list:
                        tuesday.append(x)
                    print(tuesday)
                    n = tuesday.pop(0)    
                    print(f'TURNO: {n}')
                    operador = n

            elif dia == 2:
                for x in operator_list:
                    wednesday.append(x)
                print(wednesday)
                n = wednesday.pop(0)    
                print(f'TURNO: {n}')
                operador = n
            
            elif dia == 3:
                for x in operator_list:
                    thursday.append(x)
                print(thursday)
                n = thursday.pop(0)    
                print(f'TURNO: {n}')
                operador = n
            
            elif dia == 4:    
                for x in operator_list:
                    friday.append(x)
                print(friday)
                n = friday.pop(0)    
                print(f'TURNO: {n}')
                operador = n

            elif dia == 5:
                for x in operator_list2:
                    saturday.append(x)
                print(saturday)
                n = saturday.pop(0)    
                print(f'TURNO: {n}')
                operador = n

            else:
                print("No hay operaciones disponibles")
                            
            await bot.send_message(message.chat.id, operador)
            op2 = "Nayeli "
            op3 = "Grecia "
            op4 = "Blanca "
            op5 = "Juan "
            op6 = "Ulises"
            
            #https://t.me/e
            supervisor =[1910845464]# 1287182448
            
            id_op2 = [1287182448, 5713575385, 5796936396]#Supervisor / Nayeli 
            id_op3 = [1287182448, 5713575385, 5534493638]#Supervisor / Grecia 
            id_op4 = [1287182448, 5713575385, 5725929929]#Supervisor / Blanca 
            id_op5 = [1287182448, 5713575385, 5735119439]#Supervisor / Juan 
            id_op6 = [1287182448, 5713575385, 1317088058]#Supervisor / Ulises

            All_operators = [1287182448, 5713575385, 5796936396, 5534493638, 5725929929, 5735119439, 1317088058]

            username = message.from_user.username
            #phone = message.from_user.id
            name = message.from_user.first_name
            last_n = message.from_user.last_name

            #Nayeli     
            if (operador == 'https://wa.me/qr/'):
                date = datetime.now()
                print(date)
                await message.reply("Operador asignado: NAYELI ")
                for chat in supervisor:
                    await bot.send_message(chat_id=chat,text= "Ingeniero: %s %s \n Nombre de usuario: @%s \n ID = %s \n Asignado a operador(a) de mesa de ayuda: %s \n Fecha: %s \n Hora: %s"
                    %(name, last_n, username , id1, op2, str(date.date()), str(date.time())))
            #Grecia Corona
            elif (operador == 'https://wa.me/qr/'):
                date = datetime.now()
                print(date)
                await message.reply("Operador asignado: GRECIA ")
                for chat in supervisor:
                    await bot.send_message(chat_id=chat,text= "Ingeniero: %s %s \n Nombre de usuario: @%s \n ID = %s \n Asignado a operador(a) de mesa de ayuda: %s \n Fecha: %s \n Hora: %s"
                    %(name, last_n, username , id1, op3, str(date.date()), str(date.time())))              
            #Blanca Benitez
            elif (operador == 'https://wa.me/qr/'):
                date = datetime.now()
                print(date)
                await message.reply("Operador asignado: BLANCA ")
                for chat in supervisor:
                    await bot.send_message(chat_id=chat,text= "Ingeniero: %s %s \n Nombre de usuario: @%s \n ID = %s \n Asignado a operador(a) de mesa de ayuda: %s \n Fecha: %s \n Hora: %s"
                    %(name, last_n, username , id1, op4, str(date.date()), str(date.time())))
            #Juan Luis
            elif (operador == 'https://wa.me/qr/'):
                date = datetime.now()
                print(date)
                await message.reply("Operador asignado: JUAN ")
                for chat in supervisor:
                    await bot.send_message(chat_id=chat,text= "Ingeniero: %s %s \n Nombre de usuario: @%s \n ID = %s \n Asignado a operador(a) de mesa de ayuda: %s \n Fecha: %s \n Hora: %s"
                    %(name, last_n, username , id1, op5, str(date.date()), str(date.time())))
            #Ulises
            elif (operador == 'https://wa.me/qr/'):
                date = datetime.now()
                print(date)
                await message.reply("Operador asignado: ULISES ")
                for chat in supervisor:
                    await bot.send_message(chat_id=chat,text= "Ingeniero: %s %s \n Nombre de usuario: @%s \n ID = %s \n Asignado a operador(a) de mesa de ayuda: %s \n Fecha: %s \n Hora: %s"
                    %(name, last_n, username , id1, op6, str(date.date()), str(date.time())))           
            else:
                print ("Other Operator")


operator_list = ['https://wa.me/qr/', 'https://wa.me/qr/', 'https://wa.me/qr/', 'https://wa.me/qr/', 'https://wa.me/qr/']


monday = ['https://wa.me/qr/', 'https://wa.me/qr/' ,'https://wa.me/qr/', 'https://wa.me/qr/', 'https://wa.me/qr/']

tuesday = ['https://wa.me/qr/', 'https://wa.me/qr/','https://wa.me/qr/', 'https://wa.me/qr/', 'https://wa.me/qr/']

wednesday = ['https://wa.me/qr/', 'https://wa.me/qr/' , 'https://wa.me/qr', 'https://wa.me/qr/', 'https://wa.me/qr/']

thursday = ['https://wa.me/qr/', 'https://wa.me/qr/', 'https://wa.me/qr/', 'https://wa.me/qr/', 'https://wa.me/qr/']

friday = ['https://wa.me/qr/', 'https://wa.me/qr/', 'https://wa.me/qr/', 'https://wa.me/qr/', 'https://wa.me/qr/']


#Modificar para guardia (SABADOS) (OPERADORES DISPONIBLES)
saturday = ['https://wa.me/qr/','https://wa.me/qr/' ]
operator_list2 = ['https://wa.me/qr/','https://wa.me/qr/' ]

#Hora de comida (2 a 3) (OPERADORES DISPONIBLES)
save = ['https://wa.me/qr/', 'https://wa.me/qr/']

valuesd = {
        1: 'https://t.me/',
        2: 'https://t.me/',
        3: 'https://t.me/',
        4: 'https://t.me/',
        5: 'https://t.me/',
        6: 'Ulises'
    }

executor.start_polling(dp)