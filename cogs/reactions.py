import disnake
from disnake.ext import commands
from cogs.Functions import functions
from DataBase_connector.db_connect import DB
from cogs.Constants.constants import NUMBER_REACTIONS


class ReactionsCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(description='Добавляет новую эмодзи, с помощью которой можно выдавать роли (упрощённая функция бота ReactionRole)')
    async def add_reactionrole(self, ctx, emoji, give_role):
        try:
            SQL = await DB.cursor()
            await functions.chq_moder_role(ctx=ctx)
            if emoji in NUMBER_REACTIONS:
                await ctx.send(embed=disnake.Embed(description='**Error!** :x: \n **В reactionrole сообщении нельзя использовать численные эмодзи, такие как :one: :two: и т.д.**'))
                return
            msg = await ctx.fetch_message(ctx.message.reference.message_id)
            await msg.add_reaction(emoji)
            await SQL.execute(f'INSERT INTO reactionrole_messages VALUES (?,?,?)', (msg.id, emoji, give_role[3:-1]))
            await DB.commit()
            await ctx.send('Успех :white_check_mark:')
        except:
            await ctx.send(embed=disnake.Embed(description='**Error! :x: \n Возможные причины: \n1). Вы используете не emoji для аргумента emoji \n2). Вы не отреагировали ни на одно сообщение \n3). Вы не упоминаете роль в аргументе role. \n 4). Вы пытаетесь добавить к сообщению уже существующую реакцию. \nEx. - -add_reactionrole :smile: @name_role**'))

    # Голосование
    @commands.command(description='Добавляет дополнительный vote')
    @commands.dynamic_cooldown(functions.give_guild_cooldown, commands.BucketType.user)
    async def add_vote(self, ctx, reason=1):
        try:
            await functions.chq_moder_role(ctx=ctx)
            for i in range(int(reason)):
                msg = await ctx.fetch_message(ctx.message.reference.message_id)
                reaction = [str(reaction) for reaction in msg.reactions]
                if not reaction:
                    await msg.add_reaction('0️⃣')
                for j in reversed(NUMBER_REACTIONS):
                    if j in reaction:
                        await msg.add_reaction(NUMBER_REACTIONS[NUMBER_REACTIONS.index(j) + 1])
        except:
            await ctx.send(embed=disnake.Embed(description='**Error! :x:** \n **Возможные причины:** \n **1). Вы пытаетесь добавить больше 10 vote** \n **2).Вы не сделали reply ни на одно сообщение**'))


def setup(bot: commands.Bot):
    bot.add_cog(ReactionsCommand(bot))
