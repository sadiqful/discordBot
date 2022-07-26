import discord
import os
import requests
import json
import random
from replit import db

client = discord.Client()

sad_words = [
    "sad", "frustrated", "anxious", "tired", "mad", "depressed", "down",
    "angry", "depressing", "exhausting", "low"
]

starter_encouragements = [
    'Hi there, you are absoluty amazing. Hang in there',
    'Hey, you are brillant. You will get through this',
    'You are amazing my dear friend. Do not be sad', 'You are loved',
    'Cheer up', 'Hang in there'
]


def get_qoute():
    response = requests.get('https://zenquotes.io/api/random/')
    json_data = json.loads(response.text)
    qoute = json_data[0]['q'] + " -" + json_data[0]['a']
    return qoute

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements 
  else: 
    db["encouragements"] = [encouraging_message]
    
def delete_encouragements(index): 
  encouragements = db["encouragements"]
  if length.encouragements > index: 
    del encouragements[index]
    db["encouragements"] = encouragements

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

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))


client.run(os.getenv('TOKEN'))
