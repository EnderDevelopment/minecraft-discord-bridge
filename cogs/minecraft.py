import discord
from discord.ext import commands
from mcrcon import MCRcon
import minecraft_server_util

class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.rcon = MCRcon(os.getenv('RCON_HOST'), os.getenv('RCON_PASSWORD'), int(os.getenv('RCON_PORT')))

        @commands.command()
        async def server_status(self, ctx):
            status = minecraft_server_util.status(os.getenv('MINECRAFT_SERVER_IP'), int(os.getenv('MINECRAFT_SERVER_PORT')))
            await ctx.send(f'Server status: {{status}}')

            @commands.command()
            async def player_list(self, ctx):
                self.rcon.connect()
                response = self.rcon.command('/list')
                self.rcon.disconnect()
                await ctx.send(f'Player list: {{response}}')

                @commands.command()
                async def team_finder(self, ctx):
                    # Implement team finder logic here
                    await ctx.send('Team finder feature is not implemented yet.')

                    def setup(bot):
                        bot.add_cog(Minecraft(bot))
