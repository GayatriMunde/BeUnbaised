import discord
from discord import channel
from discord.ext import commands
from discord import message

from trie.userRecord import UserRecord
from trie.trie import Trie

import random


client = discord.Client()
colors = discord.colour
trie = Trie()
record = UserRecord()
table = {
    "\"": None,
    "'": None,
    "-": None,
    "`": None,
    "~": None,
    ",": None,
    ".": None,
    ":": None,
    ";": None,
    "_": None
}


def buildTrie():
    file = open("DiscordBot/trie/words.txt", 'r')

    for line in file:
        line = line.strip()
        trie.insert(line)


def punish_user(user_id):
    user_id = '<@' + str(user_id) + '>'
    responses = [
        "Come on now, {}. Did you really need to say that?",
        "{} - LANGUAGE!",
        "Hey now {}, watch your mouth.",
        "We don't use that kind of language here, {}."
    ]

    choice = random.choice(responses)
    choice = choice.format(user_id)

    return choice


@client.event
async def on_ready():
    buildTrie()
    print("Bot is ready")


@client.event
async def on_message(message):
    text = message.content
    text = text.translate(str.maketrans(table))
    author_id = message.author.id

    if author_id != 884475820696043540:
        isClean = True
        message_word_list = text.split()
        for word in message_word_list:
            if trie.search(word):
                isClean = False
                break
        if not isClean:
            await message.channel.send(punish_user(author_id))

    
client.run(TOKEN)

