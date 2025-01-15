import discord 
from discord.ext import commands
import os
from dotenv import load_dotenv
ALLOWED_GUILD_ID = int(os.getenv("guild_id"))

load_dotenv()
login = os.getenv("login")

intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix="?")

def is_allowed_guild():
    async def predicate(ctx):
        return ctx.guild and ctx.guild.id == ALLOWED_GUILD_ID
    return commands.check(predicate)

@bot.event()
async def on_ready():
    print(f"{bot.user} has started")


@bot.command()
@is_allowed_guild()
async def test(ctx):
    await ctx.reply("This is a test message")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.reply("This command is not available in this server.")
    else:
        raise error


bot.run(login)