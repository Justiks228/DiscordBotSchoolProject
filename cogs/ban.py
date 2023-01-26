import disnake
import asyncio
from disnake.ext import commands
from cogs.Functions import functions
from DataBase_connector.db_connect import DB
import datetime


class BanCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="pban", description='Перманентно банит пользователя.')
    @commands.dynamic_cooldown(functions.give_guild_cooldown, commands.BucketType.user)
    async def slash_pban(self, inter, member: disnake.Member, *, reason):
        try:
            await functions.chq_moder_role(ctx=inter)
            await member.ban(reason=reason)
            await inter.response.send_message(embed=disnake.Embed(description=f'**{member} заблокирован! :white_check_mark: \n Срок:** Бессрочно \n** Причина:** {reason}'))
        except:
            await inter.response.send_message(embed=disnake.Embed(description=f'**Мне не удалось заблокировать** {member}! **Он имеет роль выше чем я!** :x: \n *Fix error: Сделайте роль бота более приоритетной. Настройки сервера :gear: -> Роли -> Перетащите роль JustB с помощью мышки :mouse2:*'))

    @commands.command()
    @commands.dynamic_cooldown(functions.give_guild_cooldown, commands.BucketType.user)
    async def pban(self, ctx, member: disnake.Member, *, reason='None'):
        try:
            await functions.chq_moder_role(ctx=ctx)
            await member.ban(reason=reason)
            await ctx.send(embed=disnake.Embed(description=f'**{member} заблокирован! :white_check_mark: \n Срок:** Бессрочно \n** Причина:** {reason}'))
        except:
            await ctx.send(embed=disnake.Embed(description=f'**Мне не удалось заблокировать** {member}! **Он имеет роль выше чем я!** :x: \n *Fix error: Сделайте роль бота более приоритетной. Настройки сервера :gear: -> Роли -> Перетащите роль JustB с помощью мышки :mouse2:*'))

    @commands.slash_command(name="tempban", description='Банит пользователя на поставленное кол-во времени')
    @commands.dynamic_cooldown(functions.give_guild_cooldown, commands.BucketType.user)
    async def slash_tempban(self, inter, member: disnake.Member, duration: str = commands.Param(name='time'), *, reason: str = commands.Param(name="reason")):
        try:
            SQL = await DB.cursor()
            await functions.chq_moder_role(ctx=inter)
            ban_time, time_qly, time = await functions.give_time_punishment(ctx=inter, duration=duration)
            await member.ban(reason=reason)
            await inter.response.send_message(embed=disnake.Embed(description=f'**{member} заблокирован! :white_check_mark: \n Срок:** {time+time_qly} \n** Причина:** {reason}'))
            if ban_time < 600:
                await asyncio.sleep(ban_time)
                await member.unban()
                return
            await SQL.execute(f'INSERT INTO ban_members VALUES (?,?,?)', (inter.guild.id, member.id, int(datetime.datetime.now().timestamp()+ban_time)))
            await DB.commit()
        except:
            await inter.response.send_message(embed=disnake.Embed(description=f'**Мне не удалось заблокировать** {member}! **Возможные причины:** \n \n  1. Вы неверно указали аргумент duration! Ex. 10s,1m,30d** \n \n2. Пользователь которого вы хотите наказать имеет роль выше чем я!** :x: \n *Fix error: Сделайте роль бота более приоритетной. Настройки сервера :gear: -> Роли -> Перетащите роль JustB с помощью мышки :mouse2:*'))

    @commands.command(description='Банит пользователя на поставленное кол-во времени')
    @commands.dynamic_cooldown(functions.give_guild_cooldown, commands.BucketType.user)
    async def tempban(self, ctx, member: disnake.Member, duration, *, reason='None'):
        try:
            SQL = await DB.cursor()
            await functions.chq_moder_role(ctx=ctx)
            ban_time, time_qly, time = await functions.give_time_punishment(ctx=ctx, duration=duration)
            await member.ban(reason=reason)
            await ctx.send(embed=disnake.Embed(description=f'**{member} заблокирован! :white_check_mark: \n Срок:** {time+time_qly} \n** Причина:** {reason}'))
            if ban_time < 600:
                await asyncio.sleep(ban_time)
                await member.unban()
                return
            await SQL.execute('INSERT INTO ban_members VALUES (?,?,?)', (ctx.guild.id, member.id, int(datetime.datetime.now().timestamp()+ban_time)))
            await DB.commit()
        except:
            await ctx.send(embed=disnake.Embed(description=f'**Мне не удалось заблокировать** {member}! **Возможные причины:** \n \n  1. Вы неверно указали аргумент duration! Ex. 10s,1m,30d** \n \n2. Пользователь которого вы хотите наказать имеет роль выше чем я!** :x: \n *Fix error: Сделайте роль бота более приоритетной. Настройки сервера :gear: -> Роли -> Перетащите роль JustB с помощью мышки :mouse2:*'))


def setup(bot: commands.Bot):
    bot.add_cog(BanCommand(bot))
