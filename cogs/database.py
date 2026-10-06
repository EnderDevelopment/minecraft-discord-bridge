import discord
from discord.ext import commands
import better_sqlite3

class Database(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn = better_sqlite3.connect('database.db')
        self.create_tables()

        def create_tables(self):
            self.conn.execute('''CREATE TABLE IF NOT EXISTS users (
            discord_id TEXT PRIMARY KEY,
            minecraft_username TEXT
        )''')

            @commands.command()
            async def link_account(self, ctx, minecraft_username):
                self.conn.execute('INSERT OR REPLACE INTO users (discord_id, minecraft_username) VALUES (?, ?)', (str(ctx.author.id), minecraft_username))
                await ctx.send(f'Account linked to {{minecraft_username}}')

                def setup(bot):
                    bot.add_cog(Database(bot))
