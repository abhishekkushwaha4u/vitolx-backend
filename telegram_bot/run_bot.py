import logging
import time
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from dotenv import load_dotenv
from pathlib import Path
import sys
import requests

env_path = Path('.env')
load_dotenv(dotenv_path=env_path)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

mode = os.getenv("mode")
token = os.getenv("token")

if mode == "dev":
    def run(updater):
        updater.start_polling()
elif mode == "prod":
    def run(updater):
        PORT = int(os.environ.get("PORT", "8443"))
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=token)
        updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, token))
else:
    logger.error("No mode specified!")
    sys.exit(1)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello there! Please type /notif <code_provided>")

def notif(update, context):
    otp = context.args[0]
    data = {
        'key': os.environ.get('key'),
        'otp': otp,
        'chat_id': int(update.effective_chat.id)
    }
    response = requests.post('http://127.0.0.1:8000/api/v1/user/notification/set/', data=data)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.json()['message'])



if __name__=='__main__':

    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    # Handler for starting the bot
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("notif", notif))


    run(updater)