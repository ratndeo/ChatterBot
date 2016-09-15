from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
from chatterbot.adapters.output.action_adapter import ActionAdapter


def get_date():
    from datetime import date
    return date.today().strftime("%d-%m-%y")


def get_location():
    return "Bangalore"


def get_time():
    import time
    return time.strftime("%H:%M:%S")

action_map = {
    "date": "example.get_date",
    "location":"example.get_location"
}


# Create a new instance of a ChatBot
bot = ChatBot("ActionBot",
              storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
              logic_adapters=[
                  "chatterbot.adapters.logic.ClosestMatchAdapter"
              ],
              input_adapter="chatterbot.adapters.input.TerminalAdapter",
              # output_adapter="chatterbot.adapters.output.TerminalAdapter",
              output_adapter="chatterbot.adapters.output.action_adapter.ActionAdapter",
              delegate_adapter="chatterbot.adapters.output.TerminalAdapter",
              action_map=action_map,
              database="../database.db",
              )
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train(os.path.join(os.path.dirname(__file__), "action_data"))
print("Type something to begin...")
# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break