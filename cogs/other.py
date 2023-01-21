import disnake
from disnake.ext import commands
from cogs.Constants.constants import DISNAKE_COLORS


class OtherCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description='Создаёт сообщение типа embed')
    async def embed(self, ctx, color='default', *, reason):
        await ctx.response.send_message(embed=disnake.Embed(description=reason, colour=DISNAKE_COLORS.get(color)))


    @commands.command(description='Создаёт сообщение типа embed')
    async def embed(self, ctx, color='default', *, reason):
        await ctx.send(embed=disnake.Embed(description=reason, colour=DISNAKE_COLORS.get(color)))


    @commands.slash_command(description='Отправляет сообщене о командах бота')
    async def help(self, ctx, topic: str = commands.Param(name='topic',
                                                    choices=['Модераторские команды', 'Голосование', 'Реакции по ролям',
                                                             'Прочее'])):
        if topic == 'Модераторские команды':
            await ctx.response.send_message(embed=disnake.Embed(description='''**/clear <Количество сообщений>** \n *Удаляет указанное количество сообщений. Существует slash и text версия команды.* \n *Пример использования: /clear 10* 
                                                                       \n**/pban <Пользователь> <Причина блокировки>** \n *Перманентно блокирует пользователя. Существует slash и text версия команды.* \n *Пример использования: /pban @Test_user Флуд!* 
                                                                       \n **/tempban <Пользователь> <Время> <Причина>** \n *Блокирует пользователя на указанное время. Существует slash и text версия команды.* \n *Пример использования: /tempban @Test_User 10sРеклама * 
                                                                       \n **/bkik <Пользователь> <Причина>** \n *Кикает пользователя с сервера. Существует slash и text версия команды.* \n *Пример использования: /bkick @TestUser Нарушение правил* 
                                                                       \n **/mute <Пользователь> <Время> <Причина>** \n *Выдаёт указанному пользователю тамйаут на указанное время. Существует slash и text версия команды* \n *Пример использования: /mute @Test_User 30s Нарушение правил*'''))
        elif topic == 'Голосование':
            await ctx.response.send_message(embed=disnake.Embed(description='''**/add_vote <Количество реакций>** \n \n *Добавляет реакцию на* **reply** *сообщение. Существует только text версия команды.* \n \n  *Для создания голосования напишите сообщение например как это:* \n \n В какую игру играешь? \n :zero: - Dota 2 \n :one: - Minecraft \n :two: - CS:GO 
            \n *Отправьте его, щёклните ПКМ по нему и выберите пункт Ответить (в англ. версии reply) и напишите команду -add_vote. \n \n Бот сделает реакцию :zero: на это сообщение. Повторите процедуру несколько раз, что бы добавить больше вариантов голосования.* \n \n *В голосовании не может быть больше 10 вариантов выбора!* 
            \n*Скажите участникам своего сервера ставить реакции под этим сообщением взависимости от их выбора.* \n \n *Так же существует дополнительный, необяз. аргумент reason. Он означает количество реакций добавленных под сообщение, создан для экономии времени. Вместо того что бы 5 раз писать -add_vote напишите -add_vote 5*\n*Ваше голосование готово! Бот не даст участнику проголосовать за два разных варианта ответа.*'''))
        elif topic == 'Реакции по ролям':
            await ctx.response.send_message(embed=disnake.Embed(description='''**/add_reactionrole <Эмоджи> <Упоминание роли>** \n \n *Добавляет реакцию на* **reply** *сообщение. Существует только text версия команды.* 
                                                                            \n *Для того что бы сделать* **reactionrole** сообщение, напишите сообщение похожее на это:* \n \n Какую роль хочешь получить? \n :toilet: - унитаз \n :white_check_mark: - Белой галочкой \n :x: - буквой Х. 
                                                                            \n*Отправьте его, щёклните ПКМ по нему и выберите пункт Ответить (в англ. версии reply) и напишите команду -add_reactionrole, в аргументах укажите эмоджи и соответственно какая роль будет выдаваться по нажатии по ней. Повторите действие несколько раз* 
                                                                            \n *Готово! Бот добавит реакцию, по нажатию по ней пользователь получит соответствующую роль. Примечание: если пользователь нажмёт 2 реакции, останется только 1 роль.* 
                                                                             \n *Если вы хотите удалить из reactionrole сообщения 1 из пунктов выдачи ролей просто уберите все не нужные реакции* \n *Примечание: для создания reactionrole сообщения нельзя использовать численные эмоджи такие как :one: :two: :four: :nine: и т.д.*'''))
        elif topic == 'Прочее':
            await ctx.response.send_message(embed=disnake.Embed(
                description='''**/embed <Цвет> <Содержание>** \n \n *Создаёт сообщение типа embed (Как например вот это). Существует slash и text версия команды.* \n *Пример использования: /embed blue Я Just Bot*'''))

def setup(bot: commands.Bot):
    bot.add_cog(OtherCommand(bot))