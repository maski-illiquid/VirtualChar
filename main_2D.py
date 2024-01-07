from twitchio.ext import commands
from chat import *
import vlc
import os
import time
import nltk
import creds
from TextToAudio import GenerateAudio_2D

CONVERSATION_LIMIT = 20

class Bot(commands.Bot):
    
    conversation = list()

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token= creds.TWITCH_TOKEN, prefix='!', initial_channels=[creds.TWITCH_CHANNEL])
        

    async def event_ready(self):
        # Notify us when everything is ready!
        print(f'Logged in as | {self.nick}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        if message.echo:
            return

        # download the words corpus
        nltk.download('words')

        # Check if the message contains english words
        if not any(word in message.content for word in nltk.corpus.words.words()):
            return
        
        # Check if the message is too long or short
        if len(message.content) > 70 or len(message.content) < 3:
            return
        
        print('------------------------------------------------------')
        print(message.content)
        print(message.author.name)
        print(Bot.conversation)

        content = message.content.encode(encoding='ASCII',errors='ignore').decode()

        response = GenerateResponse(content)
        print('RESPonse:' , response)

        if(Bot.conversation.count(response) == 0):
            Bot.conversation.append(response)
        
        if len(Bot.conversation) > CONVERSATION_LIMIT:
            Bot.conversation = Bot.conversation[1:]
        
        audio_file, length = GenerateAudio_2D(response,message.author.name)
        print(f'Length of File {length+1.5}')
        playerMedia = vlc.MediaPlayer(audio_file)
        playerMedia.play()
        time.sleep(length+1.5)
        os.remove(audio_file)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'Hello {ctx.author.name}!')

bot = Bot()
bot.run()



