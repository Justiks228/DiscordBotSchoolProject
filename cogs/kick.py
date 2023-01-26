import disnake
from disnake.ext import commands
from cogs.Functions import functions


class KickCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="bkick", description='Выгоняет указанного участника.')
    @commands.dynamic_cooldown(functions.give_guild_cooldown, commands.BucketType.user)
    async def slash_bkick(self, inter, member: disnake.Member, *, reason: str = commands.Param(name='reason')):
        try:
            await functions.chq_moder_role(ctx=inter)
            await member.kick(reason=reason)
            await inter.response.send_message(embed=disnake.Embed(description=f'**{member} был изгнан с сервера по причине {reason}!** :white_check_mark:'))
        except:
            await inter.response.send_message(embed=disnake.Embed(description=f'**Мне не удалось изгнать** {member}! **Он имеет роль выше чем я!** :x: \n *Fix error: Сделайте роль бота более приоритетной. Настройки сервера :gear: -> Роли -> Перетащите роль JustB с помощью мышки :mouse2:*'))

    @commands.command(description='Выгоняет указанного участника.')
    @commands.dynamic_cooldown(functions.give_guild_cooldown, commands.BucketType.user)
    async def bkick(self, ctx, member: disnake.Member, *, reason):
        try:
            await functions.chq_moder_role(ctx=ctx)
            await member.kick(reason=reason)
            await ctx.send(embed=disnake.Embed(description=f'**{member} был изгнан с сервера по причине {reason}!** :white_check_mark:'))
        except:
            await ctx.send(embed=disnake.Embed(description=f'**Мне не удалось изгнать** {member}! **Он имеет роль выше чем я!** :x: \n *Fix error: Сделайте роль бота более приоритетной. Настройки сервера :gear: -> Роли -> Перетащите роль JustB с помощью мышки :mouse2:*'))


def setup(bot: commands.Bot):
    bot.add_cog(KickCommand(bot))
