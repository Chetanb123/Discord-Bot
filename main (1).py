from discord.ext import commands
import os
import discord
import random



intents = discord.Intents.all()
bot = commands.Bot(command_prefix = '!', intents=intents)
bot.videos = ["https://youtu.be/8m4nDOkoY64", "https://youtu.be/P16dS29eHIY", "https://youtu.be/X0do6yC4Tgo"]
bot.happylist = []

@bot.command()
async def hello(ctx):
  await ctx.send("hello " + ctx.author.display_name)

@bot.command()
async def legoat(ctx):
  await ctx.send(random.choice(bot.videos))

@bot.command()
async def happy(ctx, *, item):
    await ctx.send("wowzers cuh")
    bot.happylist.append(item)
    print(bot.happylist)

@bot.command()
async def sad(ctx):
  await ctx.send("Yo jit look at this pluh")
  await ctx.send(random.choice(bot.happylist))

@bot.command()
async def calc(ctx, x: float, fn: str, y: float):
    if fn == '+':
        await ctx.send(x + y)
    elif fn == '-':
        await ctx.send(x - y)
    elif fn == '*':
        await ctx.send(x * y)
    elif fn == '/':
        await ctx.send(x / y)
    else:
        await ctx.send("We only support 4 function operations")

password = os.environ['password']
bot.run(password)

