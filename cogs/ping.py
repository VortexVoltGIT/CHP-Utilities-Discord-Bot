from nextcord.ext import commands
import nextcord

class ping(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.reply(f':ping_pong: **Ping {round (self.bot.latency * 1000)} ms Pong ** :ping_pong: ')

def setup(bot):
    bot.add_cog(ping(bot))