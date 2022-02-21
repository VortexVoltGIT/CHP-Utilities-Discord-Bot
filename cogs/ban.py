from nextcord.ext import commands
import nextcord

class ban(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def ban(self, ctx, member : nextcord.Member, *, reason=None):
        await member.ban(reason=reason)
        moderator = self.bot.get_member() #in parentheses bot will auto cache mod's dev ID
        await ctx.reply(f"{member.mention} was banned for the reason of {reason}")
        await ctx.member.send(f"You were banned from the **CHPS Discord Server** for the reason of {reason}\n\n **Moderator:** {moderator} ")

def setup(bot):
    bot.add_cog(ban(bot))