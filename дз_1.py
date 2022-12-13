#1) Напишите Бота, удаляющего из текста все слова, содержащие "абв". (Ввод от пользователя)

from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

bot = Bot(token = '5947292295:AAEZe6zzXtXo3amCJO-xrek9i1sOjgjsc8E')
updater = Updater(token = '5947292295:AAEZe6zzXtXo3amCJO-xrek9i1sOjgjsc8E')
dispahather = updater.dispatcher


A = 0


def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет, \n напиши несколько слов, содержащих а и б")
    return A

def find_substr(update, context):
    text = update.message.text.split()
    list = []
    for i in text:
        if 'абв' not in i:
            list.append(i)
    context.bot.send_message(update.effective_chat.id, " ".join(list))
    return ConversationHandler.END

def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, "Пока!")


start_handler = CommandHandler("start", start)
message_handler = MessageHandler(Filters.text, find_substr)
mas_canc_handler = MessageHandler(Filters.text, cancel)

conv_handler = ConversationHandler(entry_points=[start_handler], 
                                   states= {A: [message_handler]},
                                   fallbacks=[mas_canc_handler])

dispahather.add_handler(conv_handler)

updater.start_polling()
updater.idle()