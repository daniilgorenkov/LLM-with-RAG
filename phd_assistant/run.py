import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from bot import PhDAssistantBot

if __name__ == "__main__":
    bot = PhDAssistantBot()
    asyncio.run(bot.run())
