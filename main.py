import disnake
from config import settings
from cogs.Functions.functions import unban_members
from cogs.Constants.constants import bot


@bot.event
async def on_ready():
    activity = disnake.Game(name="/help for help", type=3)
    await bot.change_presence(status=disnake.Status.online, activity=activity)
    await unban_members()


# Загрузка когов
bot.load_extension("cogs.clear")
bot.load_extension("cogs.ban")
bot.load_extension("cogs.kick")
bot.load_extension("cogs.mute")
bot.load_extension("cogs.reactions")
bot.load_extension("cogs.other")
bot.load_extension("cogs.events")


bot.run(settings['token'])
