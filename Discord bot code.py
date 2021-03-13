import discord
from discord.ext import commands
import random
import youtube_dl
import os

client = commands.Bot(command_prefix = '!')
client.remove_command('help')

players = {}

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="your mum - !help"))

    print("Weenur pod is ready!")

@client.command(pass_context=True)
async def coins(ctx):
    coins = 500
    await ctx.send(f"Your number of coins is: {coins}")

@client.command(pass_context = True)
async def shop(ctx):
    embed = discord.Embed(
        title = 'Weenur pods shopping center!',
        colour = discord.Colour.from_rgb(255,255,0)
    )
    embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/814574712126308396/818609933876199446/shop.png')

    embed.add_field(name = '#Whaterver you want it to be', value = 'Coins: 499', inline = True)
    embed.add_field(name = '#Whaterver you want it to be', value = 'FREE', inline = True)
    embed.add_field(name = '#Whaterver you want it to be', value = 'Coins: 100', inline = True)
    embed.add_field(name = '#Whaterver you want it to be', value = '', inline = True)
    embed.add_field(name = '#Whaterver you want it to be', value = 'Coins: 1', inline = True)
    embed.add_field(name = '#Whaterver you want it to be', value = 'Coins: 25', inline = True)

    await ctx.send(embed = embed)

@client.command(pass_context = True)
async def buy(ctx, *, item):
    coins = 500
    if item == '#Whaterver you want it to be':
        n_coins = coins - 25
        await ctx.send("#Whaterver you want it to be")
    elif item == '#Whaterver you want it to be':
        n_coins = coins - 499
        await ctx.send("#Whaterver you want it to be")
    elif item == '#Whaterver you want it to be':
        await ctx.send("#Whaterver you want it to be")
    elif item == '#Whaterver you want it to be':
        n_coins = coins - 100
        await ctx.send("#Whaterver you want it to be")
    elif item == '#Whaterver you want it to be':
        n_coins = coins - 1
        await ctx.send("#Whaterver you want it to be")
    elif item == '#Whaterver you want it to be':
        n_coins = coins - 500
        await ctx.send("#Whaterver you want it to be")


@client.command(pass_context=True)
async def members(ctx):
    member_count = 0
    for member in ctx.guild.members:
        member_count += 1
    await ctx.send(ctx.guild.member_count)

@client.command(aliases = ['user', 'info'])
async def who_dis(ctx, member : discord.Member):
    embed = discord.Embed(title = member.name, color = discord.Colour.from_rgb(255,255,0))
    embed.add_field(name = "ID", value = member.id, inline = True)
    embed.set_thumbnail(url = member.avatar_url)
    await ctx.send(embed=embed)

@client.command(aliases = ['help'])
async def holp(ctx):
    embed = discord.Embed(
        title = 'Weenur pod helpline!',
        colour = discord.Colour.from_rgb(255,255,0)
    )

    embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/814574712126308396/816626948545314866/feck_off.png')

    embed.add_field(name = '!members', value = 'Lets you see the amount of members in the server.', inline = False)
    embed.add_field(name = '!coins', value = ' Shows your balance of coins.', inline = False)
    embed.add_field(name = '!music_help', value = """Lets you play a song from YouTube, write !music_help for all the music commands.""", inline = False)
    embed.add_field(name = '!8ball', value= """Lets you play a game with an 8ball. Write !8ball <your question> and he shall give you the words of wisdom.""", inline = False)
    embed.add_field(name = '!gaming_quiz', value = """Lets you play a gaming quiz. There are three questions to access all of them write gaming_quiz <quiz number> there are 3.""", inline = False)
    embed.add_field(name = '!answer', value = 'Lets you answer the gaming quiz, write !answer <number>.', inline = False)
    embed.add_field(name = '!info', value = """Lets you see the selected discord user's id, there name and there pfp. Write !info @ <user> to see there info.""", inline = False)
    embed.add_field(name = '!shop', value = 'Lets you see all the amazing items in the shop.', inline = False)
    embed.add_field(name = '!buy', value = 'Lets you buy something from the shop, write !buy <item name>.', inline = False)
    
    await ctx.send(embed=embed)

@client.command(aliases = ['music_help'])
async def music(ctx):
    embed = discord.Embed(
        title = 'This is the music helpline!',
        colour = discord.Colour.from_rgb(255,255,0)

    )

    embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/814574712126308396/816640533064712192/wpcmimg.png')

    embed.add_field(name = '!join', value = """This makes the bot join the voice channel you're in.""", inline = False)
    embed.add_field(name = '!play <URL>', value = 'Lets you play a song from YouTube.', inline = False)
    embed.add_field(name = '!leave', value = 'Stops the current song from being played and disconnects the bot.', inline = False)

    await ctx.send(embed=embed)

@client.command(aliases = ['8ball', 'skeleseer'])
async def ball_8(ctx, *, question):
    embed = discord.Embed(
        colour = discord.Colour.from_rgb(255,255,0)
    )
    ball_8_words = ['As i see it, yes',
            'Ask again later',
            'Better not tell you now',
            'Cannot predict now',
            'Dont count on it',
            'It is certain',
            'It is decidedly so',
            'Most likely',
            'My sources say no',
            'Outlook not so good',
            'Reply hazy, try again',
            'Signs point to yes',
            'Very doubtful',
            'Without a doubt',
            'Yes',
            'No',
            'Yes - definitely',
            'You may rely on it']
    
    embed.set_author(name = '8 Ball', icon_url = 'https://cdn.discordapp.com/attachments/814574712126308396/817150768179183636/epic_8_ball_v4.png')
    embed.add_field(name = f'Your question is: {question}', value = f'The answer is: {random.choice(ball_8_words)}', inline = False)

    await ctx.send(embed=embed)


@client.command(pass_context = True)
async def gaming_quiz(ctx):
    embed = discord.Embed(
        title = 'Question 1',
        colour = discord.Colour.from_rgb(255,255,0)
    )

    embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/814574712126308396/818166200068210708/220px-TLOU_P2_Box_Art_2.png')
    embed.add_field(name = 'Who made the Last of us part 2?', value = """1: Santa Monica Studios
    2: CD Project Red
    3: Naughty Dog
    4: 343 Studios
    5: From Software""", inline = False)

    await ctx.send (embed=embed)

@client.command(pass_context = True)
async def gaming_quiz_2(ctx):
    embed = discord.Embed(
        title = 'Question 2',
        colour = discord.Colour.from_rgb(255,255,0)
    )
    embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/814574712126308396/818861477007589444/epic_ps2_2.jpg')
    embed.add_field(name = 'How many PlayStation 2 consoles were sold?', value = """6: 58 Million
    7: 69 Million
    8: 100 Million
    9: 125 Million
    10: 155 Million""", inline = False)

    await ctx.send(embed = embed)

@client.command(pass_context = True)
async def gaming_quiz_3(ctx):
    embed = discord.Embed(
        title = 'Question 3',
        colour = discord.Colour.from_rgb(255,255,0)
    )
    embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/814574712126308396/818862194414452756/epic_mc_2.png')
    embed.add_field(name = 'What planet is the most similar to the scalable size of the Minecraft world?', value = """11: Neptune
    12: Saturn
    13: Jupiter
    14: Venus
    15: Mars""", inline = False)

    await ctx.send(embed = embed)


@client.command(pass_context = True)
async def answer(ctx, *, a_1):
    if a_1 == '1':
        await ctx.send("Your answer is in-correct 👎")
    elif a_1 == '2':
        await ctx.send("Your answer is in-correct 👎")
    elif a_1 == '3':
        await ctx.send("Your answer is correct! 👍")
    elif a_1 == '4':
        await ctx.send("Your answer is in-correct 👎")
    elif a_1 == '5':
        await ctx.send("Your answer is in-correct 👎")
    elif a_1 == '6':
        await ctx.send("Your answer is in-correct 👎")
    elif a_1 == '7':
        await ctx.send("Your answer is correct! 👎")
    elif a_1 == '8':
        await ctx.send("Your answer is in-correct 👎")
    elif a_1 == '9':
        await ctx.send("Your answer is in-correct 👎")
    elif a_1 == '10':
        await ctx.send("Your answer is in-correct 👍")
    elif a_1 == '11':
        await ctx.send("Your answer is correct! 👍")
    elif a_1 == '12':
        await ctx.send("Your answer is in-correct 👎")
    elif a_1 == '13':
        await ctx.send("Your answer is in-correct 👎")
    elif a_1 == '14':
        await ctx.send("Your answer is in-correct 👎")
    elif a_1 == '15':
        await ctx.send("Your answer is in-correct 👎")

@client.command(pass_context = True, aliases = ['vc'])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
        await ctx.send("Joining the VC")
    else:
        voice = await channel.connect()

@client.command(pass_context = True)
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()

@client.command(pass_context = True)
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current song to finish playing or write !leave")
        return

    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, 'song.mp3')
    voice.play(discord.FFmpegPCMAudio('song.mp3'))

@client.command(pass_context = True)    
async def who_made_me(ctx):
    embed = discord.Embed(
        title = 'My creator is...',
        colour = discord.Colour.from_rgb(255,255,0)
    )
    embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/814574712126308396/818865246323605574/angory.png')

    embed.add_field(name = 'Basker12', value = 'My great creator Basker12 is the one who created me! If you want to see my other work click here ---> https://github.com/Basker12', inline = False)
    await ctx.send(embed = embed)
    
#ctx.author.name, ctx.guild.name, ctx.guild.name, user = client.get_member(userid)

client.run('BOT Token here') # NEVER get rid of this line of code

