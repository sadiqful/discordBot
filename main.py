import discord
import os
import requests
import json

client = discord.Client()

def get_qoute():
  response = requests.get('https://zenquotes.io/api/random/')
  json_data = json.loads(response.text)
  qoute = json_data[0]['q'] + " -" + json_data[0]['a']
  return qoute

@client.event
async def on_ready():
    print('We are logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$inspire'):
      qoute = get_qoute()
    await message.channel.send(qoute)


client.run(os.getenv('TOKEN'))
