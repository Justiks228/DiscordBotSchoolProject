import disnake
from disnake.ext import commands
from cogs.Functions import functions


class MuteCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.slash_command(description='Выдаёт таймаут указанному участнику')
    @commands.dynamic_cooldown(functions.give_guild_cooldown, commands.BucketType.user)
    async def mute(self, ctx, member: disnake.Member, duration, *, reason):
        try:
            await functions.chq_moder_role(ctx=ctx)
            ban_time, time_qly, time = await functions.give_time_punishment(ctx=ctx, duration=duration)
            await member.timeout(duration=ban_time, reason=reason)
            await ctx.response.send_message(embed=disnake.Embed(description=f'**{member} замучен! :white_check_mark: \n Срок:** {time+time_qly} \n** Причина:** {reason}'))
        except:
            await ctx.response.send_message(embed=disnake.Embed(description=f'**Мне не удалось замутить** {member}!  **Возможные причины:** \n \n  1. Вы неверно указали аргумент duration! Ex. 10s,1m,30d** \n \n2.  **Пользователь которого вы хотите наказать имеет роль выше чем я!** :x: \n *Fix error: Сделайте роль бота более приоритетной. Настройки сервера :gear: -> Роли -> Перетащите роль JustB с помощью мышки :mouse2:*'))


    @commands.command(description='Выдаёт таймаут указанному участнику.')
    @commands.dynamic_cooldown(functions.give_guild_cooldown, commands.BucketType.user)
    async def mute(self, ctx, member: disnake.Member, duration, *, reason):
        try:
            await functions.chq_moder_role(ctx=ctx)
            ban_time, time_qly, time = await functions.give_time_punishment(ctx=ctx, duration=duration)
            await member.timeout(duration=ban_time, reason=reason)
            await ctx.send(embed=disnake.Embed(description=f'**{member} замучен! :white_check_mark: \n Срок:** {time+time_qly} \n** Причина:** {reason}'))
        except:
            await ctx.send(embed=disnake.Embed(description=f'**Мне не удалось замутить** {member}!  **Возможные причины:** \n \n  1. Вы неверно указали аргумент duration! Ex. 10s,1m,30d** \n \n2.  **Пользователь которого вы хотите наказать имеет роль выше чем я!** :x: \n *Fix error: Сделайте роль бота более приоритетной. Настройки сервера :gear: -> Роли -> Перетащите роль JustB с помощью мышки :mouse2:*'))


    @commands.slash_command(description='Убирает таймаут указанному игроку')
    @commands.dynamic_cooldown(functions.give_guild_cooldown, commands.BucketType.user)
    async def unmute(self, ctx, member: disnake.Member):
        try:
            await functions.chq_moder_role(ctx=ctx)
            await member.timeout(duration=0, reason='Требование действующего модератора/администратора сервера.')
            await ctx.response.send_message(embed=disnake.Embed(description=f'{member} **был успешно размучен!** :white_check_mark:'))
        except:
            await ctx.response.send_message (embed=disnake.Embed(description=f'**Мне не удалось размутить** {member}! **Он имеет роль выше чем я!** :x: \n *Fix error: Сделайте роль бота более приоритетной. Настройки сервера :gear: -> Роли -> Перетащите роль JustB с помощью мышки :mouse2:*'))


    @commands.command(description='Убирает таймаут указанному игроку')
    @commands.dynamic_cooldown(functions.give_guild_cooldown, commands.BucketType.user)
    async def unmute(self, ctx, member: disnake.Member):
        try:
            await functions.chq_moder_role(ctx=ctx)
            await member.timeout(duration=0, reason='Требование действующего модератора/администратора сервера.')
            await ctx.send(embed=disnake.Embed(description=f'{member} **был успешно размучен!** :white_check_mark:'))
        except:
            await ctx.send(embed=disnake.Embed(description=f'**Мне не удалось размутить** {member}! **Он имеет роль выше чем я!** :x: \n *Fix error: Сделайте роль бота более приоритетной. Настройки сервера :gear: -> Роли -> Перетащите роль JustB с помощью мышки :mouse2:*'))

def setup(bot: commands.Bot):
    bot.add_cog(MuteCommand(bot))