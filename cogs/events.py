import disnake

from DataBase_connector.db_connect import DB
from cogs.Constants import constants
from disnake.ext import commands

class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        try:
            if payload.member.bot:
                return

            msg = await constants.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
            users = []

            for i in msg.reactions:
                users += await i.users().flatten()

            if str(payload.emoji) in constants.NUMBER_REACTIONS:
                if users.count(constants.bot.get_user(payload.user_id)) > 1:
                    await msg.remove_reaction(payload.emoji, constants.bot.get_user(payload.user_id))
                    return

            select = await DB.execute('SELECT role_id FROM reactionrole_messages WHERE id_message = ? AND emoji = ?', (payload.message_id, str(payload.emoji)))
            fetch = await select.fetchone()

            if users.count(constants.bot.get_user(payload.user_id)) > 1:
                await msg.remove_reaction(payload.emoji, constants.bot.get_user(payload.user_id))
                return
            await payload.member.add_roles(disnake.utils.get(payload.member.guild.roles, id=fetch[0]))
            return

        except:
            ctx = await constants.bot.get_context(msg)
            await ctx.send(embed=disnake.Embed(description=f'**Мне не удалось выдать реакцию-роль** ! **Моя роль стоит ниже роли которую вы хотите выдать!** :x: \n *Fix error: Сделайте роль бота более приоритетной. Настройки сервера :gear: -> Роли -> Перетащите роль JustB с помощью мышки :mouse2:*'))


    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        try:
            member = constants.bot.get_guild(payload.guild_id).get_member(payload.user_id)
            if member.bot:
                return
            select = await DB.execute('SELECT role_id FROM reactionrole_messages WHERE id_message = ? AND emoji = ?', (payload.message_id, str(payload.emoji)))
            fetch = await select.fetchone()
            await member.remove_roles(disnake.utils.get(member.guild.roles, id=fetch[0]))
            return
        except (TypeError):
            return


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(embed=disnake.Embed(description=f'**Эта команда перезаряжается, осталось: {int(error.retry_after)} секунд**'))
            return
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=disnake.Embed(description='**Ты указал не достаточное количество аргументов! Не пытайся сломать систему! :x:**'))
            return
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(embed=disnake.Embed(description="**Такой команды не существует! :x:**"))

    @commands.Cog.listener()
    async def on_slash_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.response.send_message(embed=disnake.Embed(description=f'**Эта команда перезаряжается, осталось: {int(error.retry_after)} секунд**'))
            return

def setup(bot: commands.Bot):
    bot.add_cog(Events(bot))
