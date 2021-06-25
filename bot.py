import discord
from discord.utils import get
from discord.ext import commands
import os

t = True
intents = discord.Intents.default()
intents.members = True  
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():   #What the bot does when it starts up
  print("Ready")
  await bot.change_presence(activity=discord.Game(name="Giving roles")) #He is permaplaying "giving roles with this"

@bot.event
async def on_raw_reaction_add(reaction): #When someone reacts to some message this triggers
    msg = "858061816310792262" #id of the message meant for react
    id = str(reaction.message_id) #converts the id of the message who triggered this in a string
    guild = bot.get_guild(reaction.guild_id) #know the id of the server
    usuario = guild.get_member(int(reaction.user_id)) #know the id of who reacted


    if msg == id: #if the id of the message who triggered this is the same of the message meant to be reacted
        print("si") #comprobation
        reaccion = str(reaction.emoji) #know the id of the reacion
        print(reaccion)
        if "<:assettoicon:856622922453614612>" == reaccion: #if the id of the reaction mathches the id of the reaction meant for this triggers
            print("si")
            
            role = discord.utils.get(guild.roles, id=858064599243554826) #know the id of the role wanted
            await usuario.add_roles(role) #give the role to the user who reacted
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