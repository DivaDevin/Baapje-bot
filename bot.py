import discord

from discord.ext.commands import Bot

from discord.ext import commands

import asyncio

import time
 
import random



client = discord.Client()

client = commands.Bot(command_prefix = "!")


@client.event
async def on_message(message):                  
    
    if message.content == 'cookie':
         await client.send_message(message.channel, ':cookie:')

    elif message.content == 'train':
        await client.send_message(message.channel, ':train:')

    elif message.content == 'eggplant':
        await client.send_message(message.channel, ':eggplant:')

    elif message.content == 'tongue':
        await client.send_message(message.channel, ':tongue:')
    

    elif message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, '<@%s> Pong!' % (userID))



    elif  message.content.startswith('!guess'):
 
        await client.send_message(message.channel, 'Guess a number between 1 to 10')



        def guess_check(m):

            return m.content.isdigit()



        guess = await client.wait_for_message(timeout=5.0, author=message.author, check=guess_check)

        answer = random.randint(1, 10)

        if guess is None:

            fmt = 'Sorry, you took too long. It was {}.'

            await client.send_message(message.channel, fmt.format(answer))

            return

        if int(guess.content) == answer:

            await client.send_message(message.channel, 'You are right!')

        else:

            await client.send_message(message.channel, 'Sorry, It is  {}.'.format(answer))



    elif message.content.startswith('!meme'):
        for user in message.mentions:
            msg = 'You\'re the meme in this server!{}'.format (user.mention)
            await client.send_message(message.channel, msg)
                                  
 
                                  
                                                    
client.run('NDI4NDY1Njk2OTI2ODU5MjY0.DalIWg.ViY2n7lDc9LENalNAIkqu9-W2xs')

