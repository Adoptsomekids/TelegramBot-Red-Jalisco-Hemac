from datetime import datetime
from optparse import Values
from pydoc import text
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, Update
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#from telegram import chat,User

bot = Bot(token='-5Q')
dp = Dispatcher(bot)

button1 = InlineKeyboardButton(text="SALUD", callback_data="SALUD1")
button2 = InlineKeyboardButton(text="EDUCACION", callback_data="EDUCACION1")
button3 = InlineKeyboardButton(text="JUZGADOS", callback_data="JUZGADOS1")
button4 = InlineKeyboardButton(text="CLEAN_UP", callback_data="CLEAN_UP1")
button5 = InlineKeyboardButton(text="RJAL2.0", callback_data="RJAL2.01")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3, button4, button5)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("EDUCACIÓN", " SALUD", "JUZGADOS","CLEAN_UP","RJAL2.0")

"""#InlineKeyboardButton (En texto)
@dp.message_handler(content_types=['text'])
async def random_answer(message: types.Message):
    await message.reply("Te has contactado con mesa de ayuda... \n \n ¿Desde donde te comunicas? \n \n 1) EDUCACION \n 2) SALUD" \n 3) JUZGADOS \n 4) CLEAN UP \n 5) REDJALISCO 2.0, reply_markup=keyboard_inline)
"""
#Time Data
dia = (datetime.today().weekday())

date = datetime.now()
print(date)

#KeyboardButton (Barra)
@dp.message_handler(commands=['start', 'help' , 'INICIO', 'Inicio', 'inicio', 'inició', 'INICIÓ'])
async def welcome(message: types.Message):
    await message.reply("¡Bienvenido a la toma de turno de Mesa de Ayuda!... \n \n ¿En qué dependencia vas a realizar tu instalación? \n \n 1) EDUCACIÓN \n 2) SALUD\n 3) JUZGADOS \n 4) CLEAN UP \n 5) REDJALISCO 2.0", reply_markup=keyboard1)

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
    
    if message.text == 'EDUCACION' or message.text == 'Educacion'  or message.text == 'educacion' or message.text == 'EDUCACIÓN' or message.text == 'Educación' or message.text == 'educación'or message.text == '1':
        await message.reply("Escribe el ID de la Escuela donde te encuentras:")

    elif message.text == 'SALUD' or message.text == 'Salud'  or message.text == 'salud' or message.text == '2':
        await message.reply("Escribe el ID del Centro de salud donde te encuentras:")

    elif message.text == 'JUZGADO' or message.text == 'Juzgado'  or message.text == 'Juzgado' or message.text == '3':
        await message.reply("Escribe el ID del Juzgado donde te encuentras:")

    elif message.text == 'CLEAN_UP' or message.text == 'Clean Up'  or message.text == 'Clean Up' or message.text == '4':
        await message.reply("Escribe el ID del Clean Up donde te encuentras:")

    elif message.text == 'RJAL 2.0' or message.text == 'RedJalisco 2.0'  or message.text == 'RedJalisco 2.0' or message.text == '5':
        await message.reply("Escribe el ID del sitio donde te encuentras:")


    else:
        if len(message.text) <= 6 or message.text == "buenos dias" or message.text == "BUENOS DIAS" or message.text == "Buenos dias" or message.text == "Buenos Dias" or message.text == "buenos días" or message.text == "BUENOS DÍAS" or message.text == "Buenos días" or message.text == "Buenos Días"  or message.text == "BUENAS TARDES" or message.text == "Buenas Tardes" or message.text == "Buenas tardes" or message.text == "buenas tardes"  or message.text == "BUENAS NOCHES" or message.text == "Buenas Noches" or message.text == "Buenas noches" or message.text == "buenas noches" or message.text == "Hola buenas tardes para dar inicio" or message.text == "Para dar inicio" or message.text == "Holaa Buenos días para dar inicio" or message.text == "Hola buenos dias para dar inicio" or message.text == "Hola buenos días para dar inicio" or message.text == "Buen dia" or message.text == "Buena tarde" or message.text == "Buenoz dias" or message.text == "Hola buen dia" or message.text == "Dar inicio":
            await message.reply("\t ¡Bienvenido a la toma de turno de Mesa de Ayuda!... \n\n Nuestro horario de atencion es de 8 a 7:30 \n\nEscribe o presiona ---> /Inicio <--- para asignarte un agente")
        else:
	    #await message.reply("¡¡IMPORTANTE!!")
	
            await message.reply(f"El ID Ingresado es: {message.text}")
            await message.reply("¡¡IMPORTANTE!!\n\n ANTES DE INICIAR ACTIVIDADES ASEGURARSE QUE ENCARGADO QUE FIRMARA, CUENTA CON CREDENCIAL LEGIBLE, DE IGUAL MANERA LA FIRMA DE LA PERSONA QUE FIRMA DEBERA SER IGUAL A LAS FIRMAS DEL PROTOCOLO...")

            id1 = {message.text}
            await message.reply("Da click en el link para hablar con el Agente de Mesa de Ayuda... \n \n ")

            if (dia == 0):
                for x in operator_list:
                    monday.append(x)
                #print(monday)
                n = monday.pop(0)    
                print(f'TURNO: {n}')
                operador = n
            
            elif (dia == 1):
                for x in operator_list:
                    tuesday.append(x)
                #print(tuesday)
                n = tuesday.pop(0)    
                print(f'TURNO: {n}')
                operador = n

            elif dia == 2:
                for x in operator_list:
                    wednesday.append(x)
                #print(wednesday)
                n = wednesday.pop(0)    
                print(f'TURNO: {n}')
                operador = n
            
            elif dia == 3:
                for x in operator_list:
                    thursday.append(x)
                #print(thursday)
                n = thursday.pop(0)    
                print(f'TURNO: {n}')
                operador = n
            
            elif dia == 4:
                for x in operator_list:
                    friday.append(x)
                #print(friday)
                n = friday.pop(0)    
                print(f'TURNO: {n}')
                operador = n

            elif dia == 5:
                for x in operator_list2:
                    saturday.append(x)
                #print(saturday)
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
            op6 = "Ulises "
            op7 = "Brian "
            op8 = "Yoni "
            op9 = "Daniel "
            op10 = "Ale "
            op11 = "Ernesto "
            
            #https://t.me/e
            supervisor =[1910845464]# 1287182448
            
            id_op2 = [1287182448, 5713575385, 2095480041, 5959575070, 5796936396]#Supervisor / Nayeli 
            id_op3 = [1287182448, 5713575385, 2095480041, 5959575070, 5534493638]#Supervisor / Grecia 
            id_op4 = [1287182448, 5713575385, 2095480041, 5959575070, 5725929929]#Supervisor / Blanca 
            id_op5 = [1287182448, 5713575385, 2095480041, 5959575070, 5735119439]#Supervisor / Juan 
            id_op6 = [1287182448, 5713575385, 2095480041, 5959575070, 1317088058]#Supervisor / Ulises 
            id_op7 = [1287182448, 5713575385, 2095480041, 5959575070, 5770862254]#Supervisor / Brian 
            id_op8 = [1287182448, 5713575385, 2095480041, 5959575070, 5695339731]#Supervisor / Yoni 
            id_op9 = [1287182448, 5713575385, 2095480041, 5959575070, 5984956553]#Supervisor / Daniel 
            id_op10 =[1287182448, 5713575385, 2095480041, 5959575070, 5934371748]#Supervisor / Ale 
            id_op11 =[1287182448, 5713575385, 2095480041, 5959575070, 5776039911]#Supervisor / Santos


            All_operators = [1910845464, 1287182448, 5713575385, 2095480041, 5959575070, 5796936396, 5534493638, 5725929929, 5735119439, 1317088058, 5770862254, 5695339731,5984956553,5934371748,5776039911]

            username = message.from_user.username
            #phone = message.from_user.id
            name = message.from_user.first_name
            last_n = message.from_user.last_name

            #Nayeli     
            if (operador == 'https://wa.me/qr/'):
                date = datetime.now()
                print(date)
                await message.reply("Operador asignado: NAYELI ")
                for chat in All_operators:
                    await bot.send_message(chat_id=chat,text= "Ingeniero: %s %s \n Nombre de usuario: @%s \n ID = %s \n Asignado a operador(a) de mesa de ayuda: %s \n Fecha: %s \n Hora: %s"
                    %(name, last_n, username , id1, op2, str(date.date()), str(date.time())))
            #Grecia Corona
            elif (operador == 'https://wa.me/qr/'):
                date = datetime.now()
                print(date)
                await message.reply("Operador asignado: GRECIA ")
                for chat in All_operators:
                    await bot.send_message(chat_id=chat,text= "Ingeniero: %s %s \n Nombre de usuario: @%s \n ID = %s \n Asignado a operador(a) de mesa de ayuda: %s \n Fecha: %s \n Hora: %s"
                    %(name, last_n, username , id1, op3, str(date.date()), str(date.time())))              
            #Blanca Benitez
            elif (operador == 'https://wa.me/qr/'):
                date = datetime.now()
                print(date)
                await message.reply("Operador asignado: BLANCA ")
                for chat in All_operators:
                    await bot.send_message(chat_id=chat,text= "Ingeniero: %s %s \n Nombre de usuario: @%s \n ID = %s \n Asignado a operador(a) de mesa de ayuda: %s \n Fecha: %s \n Hora: %s"
                    %(name, last_n, username , id1, op4, str(date.date()), str(date.time())))
            #Juan Luis
            elif (operador == 'https://wa.me/qr/'):
                date = datetime.now()
                print(date)
                await message.reply("Operador asignado: JUAN ")
                for chat in All_operators:
                    await bot.send_message(chat_id=chat,text= "Ingeniero: %s %s \n Nombre de usuario: @%s \n ID = %s \n Asignado a operador(a) de mesa de ayuda: %s \n Fecha: %s \n Hora: %s"
                    %(name, last_n, username , id1, op5, str(date.date()), str(date.time())))
            #Ulises
            elif (operador == 'https://wa.me/qr/'):
                date = datetime.now()
                print(date)
                await message.reply("Operador asignado: ULISES ")
                for chat in All_operators:
                    await bot.send_message(chat_id=chat,text= "Ingeniero: %s %s \n Nombre de usuario: @%s \n ID = %s \n Asignado a operador(a) de mesa de ayuda: %s \n Fecha: %s \n Hora: %s"
                    %(name, last_n, username , id1, op6, str(date.date()), str(date.time())))  
            #Brian Barajas
            elif (operador == 'https://wa.me/qr/'):
                date = datetime.now()
                print(date)
                await message.reply("Operador asignado: BRIAN ")
                for chat in All_operators:
                    await bot.send_message(chat_id=chat,text= "Ingeniero: %s %s \n Nombre de usuario: @%s \n ID = %s \n Asignado a operador(a) de mesa de ayuda: %s \n Fecha: %s \n Hora: %s"
                    %(name, last_n, username , id1, op7, str(date.date()), str(date.time())))
            #Yoni Deara
            elif (operador == 'https://wa.me/qr/'):
                date = datetime.now()
                print(date)
                await message.reply("Operador asignado: YONI ")
                for chat in All_operators:
                    await bot.send_message(chat_id=chat,text= "Ingeniero: %s %s \n Nombre de usuario: @%s \n ID = %s \n Asignado a operador(a) de mesa de ayuda: %s \n Fecha: %s \n Hora: %s"
                    %(name, last_n, username , id1, op8, str(date.date()), str(date.time())))
            #Daniel     
            elif (operador == 'https://wa.me/qr/'):
                date = datetime.now()
                print(date)
                await message.reply("Operador asignado: DANIEL")
                for chat in All_operators:
                    await bot.send_message(chat_id=chat,text= "Ingeniero: %s %s \n Nombre de usuario: @%s \n ID = %s \n Asignado a operador(a) de mesa de ayuda: %s \n Fecha: %s \n Hora: %s"
                    %(name, last_n, username , id1, op9, str(date.date()), str(date.time())))
            #Ale
            elif (operador == 'https://wa.me/qr/'):
                date = datetime.now()
                print(date)
                await message.reply("Operador asignado: ALE ")
                for chat in All_operators:
                    await bot.send_message(chat_id=chat,text= "Ingeniero: %s %s \n Nombre de usuario: @%s \n ID = %s \n Asignado a operador(a) de mesa de ayuda: %s \n Fecha: %s \n Hora: %s"
                    %(name, last_n, username , id1, op10, str(date.date()), str(date.time())))
            #Ernesto
            elif (operador == 'https://wa.me/qr/'):
                date = datetime.now()
                print(date)
                await message.reply("Operador asignado: ERNESTO ")
                for chat in All_operators:
                    await bot.send_message(chat_id=chat,text= "Ingeniero: %s %s \n Nombre de usuario: @%s \n ID = %s \n Asignado a operador(a) de mesa de ayuda: %s \n Fecha: %s \n Hora: %s"
                    %(name, last_n, username , id1, op11, str(date.date()), str(date.time())))         
            else:
                print ("Other Operator")




operator_list = [
                'https://wa.me/qr/',
                
                ]

monday = [
         'https://wa.me/qr/',
         
         ]

tuesday = [
          'https://wa.me/qr/',
          
          ]

wednesday = [
            'https://wa.me/qr/',
            
            ]

thursday = [
            'https://wa.me/qr/',
            
            ]

friday = [
         'https://wa.me/qr/',
         
         ]





#Modificar para guardia (SABADO)
saturday = ['https://wa.me/qr/' ]
operator_list2 = ['https://wa.me/qr/' ]


#No tocar (Diccionario sin uso)
valuesd = {
        1: 'https://t.me/',
        2: 'https://t.me/',
        3: 'https://t.me/',
        4: 'https://t.me/',
        5: 'https://t.me/',
        6: 'Ulises'
    }

executor.start_polling(dp)
