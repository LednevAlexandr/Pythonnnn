from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import datetime

def log(update: Update, context: CallbackContext) -> None:
    file = open('db.csv','a',encoding ='UTF8')
    file.write(f'{update.effective_user.first_name},{update.effective_user.id},{update.message.text}\n')
    file.close()