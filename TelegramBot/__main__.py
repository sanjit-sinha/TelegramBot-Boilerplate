from TelegramBot import bot
from TelegramBot.logging import LOGGER

LOGGER(__name__).info("Starting the TelegramBot...")
if __name__ == "__main__":
    bot.run()
