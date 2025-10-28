import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}')

@bot.command()
async def solve(ctx, expression):
    try:
        result = eval(expression)
        try:
            int(result)
            await ctx.send(str(result))
        except:
            try:
                float(result)
                await ctx.send(str(result))
            except:
                await ctx.send("Sorry, couldn't solve.")
    except:
        await ctx.send("Sorry, couldn't solve.")

bot.run("DISCORD BOT TOKEN")
