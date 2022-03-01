from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import datetime
from log import*

def start_command(update: Update, context: CallbackContext) -> None:
    log(update,context)
    update.message.reply_text(f'/hi - приветствие\n/time - тукущее время\n/help - список всех команд\n/sum - сумма дыух чисел')

def hi_command(update: Update, context: CallbackContext) -> None:
    log(update,context)
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def time_command(update: Update, context: CallbackContext) -> None:
    log(update,context)
    update.message.reply_text(f'Время: {datetime.now().time()}')
    
def help_command(update: Update, context: CallbackContext) -> None:
    log(update,context)
    update.message.reply_text(f'/hi - приветствие\n/time - тукущее время\n/help - список всех команд\n/sum - сумма дыух чисел')

def sum_command(update: Update, context: CallbackContext) -> None:
    log(update,context)
    mas = update.message.text
    temp =mas.split()
    x = int(temp[1])
    y = int(temp[2])
    update.message.reply_text(f'{x}+{y} = {x+y}')