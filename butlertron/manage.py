#! /usr/bin/env python
from tron.bot import Bot
import settings

def main():
    bot = Bot(settings)
    bot.start()

if __name__ == "__main__":
    main()
