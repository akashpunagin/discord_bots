import discord
import os
from services.quotes import get_quote

def run():

  print("Running Chill Palace")

  client = discord.Client()


  @client.event
  async def on_ready():
      print('chill palace: We have logged in as {0.user}'.format(client))

  @client.event
  async def on_message(message):
      if message.author == client.user:
          return

      if message.content.startswith('-hey'):
          await message.channel.send('Hey yourself !')

      if message.content.startswith('-jss'):
        await message.channel.send('We do not talk about this!')

      if message.content.startswith('-inspire'):
        quote = get_quote()
        await message.channel.send(quote)

  try:
    client.run(os.environ['TOKEN_CHILL_PALACE'])
    print("TOKEN fetched in chill palace")
  except:
    print("ERROR IN GETTING TOKEN in chill palace")