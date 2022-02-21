from nextcord.ext import commands
import nextcord
import datetime
import humanfriendly

class mute(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def mute(self, ctx, member:nextcord.Member, time, *, reason):
        time = humanfriendly.parse_timespan(time)
        moderator = self.bot.get_member()
        await member.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=time))
        await ctx.reply(f"{member.mention} has been muted for the reason of {reason}")
        await member.send(f"You've been muted in the **CHPS Discord Server** for the reason of {reason}\n\n**Moderator:** {moderator}")
    
    @commands.command()
    async def unmute(self, ctx, member:nextcord.Member, *, reason):
        await member.edit(timeout=None)
        moderator = self.bot.get_member()
        await ctx.reply(f"{member.mention} has been unmuted for the reason of {reason}")
        await member.send(f"You've been unmuted in the **CHPS Discord Server** for the reason of {reason}\n\n**Moderator:** {moderator}")

def setup(bot):
    bot.add_cog(mute(bot))