import discord
import os
from services.quotes import get_quote
from services.jokes import get_joke
from services.jokes import jokes_categories

def run():

  print("Running PFP")

  client = discord.Client()


  @client.event
  async def on_ready():
      print('PFP: We have logged in as {0.user}'.format(client))

  @client.event
  async def on_message(message):
      # print('client', client.user)
      # print('message', message.author)
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
        if (message.content.startswith("-joke --help")):
          msg = "Get Jokes From \"-joke\" command !\n\nAdditional Options:\n"

          for index, category in enumerate(jokes_categories):
            msg = msg + (f"\t{index + 1}. {category}\n")

          msg = msg + "Enter specific number to get jokes from that category\nEg: -jokes --1"
          await message.channel.send(msg)  
        else:

          try:
            list_args = message.content.split("--")

            if (len(list_args) <= 1):
              await message.channel.send(get_joke(-1)) # All
            else:
              arg = list_args[1]


              if (len(arg) > 1):
                raise Exception("Please enter only one number after --")
              else:
                number = int(arg)
                if (number > len(jokes_categories)):
                  raise Exception(f"Please enter number between 1 and {len(jokes_categories)}")

                await message.channel.send(get_joke(number))

          except ValueError:
              await message.channel.send("Please enter a number after -- ")
          except Exception as e:
              await message.channel.send(e)
            
  try:
    client.run(os.environ['TOKEN_PFP'])
    print("TOKEN fetched in PFP")
  except:
    print("ERROR IN GETTING TOKEN in PFP")