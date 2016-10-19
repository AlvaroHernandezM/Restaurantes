import pln
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import os
import fuzzyLogic as fl
import adminDB

def listener(bot, update):
    id = update.message.chat_id
    message = (update.message.text).lower()
    #print('ID: ' + str(id) + ' MENSAJE: ' + message)
    #if message.lower() 
    option = identifiedOptionConversation(id)
    writeConversation(str(id),"user: "+message)
    if option == 0: #la respuesta hecha por el bot fue la edad
        filterAge(message, bot, id)
    elif option == 1:
        filterProfesion(message,bot,id)
    elif option == 2:
        filterHourFood(message,bot,id)
    elif option == 3:
        filterTypeFood(message,bot,id)
    elif option == 4:
        filterCashOnly(message,bot,id)
    elif option == 5:
        filterDisability(message,bot,id)
    elif option == 6:
        filterParking(message,bot,id)
    elif option == 7:
        filterSmoking(message,bot,id)
    elif option == 8:
        filterAlcohol(message,bot,id)
    elif option == 9:
        filterWithFriends(message,bot,id)
    else:
        bot.sendMessage(chat_id=id, text="No entender")
def filterWithFriends(message,bot,id):
    resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
    print (resultPln)
    bot.sendMessage(chat_id=id, text="Ha terminado la conversacion, te recomiendo")
    writeConversation(str(id),"bot: "+message.lower())
def filterAlcohol(message,bot,id):
    resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
    print (resultPln)
    message="¿Vas con amigos?"
    bot.sendMessage(chat_id=id, text="Y como última pregunta:")
    bot.sendMessage(chat_id=id, text=message)
    writeConversation(str(id),"bot: "+message.lower())
def filterSmoking(message,bot,id):
    resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
    print (resultPln)
    message="¿Tienes pensado tomar alcohol hoy?"
    bot.sendMessage(chat_id=id, text=message)
    writeConversation(str(id),"bot: "+message.lower())

def filterParking(message,bot,id):
    resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
    print (resultPln)
    message="¿Fumas?"
    bot.sendMessage(chat_id=id, text=message)
    writeConversation(str(id),"bot: "+message.lower())

def filterDisability(message,bot,id): #acesso para personas con discapacidad
    resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
    print (resultPln)
    message="¿Necesitas estacionamiento?"
    bot.sendMessage(chat_id=id, text=message)
    writeConversation(str(id),"bot: "+message.lower())

def filterCashOnly(message,bot,id):
    resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
    print (resultPln)
    message="¿Tienes alguna discapacidad o vas en compañía de alguien en esta condición?"
    bot.sendMessage(chat_id=id, text="Para una mejor comodidad:")
    bot.sendMessage(chat_id=id, text=message)
    writeConversation(str(id),"bot: "+message.lower())    

def filterTypeFood(message,bot,id):
    resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
    print (resultPln)
    message="¿Pagaras en efectivo o con algún tipo tarjeta?"
    bot.sendMessage(chat_id=id, text="¡Me antoje!")
    bot.sendMessage(chat_id=id, text=message)
    writeConversation(str(id),"bot: "+message.lower())

def filterProfesion(message, bot, id):
    resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
    print (resultPln) #continuar con los sinonimos de estudiar (estudio)
    message="¿Quieres desayuno, almuerzo o cena?"
    bot.sendMessage(chat_id=id, text="¡Muy buena profesión!, para tener más certeza:")
    bot.sendMessage(chat_id=id, text=message)
    writeConversation(str(id),"bot: "+message.lower())

def filterHourFood(message, bot, id):
    resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
    if(len(resultPln)==1):
        if isMealBreakfast(resultPln[0]):
            #se debe filtrar los restaurantes que tengan true en la bd knowledge
            print('consulta de restaurante con true meal_breakfast')
        elif isMealLunch(resultPln[0]):
            #se debe filtrar los restaurantes que tengan true en la bd knowledge
            print('consulta de restaurante con true meal_lunch')
        elif isMealDinner(resultPln[0]):
            #se debe filtrar los restaurantes que tengan true en la bd knowledge
            print('consulta de restaurante con true meal_dinner')
    else:
        print('caso presentado')
        print (resultPln)
        message="¿Quieres desayuno, almuerzo o cena?"
        bot.sendMessage(chat_id=id, text="¡Ops, revisa que tengas bien la escritura de lo que deseas comunicarme, se me dificultad entender!")
        bot.sendMessage(chat_id=id, text=message)
        writeConversation(str(id),"bot: "+message.lower())

    message="¿Cuál es el tipo de comida que más te gusta?"
    message2="¿o disfrutas más la comida de algún país en especial?"
    bot.sendMessage(chat_id=id, text="Ahora dime:")
    bot.sendMessage(chat_id=id, text=message)
    bot.sendMessage(chat_id=id, text=message2)
    writeConversation(str(id),"bot: "+message2.lower())

def isMealBreakfast(text):
    return pln.islistBreakfast(text)

def isMealLunch(text):
    return pln.islistLunch(text)

def isMealDinner(text):
    return pln.islistDinner(text)

def readLastMessageConversation(id): #retornar la ultima linea del archivo que tiene creado para el usuario
    return readLastLineConversation(str(id))[len(readLastLineConversation(str(id)))-1].lower().replace('bot: ','').replace(' ','').replace('\n','')

def isValidateAge(age):
    return True if age>=10 and age<=100 else False

def filterAge(message, bot, id):
    resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
    #print(resultPln)
    if(isOneDigit(resultPln)):
        value = int(resultPln[0])
        if(isValidateAge(value)):#es un rango de edad valido?
            #se debe asginar el valor difurso con este valor que es un solo digito     
            #se continua con la conversación porque ya tomo el valor difuso
            valueFuzzy = fl.getAge(value)
            values = [int(id),value]
            adminDB.insertValue('(id, edad)','users',values)
            message="¿Cuál es tu profesión o qué haces a diario?"
            bot.sendMessage(chat_id=id, text="¡Que bien! y cuentame:")
            bot.sendMessage(chat_id=id, text=message)
            writeConversation(str(id),"bot: "+message.lower())
        else:
            message="¿Qué edad tienes?"
            bot.sendMessage(chat_id=id, text="¡Ops, tu edad no se encuentra en el rango de 15-100 años, ingresa tu edad correctamente!")
            bot.sendMessage(chat_id=id, text=message)
            writeConversation(str(id),"bot: "+message.lower())
    else:
        if(len(findDigits(resultPln))>0):#se verifica si si tiene digitos
            if(isOnlyDigits(resultPln)):#se verifica que solos ean digitos
                #se encontro mas de un numero por lo que se deberia notificar el usuario que digite d enuev
                message="¿Qué edad tienes?"
                bot.sendMessage(chat_id=id, text="¡Ops, cuando ingresas más de una cadena de números no puedo identificar tu edad, vuelve a intentarlo!")
                bot.sendMessage(chat_id=id, text=message)
                writeConversation(str(id),"bot: "+message.lower())
            else:#se extrae el primero valor digito de todos los texto
                value = int(firstDigit(resultPln))
                print('falta hallar valor difuso para: '+str(value))
                #se continua con la conversación porque ya tomo el valor difuso
                message="¿Cuál es tu profesión o qué haces a diario?"
                bot.sendMessage(chat_id=id, text="¡Que bien! y cuentame:")
                bot.sendMessage(chat_id=id, text=message)
                writeConversation(str(id),"bot: "+message.lower())
        else: 
            #no se esta reconociendo ningun digito pero esta palabra paso el pln
            #print(resultPln)
            message="¿Qué edad tienes?"
            bot.sendMessage(chat_id=id, text="¡Ops, lo siento pero aún no se reconoce la fecha por texto, ingresa tu edad como un número!")
            bot.sendMessage(chat_id=id, text=message)
            writeConversation(str(id),"bot: "+message.lower())

def firstDigit(resultPln):
    for word in resultPln:
        if (word.isdigit()):
            return word
    return 'None'
def isOneDigit(resultPln):
    return len(findDigits(resultPln)) ==1 and len(resultPln) == 1

def isOnlyDigits(resultPln):
    return len(findDigits(resultPln))==len(resultPln)

def findDigits(resultPln):
    words = []
    for word in resultPln:
        if (word.isdigit()):
            words.append(word)
    return words

def start(bot, update):
    id = update.message.chat_id
    user = update.message.from_user
    message = '¿qué edad tienes?'
    bot.sendMessage(chat_id=update.message.chat_id, text='¡Hola '+user.first_name+'! Bienvenido al Sistema Recomendador de Restaurantes. Para empezar:')
    bot.sendMessage(chat_id=update.message.chat_id, text=message)
    writeConversation(str(id),"bot: "+message)

def writeConversation(id,message):
    file = open(id, 'a')
    file.write(message+'\n')
    file.close()

def readLastLineConversation(id):
    file = open(id, 'r') 
    data = file.readlines()
    file.close()
    return data

def identifiedOptionConversation(id): #retorna el identificador para cada 
    lastMessage=readLastMessageConversation(id)
    print(lastMessage)
    if lastMessage=='¿quéedadtienes?':
        return 0
    elif lastMessage =='¿cuálestuprofesiónoquéhacesadiario?':
        return 1
    elif lastMessage =='¿quieresdesayuno,almuerzoocena?':
        return 2
    elif lastMessage =='¿odisfrutasmáslacomidadealgúnpaísenespecial?':
        return 3
    elif lastMessage =='¿pagarasenefectivooconalgúntipotarjeta?':
        return 4
    elif lastMessage =='¿tienesalgunadiscapacidadovasencompañíadealguienenestacondición?':
        return 5
    elif lastMessage =='¿necesitasestacionamiento?':
        return 6
    elif lastMessage =='¿fumas?':
        return 7
    elif lastMessage =='¿tienespensadotomaralcoholhoy?':
        return 8
    elif lastMessage =='¿vasconamigos?':
        return 9
    else:
        return 10

def main():
    adminDB.createDB()
    updater = Updater('205961193:AAE4XZ9K6VcdfnzM7DvTuI1JsIF_SVKQ_Fo')
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    listener_handler = MessageHandler([Filters.text], listener)
    dispatcher.add_handler(listener_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()