import logging

import disnake
from disnake.ext import commands

from src.settings import config


class Bot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix=config.PREFIX,
            intents=disnake.Intents.all(),
            reload=True,
            help_command=None,
            status=disnake.Status.online,
        )

    def __call__(self):
        if config.DEBUG:
            logging.basicConfig(level=logging.INFO)
        token = get_token()
        try:
            print("Bot is running...")
            self.run(token)
        except Exception as e:
            print(f"Run bot failed...\nError: {e}")


def get_token() -> str:
    return config.TOKEN_TEST if config.DEBUG else config.TOKEN
