import telegram
from telegram.ext import Updater, CommandHandler

# Define a function to handle the /start command
def start(update, context):
    # Get the user's chat ID
    chat_id = update.message.chat_id
    # Send the user's chat ID as a message
    context.bot.send_message(chat_id=chat_id, text=f"Your chat ID is {chat_id}")

# Create an updater object and set up the bot
updater = Updater(token='5419432479:AAH7KSrGyVuXQerNl-Uv50R-PMTV9ydjvqs', use_context=True)
dispatcher = updater.dispatcher

# Add a command handler for the /start command
dispatcher.add_handler(CommandHandler('start', start))

# Start the bot
updater.start_polling()
