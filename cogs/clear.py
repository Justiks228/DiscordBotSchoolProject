import disnake
from disnake.ext import commands
from cogs.Functions import functions as func


class ClearCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def clear(self, ctx, reason: int = commands.Param(name="number_of_messages_to_clear")):  # slash-command clear
        await func.chq_moder_role(ctx=ctx)
        await ctx.channel.purge(limit=reason)
        await ctx.response.send_message(embed=disnake.Embed(description=f'**{reason} сообщений(e) удалено!** :white_check_mark:'), delete_after=60)


    @commands.command()
    @commands.dynamic_cooldown(func.give_guild_cooldown, commands.BucketType.user)
    async def clear(self, ctx, reason):  # unslash-command clear
        await func.chq_moder_role(ctx=ctx)
        await ctx.channel.purge(limit=int(reason))
        await ctx.send(embed=disnake.Embed(description=f'**{reason} сообщений(е) удалено!** :white_check_mark:'),delete_after=60)


def setup(bot: commands.Bot):
    bot.add_cog(ClearCommand(bot))

