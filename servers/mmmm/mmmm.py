import discord
import os
from services.quotes import get_quote
from services.jokes import get_joke
from servers.utils import utils
import glob
import random


def run():

  print("Running mmmm")

  client = discord.Client()

  @client.event
  async def on_ready():
      print('MMMM: We have logged in as {0.user}'.format(client))

  @client.event
  async def on_message(message):
      if message.author == client.user:
          return

      if message.content == ";":
          await message.channel.send(f'Termination of communication by {message.author}')

      if message.content.startswith('-inspire'):
        quote = get_quote()
        await message.channel.send(quote)
        if "pri" in message.content.lower():
          await message.channel.send("Hey Pri, I have some ") # TODO

      if message.content.startswith('-joke'):
        await message.channel.send(get_joke(message.content))

      if message.content.startswith('-random'):
        images = glob.glob("/home/runner/discordbots/servers/mmmm/images/random/*")
        random_image = random.choice(images)
        await utils.sendImageToChannel(
          __file__, 
          message.channel, 
          os.path.sep.join(random_image.split("/")[-3:])
        )
      
  try:
    client.run(os.environ['TOKEN_MMMM'])
    print("TOKEN fetched in PFP")
  except:
    print("ERROR IN GETTING TOKEN in PFP")