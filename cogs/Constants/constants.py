import disnake
from disnake.ext import commands
from config import settings

intents = disnake.Intents.all()

bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)


# Константы
NUMBER_REACTIONS = ('0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣')
TIME_QLY = ['s', 'm', 'h', 'd']
DISNAKE_COLORS = {'blue': disnake.Color.blue(), 'red': disnake.Color.red(), 'orange': disnake.Color.orange(),
                  'yellow': disnake.Color.yellow(), 'green': disnake.Color.green(), 'gold': disnake.Color.gold(),
                  'default': disnake.Color.default(), 'magenta': disnake.Color.magenta(),
                  'purple': disnake.Color.magenta()}
