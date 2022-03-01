
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_comm import*
from datetime import datetime


updater = Updater('5129676163:AAHGI5IeNCXkzWSY576C5OOBOIopTVnvK9I')
updater.dispatcher.add_handler(CommandHandler('start', start_command))
updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))

updater.start_polling()
updater.idle()