#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The custom bot for registering complaints for Janagraha Issue Reporting System
"""

import logging
import requests
import traceback
from telegram.ext import Updater
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import CommandHandler, MessageHandler, Filters, ConversationHandler
from config import TG_BOT_API, FLASK_URL

# Logging Setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

LOCATION, SELECT_OPTIONS, COMPLAINT, VIEW_STATUS = range(4)

COMPLAINT_REGISTERED = 4

RETRY = 5

END = ConversationHandler.END

OPTION_MAP = {
    COMPLAINT: "Register Complaint",
    VIEW_STATUS: "View Status of Complaint",

}


def start(update, context):
    """
    Entry point for the bot
    :param update:
    :param context:s
    :return:
    """
    update.message.reply_text(
        'Hi! I\'m here to help you with the complaints. Thank you so much for taking your time!\n'
        'Please send me you location to continue')

    return LOCATION

def location(update, context):
    user = update.message.from_user
    user_location = update.message.location
    context.user_data["user_location"] = user_location
    logger.info("Location of %s: %f / %f", user.first_name, user_location.latitude,
                user_location.longitude)
    reply_options = [["Register Complaint", "View Status of Complaint"]]
    update.message.reply_text('Thank you for providing the location. Please select from the options below',
                              reply_markup=ReplyKeyboardMarkup(reply_options, one_time_keyboard=True))

    return SELECT_OPTIONS


def skip_location(update, context):
    user = update.message.from_user
    logger.info("User %s did not send a location.", user.first_name)
    update.message.reply_text('I\'m so srry. But we cannot continue without your location')

    return LOCATION


def end(update, context):
    """End conversation from InlineKeyboardButton."""
    update.callback_query.answer()

    text = 'See you around!'
    update.callback_query.edit_message_text(text=text)

    return END


def register_complaint(update, context):
    """Reached through SELECT_OPTIONS keyword"""
    context.user_data['choice'] = update.message.text
    update.message.reply_text(
        'Okay, please tell me about the complaint',
        reply_markup=ReplyKeyboardRemove())

    return COMPLAINT_REGISTERED


def get_status(update, context):
    """Callback to display status of the registered complaints"""

    def pretty_print(response):
        text = "Here are the complaints you have registered\n\n\n"
        for complaint in response['complaints']:
            text += "\n\n\nComplaint ID: %s\n\nCategory: %s\n\nLocation: %s\n\nText: %s\n\nStatus: %s"%(
                complaint["id"],
                complaint["category"],
                complaint["location"],
                complaint["text"],
                complaint["status"]
            )
        return text

    def get_status_api(username):
        responses = requests.get(FLASK_URL+"/api/complaints", params={"user_name": username})
        response_json = responses.json()
        return response_json

    text = update.message.text
    user = update.message.from_user

    try:
        response = get_status_api(user.first_name)
        print(response)
        text = pretty_print(response)
        print(text)
        text += "\nThank you so much for the concern."
    except Exception as e:
        traceback.print_stack()
        text = "Oh I'm so sorry. I'm unable to get information regarding the" \
               " complaints at the moment. Please try again later."
    finally:
        update.message.reply_text(text)
        update.message.reply_text("Thank you")
        return ConversationHandler.END


def complaint_registered(update, context):
    """API call to store complaint text"""
    if "choice" in context.user_data:
        choice = context.user_data["choice"]

    def send_data_api(username, userid, text, user_location):
        request_json = {
            "user" : {
                "username": username,
                "id": userid
            },
            "location" : {
                "lat" : user_location.latitude,
                "long" : user_location.longitude
            },
            "complaint_text": text
        }
        response = requests.post(FLASK_URL+"/api/complaint", json=request_json)
        return response.json()



    text = update.message.text
    user = update.message.from_user

    if choice == OPTION_MAP[COMPLAINT]:
        try:
            response = send_data_api(user.first_name, user.id, text, context.user_data["user_location"])
            text = "Your complaint has been registered with us under %s. " \
                   "Thank you so much for your efforts." % (response['complaint']['category'])
        except Exception as e:
            text = "Oh I'm so sorry. I'm unable to register any complaints at the moment. Please try again later."
            print(e.with_traceback())
        finally:
            update.message.reply_text(text)
            update.message.reply_text("Thank you")
            return ConversationHandler.END
    else:
        update.message.reply_text("Thank you")
        return ConversationHandler.END

def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def generic_response(update, context):
    update.message.reply_text("Hello there! Please type start to continue.")

def failure_response_selection(update, context):
    update.message.reply_text("I'm sorry I don't understand. Please select the below options.")

def failure_response_location(update, context):
    update.message.reply_text("I'm sorry I don't understand. Please enter the location")


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TG_BOT_API, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Set up top level ConversationHandler (selecting action)
    # Because the states of the third level conversation map to the ones of the econd level
    # conversation, we need to make sure the top level conversation can also handle them
    selection_handlers = [
        MessageHandler(Filters.regex('^Register Complaint$'), register_complaint),
        MessageHandler(Filters.regex('^View Status of Complaint$'), get_status),
        MessageHandler(Filters.regex('(?!View Status of Complaint|Register Complaint).*$') &
                       ~Filters.regex('^[cC]ancel$'), failure_response_selection)
    ]
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start),
                      MessageHandler(Filters.regex('^start|Start|Hi|hi|Hey|hey|hello|Hello$'), start)],

        states={
            SELECT_OPTIONS: selection_handlers,
            LOCATION: [MessageHandler(Filters.location, location),
                       CommandHandler('skip', skip_location),
                       MessageHandler(Filters.text & ~Filters.location & ~Filters.regex('^[cC]ancel$'), failure_response_location)],
            COMPLAINT_REGISTERED: [MessageHandler(Filters.text, complaint_registered)],
            RETRY: [CommandHandler('start', start)],
        },

        fallbacks=[CommandHandler('cancel', cancel),
                   MessageHandler(Filters.regex('^[cC]ancel$'), cancel)],
    )
    general_handler = MessageHandler(Filters.text, generic_response)
    dp.add_handler(conv_handler)
    dp.add_handler(general_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()



