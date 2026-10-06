import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {{bot.user.name}} ({{bot.user.id}})')
    print('------')

    @bot.command()
    async def ping(ctx):
        await ctx.send('Pong!')

        async def main():
            async with bot:
                await bot.load_extension('cogs.minecraft')
                await bot.load_extension('cogs.database')
                await bot.load_extension('cogs.discordsrv')
                await bot.start(os.getenv('DISCORD_TOKEN'))

                if __name__ == '__main__':
                    asyncio.run(main())
