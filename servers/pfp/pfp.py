import discord
import os
from services.quotes import get_quote
from services.jokes import get_joke
from servers.utils import utils


def run():

  print("Running PFP")

  client = discord.Client()


  @client.event
  async def on_ready():
      print('PFP: We have logged in as {0.user}'.format(client))

  @client.event
  async def on_message(message):
      if message.author == client.user:
          return
      
      # if message.author.name.lower().startswith('pramod') and "kill me" not in message.content.lower():
      #   await message.channel.send(f'Hey Pramod, instead of saying {message.content}, why don\'t you kill yourself\nSay kill me in the message and you wont get this message')

      if message.content.startswith('-hello'):
          await message.channel.send('Hello!')

      if message.content == ";":
          await message.channel.send(f'Termination of communication by {message.author}')

      if message.content.startswith('-jss'):
        await message.channel.send('Hey, i just found out this is the best college ever!')

      if message.content.startswith('-inspire'):
        quote = get_quote()
        await message.channel.send(quote)
        if "pramod" in message.content.lower():
          await message.channel.send("Pramod, I believe you have all the inspiration you need (:")

      if message.content.startswith('-joke'):
        await message.channel.send(get_joke(message.content))

      if message.content.startswith('-whos the gang'):
          await utils.sendImageToChannel(__file__, message.channel, "images/image.jpg")
  
      if message.content.startswith('-whos the bitch'):
        await utils.sendImageToChannel(__file__, message.channel, "images/pramod_image.jpg")
            
  try:
    client.run(os.environ['TOKEN_PFP'])
    print("TOKEN fetched in PFP")
  except:
    print("ERROR IN GETTING TOKEN in PFP")