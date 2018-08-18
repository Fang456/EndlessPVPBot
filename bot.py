import discord
from discord.ext import commands
import asyncio
import json

config = json.loads(open("./config.json").read())
bot = commands.Bot(command_prefix=config["command-prefix"])
bot.remove_command(name="help")

@bot.event
async def on_ready():
    print("-------------------- EndlessPvP Bot --------------------")
    print("Bot Username: " + bot.user.name + "#" + bot.user.discriminator)
    print("Bot ID: {}".format(bot.user.id))
    print("--------------------------------------------------------")
    print("Created by: TechDylan#1443")
    print("Creation date: 18/08/2018")
    print("--------------------------------------------------------")
    print("                          T&C                           ")
    print("» You must not claim this as your work.")
    print("» This is a free bot, therefore you cannot resell the bot.")

@bot.command()
async def prefix(ctx):
    if not config["role-required-name"] in [role.name for role in ctx.author.roles]:
        await ctx.send(config["no-permission-message"])
    else:
        user = ctx.author
        role = discord.utils.get(ctx.guild.roles, name["donor"])
        await user.add_roles(role)
        try:
            await user.edit(nick="[Donor] " + user.name)
        except discord.Forbidden:
            await ctx.send("I don't have permission to change your nickname.")

bot.run(config["bot-token"])
