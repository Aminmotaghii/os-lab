import os
from gtts import gTTS
from khayyam import JalaliDate, JalaliDatetime
import logging
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton)
from telegram.ext import (
    Updater,
    Filters,
    MessageHandler,
    CommandHandler,
    CallbackContext,
    ConversationHandler,
    CallbackQueryHandler)

GET_BORN_DATE, GET_EN_TEXT, MAX_ARRAY = range(3)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def start(update: Update, _: CallbackContext):
    update.message.reply_text(text='سلام ' + update.effective_user.first_name + ' خوش آمدی!')


def age(update: Update, _: CallbackContext):
    update.message.reply_text(text='دوست عزیر تاریخ تولدت رو به صورت زیر برام بفرس.\n\nمثال: 1400 12 12')
    return GET_BORN_DATE


def send_age(update: Update, _: CallbackContext):
    year = int(update.message.text.split()[0])
    month = int(update.message.text.split()[1])
    day = int(update.message.text.split()[2])
    age = str(JalaliDatetime.now() - JalaliDate(year, month, day)).split()[0]
    age_Y = int(age) // 365
    age_M = (int(age) - (365 * age_Y)) // 30
    age_D = int(age) - age_Y * 365 - age_M * 30
    update.message.reply_text(text='سن شما:\n\n' +
                                   str(age_Y) + ' سال و ' +
                                   str(age_M) + ' ماه و ' +
                                   str(age_D) + ' روز ')


def voice(update: Update, _: CallbackContext):
    update.message.reply_text(text='متن مورد نظر خود را برای تبدیل به ویس بفرستید.\nمتن باید انگلیسی باشد')
    return GET_EN_TEXT


def send_voice(update: Update, _: CallbackContext):
    text = update.message.text
    obj = gTTS(text=text, lang='en', slow=False)
    voice = obj.save('text2voice.ogg')
    update.message.reply_voice(voice=voice)


def maxn(update: Update, _: CallbackContext):
    update.message.reply_text(text='آرایه های عددی به صورت زیر وارد کید تا بیشترین مقدار چاپ شود\n\n'
                                   '15 7 8 12 9 10')
    return MAX_ARRAY


def send_max(update: Update, _: CallbackContext):
    global maxi
    list = update.message.text.split()
    a = []

    for i in list:
        b = a.append(int(i))
        maxi = max(b)
    update.message.reply_text(text='بزرگترین عدد: ' + str(maxi))


def main():
    TOKEN = os.environ['TOKEN']
    updater = Updater(TOKEN)
    conv_handler0 = ConversationHandler(
        entry_points=[CommandHandler('start', start),
                      CommandHandler('age', age),
                      CommandHandler('voice', voice),
                      CommandHandler('max', maxn)],
        states={
            GET_BORN_DATE:
                [MessageHandler(~Filters.regex('^(/start|/age|/max)$'), send_age),
                 CommandHandler('start', start),
                 CommandHandler('age', age),
                 CommandHandler('max', maxn)],
            GET_EN_TEXT:
                [MessageHandler(~Filters.regex('^(/start|/age|/max)$'), send_voice),
                 CommandHandler('start', start),
                 CommandHandler('age', age),
                 CommandHandler('max', maxn)],
            MAX_ARRAY:
                [MessageHandler(~Filters.regex('^(/start|/age|/max)$'), send_max),
                 CommandHandler('start', start),
                 CommandHandler('age', age),
                 CommandHandler('max', maxn)]},
        fallbacks=[CommandHandler('start', start)])

    conv_handler1 = CommandHandler('start', start)
    conv_handler2 = CommandHandler('age', age)
    conv_handler3 = CommandHandler('voice', voice)
    conv_handler4 = CommandHandler('max', maxn)
    updater.dispatcher.add_handler(conv_handler0)
    updater.dispatcher.add_handler(conv_handler1)
    updater.dispatcher.add_handler(conv_handler2)
    updater.dispatcher.add_handler(conv_handler3)
    updater.dispatcher.add_handler(conv_handler4)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
