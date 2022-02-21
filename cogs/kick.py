from nextcord.ext import commands
import nextcord

class kick(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, member : nextcord.Member, *, reason=None):
        await member.kick(reason=reason)
        moderator = self.bot.get_member() #in parentheses bot will auto cache mod's dev ID
        await ctx.reply(f"{member.mention} was kicked for the reason of {reason}")
        await ctx.member.send(f"You were kicked from the **CHPS Discord Server** for the reason of {reason}\n\n **Moderator:** {moderator} ")

    
def setup(bot):
    bot.add_cog(kick(bot))