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
          await message.channel.send("Hey Pri, hope this will inspire the shit out of you hahah")

      if message.content.startswith('-get-shit-done'):
        images = glob.glob("/home/runner/discordbots/servers/mmmm/images/get_shit_done/*")

        await message.channel.send(f'Sending {len(images)} images that will make you to get shit done\n')
        
        for image in images:
          await utils.sendImageToChannel(
            __file__, 
            message.channel, 
            os.path.sep.join(image.split("/")[-3:])
          )

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

      if message.content.startswith('-song'):
        file_path = "/home/runner/discordbots/servers/mmmm/audio/pictures_of_you.mp3"
        await message.channel.send(
          file = discord.File(file_path)
        )
      
  try:
    client.run(os.environ['TOKEN_MMMM'])
    print("TOKEN fetched in MMMM")
  except:
    print("ERROR IN GETTING TOKEN in MMMM")