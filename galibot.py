import telebot, ledcontrol

types = telebot.types
bot = telebot.TeleBot("140398368:AAG-LjPjcehq-T6GUhLbi4IJ5uB7XRxl_I0")
users = list()


pins = [{'pin':0,'name':'Zero'},{'pin':2,'name':'Dos'}]
gpio = ledcontrol.wiringx86_dummy()
Leds = ledcontrol.LedControl(pins,gpio)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Hola! Sigo en Construccion")

@bot.message_handler(commands=['ledcontrol'])
def showKeyboard(message):
  markup = types.ReplyKeyboardMarkup(row_width=len(Leds.leds),selective=True,one_time_keyboard=True)
  for x in Leds.leds:
    markup.add(x.name)
  bot.send_message(message.chat.id,"Choose a Led",reply_markup=markup,reply_to_message_id=message.message_id)
  users.append(message.chat.id)

@bot.message_handler(func=lambda message: (message.text in Leds.getNames()) and (message.chat.id in users))
def controlLed(message):
  pin = Leds.getNames().index(message.text)
  Leds.leds[pin].toggleState()
  print "toggle " + str(pin)

@bot.message_handler(commands=['showstate'])
def showState(message):
  Strings = Leds.getNames()
  replymessage = ""
  for x in Strings:
    replymessage += x
    replymessage += ": "
    replymessage += "On" if Leds.leds[Strings.index(x)].getState() == 1 else "Off"
    replymessage += "\n"
  replymessage = replymessage[:-1]
  bot.reply_to(message,replymessage)

if __name__=="__main__":
  bot.polling()
