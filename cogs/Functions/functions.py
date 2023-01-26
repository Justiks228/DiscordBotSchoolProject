import disnake
import re
import asyncio
import datetime
from cogs.Constants.constants import bot

from DataBase_connector.db_connect import DB


async def chq_moder_role(ctx):
    if ctx.author.guild_permissions.administrator is False:
        select = await DB.execute('SELECT moderator_role_id FROM servers_info WHERE id_server = ?')
        fetch = await select.fetchall()
        role = disnake.utils.get(ctx.guild.roles, id=fetch[0])
        if role not in ctx.author.roles:
            await ctx.send(embed=disnake.Embed(description='**Нет прав! :x:**'))
            raise Exception('Not Found moder role in author.guild.roles')


async def give_time_punishment(ctx, duration):
    if len(duration) > 3:
        await ctx.send(embed=disnake.Embed(description='**Длина аргумента duration должна быть не более 3 символов!**'))
        raise Exception('MyArgumentError')
    time_qly = re.findall('[s, m, h, d]+', duration)[0]
    time = re.findall(r'\d+', duration)[0]
    if time_qly == 's':
        ban_time = int(time)
    elif time_qly == 'm':
        ban_time = int(time) * 60
    elif time_qly == 'h':
        ban_time = int(time) * 3600
    elif time_qly == 'd':
        ban_time = int(time) * 86400
    return ban_time, time_qly, time


async def unban_members():
    select = await DB.execute('SELECT datatime FROM ban_members')
    fetch = await select.fetchall()
    for i in fetch:
        try:
            if i[2] < datetime.datetime.now().timestamp():
                member = await bot.fetch_user(i[1])
                await bot.get_guild(i[2]).unban(member)
                await DB.execute("DELETE FROM ban_members WHERE member_id=? AND guild_id=?", (fetch[1], bot.get_guild(i[2]).id))
                await DB.commit()
        except:
            await DB.execute("DELETE FROM ban_members WHERE member_id=? AND guild_id=?", (fetch[1], bot.get_guild(i[2]).id))
            await DB.commit()
            continue

    await asyncio.sleep(600)
    await unban_members()


def give_guild_cooldown(message):
    #SQL = await DB.cursor()
    #if message.author.guild_permissions.administrator:
        #return disnake.ext.commands.Cooldown(rate=1, per=0)
    #for value in await SQL.execute('SELECT * FROM servers_info'):
        #if value[0] == message.guild.id:
            #return disnake.ext.commands.Cooldown(rate=1, per=value[3])
    #return disnake.ext.commands.Cooldown(rate=1, per=10)
    return disnake.ext.commands.Cooldown(rate=1, per=10)
