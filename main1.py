# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext
# # from bot_command import*

# def hi_command(update: Update, context: CallbackContext):
#     update.message.reply_text(f'hi {update.effective_user.first_name}!')

# updater = Updater('5289448381:AAFv40JGzXaTOunGSW6zPCiZt9C-AdlchdQ')

# updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
# # updater.dispatcher.add_handler(CommandHandler('time', time_command))
# # updater.dispatcher.add_handler(CommandHandler('help', help_command))
# # updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
# print('start')


# updater.start_polling()
# updater.idle()
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater('5289448381:AAFv40JGzXaTOunGSW6zPCiZt9C-AdlchdQ')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()