import os
import discord

async def sendImageToChannel(file_path, channel, image_path):
  absolute_path = os.path.dirname(os.path.abspath(file_path))
  filename = absolute_path + os.path.sep + image_path
  with open(filename, 'rb') as fp:
    await channel.send(file=discord.File(fp, image_path.split("/")[-1] ))