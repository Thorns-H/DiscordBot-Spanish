"""
Bob Esponja Discord Bot by ThornsH

Este es mi primer código de un bot en python, es de libre uso y basicamente es una gúia para personas
que esten introduciendo al lenguaje también.

Para el uso correcto de este bot se necesita tener pip y pipenv, para crear un entorno virtual de proyecto.
O bien también pueden hostear el bot en Heroku, tal como lo hice yo, para esto se necesita git y también
seguir los pasos de deploy en la página.

Lastest Update : 03/11/2020 - Python 3.9.0
"""
# Importando Librerias

import discord
import re
import random
from discord.ext import commands
from urllib import parse, request
from random import choice
random.randint(1,10) 

# Inicio de Comandos

bot=commands.Bot(command_prefix='.') # Este linea crea el prefijo de cada uno de nuestros comandos para el bot.
bot.remove_command("help") # Esta linea remueve el comando help que viene por default en el bot, para despues crear uno más estetico.

# Esta lista es una variable global de frases que el bot puede decir randomente con el comando .hey

frases=[
    "¿No tienes que ser estúpido en algún otro lugar, Patricio?",
    "Gary, vete de aquí, ¿no ves que estoy tratando de olvidarte?",
    "Patricio, si tuviera un dólar por cada cerebro que no tienes, solo tendría un dólar.",
    "¡La pizza de Don Cangrejo es para ti y para mi!",
    "¡Salgan de mi camino, hay un hombre que va a patearme el trasero!",
    "Es decir que ¿Se apoderaron de lo que creíamos creer y nos hacen creer que creíamos que los pensamientos que hemos tenido son pensamientos que creemos que son que creíamos?",
    "Bueno, puede ser estúpido, ¡Pero también es tonto!",
    "¡Patricio, si tus padres ven a un verdadero tonto, podrán ver que tan genio eres!",
    "Es horrible, ¡Me da asco solo verlo!",
    "¿Qué le pasa a ese estúpido?",
    "¡Cielos que macizo!",
    "¡Yo quiero ser el sucio dan!",
    "¿A quién le esta hablando la gorda?",
    "¿El para qué cosa de quién?",
]

# Comandos útiles y de uso general

@bot.command()
async def help(ctx): # Este comando muestra un embed con todos los demás comandos y su uso.
    embed=discord.Embed(colour = discord.Colour.blue())
    thumbnail="https://i.pinimg.com/originals/8f/c9/6c/8fc96c0582882650b7e1750240c8d773.png"
    embed.set_thumbnail(url=thumbnail)
    embed.set_author(name="Esta es la lista de comandos que el bot tiene :")
    embed.add_field(name=".ping", value="_Muestra la latencia del bot._", inline=False)
    embed.add_field(name=".hey", value="_Haz que Bob te iluestre con sus frases._", inline=False)
    embed.add_field(name=".clear [cantidad]", value="_Elimina mensajes de un canal._", inline=False)
    embed.add_field(name=".youtube [cantidad] , [busqueda]", value="_Busca videos de youtube_", inline=False)
    embed.add_field(name=".default", value="_Regresa al bot a su actividad default._", inline=False)
    embed.add_field(name=".version", value="_Muestra la información del bot y su creador._", inline=False)
    await ctx.send(embed=embed)

# Comandos pendejos y de uso personal

@bot.command()
async def dumb(ctx): # Este comando esta hecho por diversión y solo muestra comandos tontos que tenemos en el servidor propio.
    embed=discord.Embed(colour=discord.Colour.red())
    thumbnail="https://www.pngkit.com/png/full/794-7948977_png-plantilla-momo-holk-bobesponja-patricio-bob-esponja.png"
    embed.set_thumbnail(url=thumbnail)
    embed.set_author(name="Lista de comandos pendejos que tenemos en el bot, enjoy :")
    embed.add_field(name=".say", value="_Por si quieres hacer que bob repita algo_", inline=False)
    embed.add_field(name=".bongocat", value="_Muestra información y la web para jugar con el bongocat_", inline=False)
    embed.add_field(name=".stream", value="_Para cuando Gera este stremeando_", inline=False)
    embed.add_field(name=".memes", value='_Muestra la playlist de videos en youtube de "The Boys"_', inline=False)
    embed.add_field(name=".messirve", value="_Cuando te sirve algo pa'_", inline=False)
    embed.add_field(name=".nomessirve", value="_Cuando no te sirve algo pa'_", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx): # Este comando muestra la latencia que tiene el bot.
    await ctx.send(f"**Tengo un ping de: {round(bot.latency * 1000)}ms**")

@bot.command()
async def hey(ctx): # Este comando hace que bot te responda con un mensaje random de la lista [frases].
    fraserandom=(choice(frases))
    await ctx.send(fraserandom)

@bot.command()
async def bongocat(ctx): # Este comando te envia la información para jugar con el bongocat y su lista de canciones.
    embed=discord.Embed(colour=discord.Colour.blue())
    thumbnail="https://camo.githubusercontent.com/6a953b2bbfa5782ab8ab332714d2a46ee4093de5/68747470733a2f2f626f6e676f2e6361742f6d6574612f7468756d626e61696c2e706e67"
    embed.set_thumbnail(url=thumbnail)
    embed.set_author(name="BongoCat Website w/ Songs Source")
    embed.add_field(name="BongoCat Website", value="_https://bongo.cat/_", inline=False)
    embed.add_field(name="BongoCat Songs", value="_https://github.com/Externalizable/bongo.cat/issues_", inline=False)
    embed.add_field(name="BongoCat Help", value="_https://github.com/Externalizable/bongo.cat_", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def version(ctx): # Este comando muestra las notas de la versión del bot, asi como mis redes sociales.
    embed=discord.Embed(colour=discord.Colour.purple())
    thumbnail="https://i.dlpng.com/static/png/6753650_preview.png"
    embed.set_thumbnail(url=thumbnail)
    embed.set_author(name="Este bot fue hecho por ThornsH")
    embed.add_field(name="¡Sígueme en Instagram!", value="https://www.instagram.com/abrahammh_/", inline=False)
    embed.add_field(name="¡Sígueme en Spotify!", value="https://open.spotify.com/user/abrahamm9986", inline=False)
    embed.add_field(name="¡Agrégame en Steam!", value="https://steamcommunity.com/id/ThornsH/", inline=False)
    embed.add_field(name="Notas de Versión:", value="_Bob Esponja BOT v0.2_\n _Python 3.9.0 - Hosted on Heroku_\n\n_Ultima actualización_ ***03/11/2020***", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, amount : int, *search): # Este comando sirve para buscar videos en youtube, usa .help, para ver sus parametros.
  #  await ctx.send("Uso correcto : .youtube [cantidad de videos], [nombre]")
    results = parse.urlencode({"search_query": search})
    html_content = request.urlopen("https://www.youtube.com/results?"+results)
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    if amount==1:
        await ctx.send('https://www.youtube.com/watch?v=' + search_results [0])
    elif amount==2:
        await ctx.send('https://www.youtube.com/watch?v=' + search_results [0])
        await ctx.send('https://www.youtube.com/watch?v=' + search_results [1])
    elif amount==3:
        await ctx.send('https://www.youtube.com/watch?v=' + search_results [0])
        await ctx.send('https://www.youtube.com/watch?v=' + search_results [1]) 
        await ctx.send('https://www.youtube.com/watch?v=' + search_results [2])
    else:
        await ctx.send("**¡Solo puedo mostrar tres vídeos a la vez!**")

@youtube.error
async def youtube_error(ctx, error): # Este es un error en el comando de .youtube, solo sirve para indicar su uso.
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("**¡Faltan parámetros en el comando!**")
        await ctx.send("**.youtube [cantidad], [busqueda]**")

@bot.command()
async def default(ctx): # Este comando regresa el bot a su estado normal.
    await bot.change_presence(activity=discord.Game(name="¡Estoy Listo! | .help"))

@bot.command() 
async def clear(ctx, amount : int): # Este comando sirve para eliminar mensajes de un canal de texto en discord.
    limite=amount+1
    await ctx.channel.purge(limit=limite)
    if amount==1:
        await ctx.send(f"**¡Se ha eliminado {amount} mensaje exitosamente!**")
    else:
        await ctx.send(f"**¡Se han eliminado {amount} mensajes exitosamente!**")

@clear.error
async def clear_error(ctx, error): # Este es un error del comando .clear, sirve solo para reindicar su uso.
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("**¡Faltan parámetros en el comando!**")
        await ctx.send("**.clear [cantidad]**")

# Comandos de los Superconocidos

@bot.command()
async def messirve(ctx): # Envia un meme de messirve.
    await ctx.send("https://i.ytimg.com/vi/09BKjKu1QUA/sddefault.jpg")

@bot.command()
async def nomessirve(ctx): # Envia un meme de nomessirve.
    await ctx.send("https://i.ytimg.com/vi/Q2maBqfCACM/hqdefault.jpg")

@bot.command()
async def stream(ctx): # Este comando activa el modo stream del bot para el canal de SadGabo_.
    canal="channel"
    images=[
        "https://i.gyazo.com/7e65edcea96c34e9d3972bfeb6c9ec61.png",
        "https://i.gyazo.com/f6d4fde79f4b1c89ab0ceaa963fdbeb6.jpg",
        "https://i.gyazo.com/e8920233558ec252e6b3b0512524e95a.png",
        "https://i.gyazo.com/8de2a76a8eadd4483ba15cda9436eb87.png",
        "https://i.gyazo.com/06ce3a1b1d8628d8b02fbd75a5db5523.png",
    ]
    randomlink=random.choice(images)
    embed=discord.Embed(colour=discord.Colour.red())
    thumbnail="https://static-cdn.jtvnw.net/jtv_user_pictures/bb80df16-9f83-4999-9801-479b95f90cbf-profile_image-70x70.png"
    embed.set_thumbnail(url=thumbnail)
    embed.set_author(name="¡SadGabo esta en vivo!")
    embed.add_field(name="Twitch Channel :", value="**https://www.twitch.tv/sadgabo_** :thumbsup: :100:\n\n @everyone :smiling_imp: :fire:\n\n **¡Cambiado al modo streaming!** :white_check_mark:\n**¡Puedes ver el streaming en el estado del bot!** :white_check_mark:", inline=False)
    embed.set_image(url=randomlink)
    await ctx.send(embed=embed)
    await bot.change_presence(activity=discord.Streaming(name="SadGabo", url="https://www.twitch.tv/sadgabo_" ))

@bot.command()
async def memes(ctx): # Este comando te envia la playlist de videos tontos que tenemos en el servidor.
    await ctx.send ('**Memes Hechos por "ThornsH" on YouTube**')
    await ctx.send("https://www.youtube.com/watch?v=GyYWJ4ZmvNk&list=PLRXtWSospviqD1_hnOea6l1I9mp9plsCo&index=1&ab_channel=AbrahamM.")

@bot.command()
async def say(ctx, *, text): # Este comando sirve para que bob repita lo que quieras (con algunas excepciones).
    message = ctx.message
    if text in ["Chinga tu madre", "chinga tu madre", "chingatumadre", "CHINGA TU MADRE", "CHINGATUMADRE"]:
        await ctx.send("**La tuya en vinagre**")
    else:
        await message.delete()
        await ctx.send(f"{text}")

# Eventos del Servidor

@bot.event
async def on_command_error(ctx, error): # Este evento es un evento general que sirve por si se usa un comando que no existe.
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("**Ese comando no existe, para ver los comandos disponibles usa .help**")

@bot.event
async def on_ready(): # Este evento sirve para que cuando el bot se conecte entre en estado default.
    await bot.change_presence(activity=discord.Game(name="¡Estoy Listo! | .help"))
    print("¡Estoy Listo!")

# Token del Bot 

bot.run('TOKEN')