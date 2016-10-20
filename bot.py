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
        filterDisability(message,bot,id)
    elif option == 5:
        filterAlcohol(message,bot,id)
    elif option == 6:
        filterWithFriends(message,bot,id)
    else:
        bot.sendMessage(chat_id=id, text="No entender")
def filterWithFriends(message,bot,id):
    resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
    if(verifyWordPositive(resultPln)):
        print('si va con amigos')
        bot.sendMessage(chat_id=id, text="Te recomiendo")
        writeConversation(str(id),"bot: "+message.lower())
    elif(verifyWordNegative(resultPln)):
        print('no va con amigos')
        bot.sendMessage(chat_id=id, text="Te recomiendo")
        writeConversation(str(id),"bot: "+message.lower())
    else:
        message="¿Vas con amigos?"
        askAgainPositiveNegative(bot,id,message)

def askAgainPositiveNegative(bot,id,question):
    bot.sendMessage(chat_id=id, text="¡Ops, no puedo entenderte, menciona una palabra afirmativa o negativa para conocer tu respuesta!")
    bot.sendMessage(chat_id=id, text=question)
    writeConversation(str(id),"bot: "+question.lower())

def verifyWordPositive(resultPln):
    for word in resultPln:
        if(pln.isWordAfirmative(word)):
            return True
        else:
            pass
    return False

def verifyWordNegative(resultPln):
    for word in resultPln:
        if(pln.isWordNegative(word)):
            return True
        else:
            pass
    return False

def filterAlcohol(message,bot,id):
    resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
    try:
        resultPln.remove('mi')
        resultPln.remove('mis')
    except:
        pass
    if(verifyWordPositive(resultPln)):
        print('si tomará alcohol')
        askWithFriends(bot,id)
    elif(verifyWordNegative(resultPln)):
        print('no tomará alcohol')
        askWithFriends(bot,id)
    else:
        message="¿Tienes pensado tomar alcohol hoy?"
        askAgainPositiveNegative(bot,id,message)
    
def askWithFriends(bot,id):
    message="¿Vas con amigos?"
    bot.sendMessage(chat_id=id, text="Y como última pregunta:")
    bot.sendMessage(chat_id=id, text=message)
    writeConversation(str(id),"bot: "+message.lower())

def filterDisability(message,bot,id): #acesso para personas con discapacidad
    resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
    if(verifyWordPositive(resultPln)):
        print('si necesita restaurante para discapacitados')
        askAlcohol(bot,id)
    elif(verifyWordNegative(resultPln)):
        print('no necesita restaurante para discapacitador')
        askAlcohol(bot,id)
    else:
        message="¿Tienes alguna discapacidad o vas en compañía de alguien en esta condición?"
        askAgainPositiveNegative(bot,id,message)

def askAlcohol(bot,id):       
    message="¿Tienes pensado tomar alcohol hoy?"
    bot.sendMessage(chat_id=id, text=message)
    writeConversation(str(id),"bot: "+message.lower())

def listTypeFood(type):
    print('tipo ingresado: '+str(type))
    if(type==1):
        return ['American','Traditional','Contemporary','Latin American','Southern']
    elif(type==2):
        return ['Italian','European','Mediterranean','French']
    elif(type==3):
        return ['Asian','Japanese']
    elif(type==4):
        return ['Sushi','Seafood']
    elif(type==5):
        return ['Cafe','Coffee','Pub Food','Tea']
    elif(type==6):
        return ['Sandwiches','Pizza','Fast Food','Burgers']
    elif(type==7):
        return ['Grill','Barbecue','Steak']
    elif(type==8):
        return ['Bakery']
    else:
        print('no esta en un rango de 1 a 11, verificar porque paso')

def filterTypeFood(message,bot,id):
    resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
    typeFood = verifyTypeFood(resultPln)
    if(typeFood!=12):
        print(listTypeFood(typeFood))
        bot.sendMessage(chat_id=id, text="¡Me antoje!")
        message="¿Tienes alguna discapacidad o vas en compañía de alguien en esta condición?"
        bot.sendMessage(chat_id=id, text="Para una mejor comodidad:")
        bot.sendMessage(chat_id=id, text=message)
        writeConversation(str(id),"bot: "+message.lower())
    else:
        message="¿Cuál es el tipo de comida que más te gusta?"
        message2="¿o disfrutas más la comida de algún país en especial?"
        bot.sendMessage(chat_id=id, text="!Ops, lo siento pero el tipo de comida que ingresas no es claro, vuelve a intentarlo!")
        bot.sendMessage(chat_id=id, text=message)
        bot.sendMessage(chat_id=id, text=message2)
        writeConversation(str(id),"bot: "+message2.lower())          
     

def verifyTypeFood(resultPln):
    for word in resultPln:
        if(pln.isTypeFood1(word)):
            return 1
        elif(pln.isTypeFood2(word)):
            return 2
        elif(pln.isTypeFood3(word)):
            return 3
        elif(pln.isTypeFood4(word)):
            return 4
        elif(pln.isTypeFood5(word)):
            return 5
        elif(pln.isTypeFood6(word)):
            return 6
        elif(pln.isTypeFood7(word)):
            return 7
        elif(pln.isTypeFood8(word)):
            return 8
        else:
            pass
    return 12
def filterProfesion(message, bot, id):
    resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
    valueProfession, rangeProfession = fl.getProfession(resultPln)
    values = [int(id), valueProfession, rangeProfession]
    adminDB.insertValue('(id, profesion, rangoProfesion)', 'users', values)
    rangeAge = adminDB.getRangeAge(int(id))
    rangePrice = adminDB.getRangePrice(rangeProfession, rangeAge)
    restaurants = adminDB.getRestaurantsPrice(rangePrice)
    if len(restaurants)<4:
        bot.sendMessage(chat_id=id, text="Deberias ir a")
        writeConversation(str(id),"bot: "+message.lower())
        bot.sendMessage(chat_id=id, text=restaurants[0][1])
        adminDB.dropRestaurantsView()
    else:
        message="¿Quieres desayuno, almuerzo o cena?"
        bot.sendMessage(chat_id=id, text="¡Muy buena profesión!, para tener más certeza:")
        bot.sendMessage(chat_id=id, text=message)
        writeConversation(str(id),"bot: "+message.lower())

def filterHourFood(message, bot, id):
    resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message)))) 
    #se debe filtrar los restaurantes que tengan true en la bd knowledge
    if verifyListBreakFast(resultPln):
        print('consulta de restaurante con true meal_breakfast')
        askTypeFood(id,bot)
    elif verifyListLunch(resultPln):
        print('consulta de restaurante con true meal_lunch')
        askTypeFood(id,bot)
    elif verifyListDinner(resultPln):
        print('consulta de restaurante con true meal_dinner')
        askTypeFood(id,bot)
    else:
        message="¿Quieres desayuno, almuerzo o cena?"
        bot.sendMessage(chat_id=id, text="¡Ops, revisa que tengas bien la escritura de lo que deseas comunicarme, se me dificultad entender!")
        bot.sendMessage(chat_id=id, text=message)
        writeConversation(str(id),"bot: "+message.lower())

def askTypeFood(id,bot):
    message="¿Cuál es el tipo de comida que más te gusta?"
    message2="¿o disfrutas más la comida de algún país en especial?"
    bot.sendMessage(chat_id=id, text="Ahora dime:")
    bot.sendMessage(chat_id=id, text=message)
    bot.sendMessage(chat_id=id, text=message2)
    writeConversation(str(id),"bot: "+message2.lower())    


def verifyListBreakFast(values):
    aux = 0
    for word in values:
        if pln.islistBreakfast(word):
            return True
        else:
            pass
    return False

def verifyListLunch(values):
    aux = 0
    for word in values:
        if pln.islistLunch(word):
            return True
        else:
            pass
    return False

def verifyListDinner(values):
    aux = 0
    for word in values:
        if pln.islistDinner(word):
            return True
        else:
            pass
    return False

def readLastMessageConversation(id): #retornar la ultima linea del archivo que tiene creado para el usuario
    return readLastLineConversation(str(id))[len(readLastLineConversation(str(id)))-1].lower().replace('bot: ','').replace(' ','').replace('\n','')

def isValidateAge(age):
    return True if age>=10 and age<=100 else False

def askProfesion(id,bot):
    message="¿Cuál es tu profesión o qué haces a diario?"
    bot.sendMessage(chat_id=id, text="¡Que bien! y cuentame:")
    bot.sendMessage(chat_id=id, text=message)
    writeConversation(str(id),"bot: "+message.lower())

def askAgainAgeError(bot,id,error):
    message="¿Qué edad tienes?"
    bot.sendMessage(chat_id=id, text=error)
    bot.sendMessage(chat_id=id, text=message)
    writeConversation(str(id),"bot: "+message.lower())

def filterAge(message, bot, id):
    resultPln = pln.filterSignes(list(pln.clearEmptyWords(pln.separateText(message))))
    #print(resultPln)
    if(isOneDigit(resultPln)):
        value = int(resultPln[0])
        if(isValidateAge(value)):#es un rango de edad valido?
            #se debe asginar el valor difurso con este valor que es un solo digito     
            #se continua con la conversación porque ya tomo el valor difuso
            rangeAge = fl.getAge(value)
            values = [int(id), value, rangeAge]
            adminDB.insertValue('(id, edad, rangoEdad)','users',values)
            askProfesion(id,bot)
        else:
            error = "¡Ops, tu edad no se encuentra en el rango de 12-100 años, ingresa tu edad correctamente!"
            askAgainAgeError(bot,id,error)
    else:
        if(len(findDigits(resultPln))>0):#se verifica si si tiene digitos
            if(isOnlyDigits(resultPln)):#se verifica que solos ean digitos
                #se encontro mas de un numero por lo que se deberia notificar el usuario que digite d enuev
                error="¡Ops, cuando ingresas más de una cadena de números no puedo identificar tu edad, vuelve a intentarlo!"
                askAgainAgeError(bot,id,error)
            else:#se extrae el primero valor digito de todos los texto
                value = int(firstDigit(resultPln))
                values = [int(id),value]
                adminDB.insertValue('(id, edad)','users',values)
                askProfesion(id,bot)
        else: 
            #no se esta reconociendo ningun digito pero esta palabra paso el pln
            #print(resultPln)
            error="¡Ops, lo siento pero aún no se reconoce la fecha por texto, ingresa tu edad como un número!"
            askAgainAgeError(bot,id,error)
            

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
    elif lastMessage =='¿tienesalgunadiscapacidadovasencompañíadealguienenestacondición?':
        return 4
    elif lastMessage =='¿tienespensadotomaralcoholhoy?':
        return 5
    elif lastMessage =='¿vasconamigos?':
        return 6
    else:
        return 7

def main():
    print('Creando base de datos.')
    adminDB.createDB()
    print('Inicializando sinonimos.')
    fl.initProfession()
    print('Bot iniciado')
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