import discord
from discord.utils import get
from discord.ext import commands
import os

t = True
intents = discord.Intents.default()
intents.members = True  
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():  
  print("Ready")
  await bot.change_presence(activity=discord.Game(name="Giving roles"))

@bot.event
async def on_raw_reaction_add(reaction):
    msg = "858061816310792262"
    id = str(reaction.message_id)
    guild = bot.get_guild(reaction.guild_id)
    usuario = guild.get_member(int(reaction.user_id))


    if msg == id:
        print("si")
        reaccion = str(reaction.emoji)
        print(reaccion)
        if "<:assettoicon:856622922453614612>" == reaccion:
            print("si")
            
            role = discord.utils.get(guild.roles, id=858064599243554826)
            await usuario.add_roles(role)
        elif "<:acc:858073968379428868>" == reaccion:
            print("si2")
            
            role = discord.utils.get(guild.roles, id=858074298153304064)
            await usuario.add_roles(role)
        elif "<:f1icon:856622870359703582>" == reaccion:
            print("si2")
            
            role = discord.utils.get(guild.roles, id=858074668606423120)
            await usuario.add_roles(role)
        elif "<:f2icon:856622883110518784>" == reaccion:
            print("si2")
            
            role = discord.utils.get(guild.roles, id=858075262410555442)
            await usuario.add_roles(role)



bot.run("TOKEN")