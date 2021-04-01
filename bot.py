#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import csv
import telegram

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
bot=telegram.Bot(token="1652850405:AAF-wGXPg4pNsQhZ-TARv78F9j5qK4CCRrY")
data_csv = 'data.csv'
with open('data.csv', 'r') as file:
    
    message=""
    reader = csv.reader(file)
    line_count = 0
    for row in reader:
        if line_count == 0:
            print(f'{" ".join(row)}')
            line_count += 1
        else:
             message += row[0] +" . <b>"+row[1] +"</b> \n"+ " Starts from" + row[2]+ " onwards \n ends in " + row[3] + " \n Website Link :" + row[4] +"\n" 
             print(f"""\t{row[0]}  {row[1]}  {row[2]} {row[3]} {row[4]}.""")    
             line_count += 1
    
    print(f'Processed {line_count} lines.')  
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def HI(update, context):
    """Send a message when the command /HI is issued."""
    update.message.reply_text("""WELCOME TO THE IoT LAB!""")
 
def gokul(update, context):
    """Send a message when the command /gokul is issued."""
    update.message.reply_text("""GOKULAKRISHNAN-191MC126
    MOBILE-1234567890""")
    
def bala(update, context):
    """Send a message when the command /bala is issued."""
    update.message.reply_text("""BALAKUMAR-191MC110
    MOBILE-8903220635""")

def help(update, context):
    """Send a message when the command /bala is issued."""
    update.message.reply_text("""THESE ARE THE COMMANDS
      /hi
    /gokul
    /bala
    /competition
    /form
    """)    

def form(update, context):
    """Send a message when the command /form is issued."""
    update.message.reply_text("""Fill out the form 👇 👇 👇
    https://forms.gle/VREhdtCNqJ6rZNfQ7""")

def competition(update, context):
    """Send a message when the command /competition is issued."""
    #update.message.reply_text(s)
    chat_id = update.message.chat_id
    bot.send_message(chat_id,text=message,
    parse_mode=telegram.ParseMode.HTML)
    #return s  

#def echo(update, context):
 #   """Echo the user message."""
  #  update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1652850405:AAF-wGXPg4pNsQhZ-TARv78F9j5qK4CCRrY", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("hi", HI))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("gokul",gokul))
    dp.add_handler(CommandHandler("bala",bala))
    dp.add_handler(CommandHandler("form",form))
    dp.add_handler(CommandHandler("competition",competition))

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

