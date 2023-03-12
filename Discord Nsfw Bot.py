import discord
import requests
import json
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_message(message):
    if message.content.startswith('!e621'):
        search_query = message.content[6:]
        headers = {
            'User-Agent': '🌸𝙁𝙖𝙞𝙧𝙚𝙣🌸#0069',
            'Authorization': '6hF5atj1HEkNEytKHkpiQEmc'
        }
        url = 'https://e621.net/posts.json?limit=30&tags=' + search_query
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        if 'posts' in data:
            nsfw_posts = [post for post in data['posts'] if 'file' in post and post['rating'] == 'e']
            if len(nsfw_posts) > 0:
                post = nsfw_posts[random.randint(0, len(nsfw_posts)-1)]
                image_url = post['file']['url']
                await message.channel.send(image_url)
            else:
                await message.channel.send('No NSFW image found')
        else:
            await message.channel.send('An error occurred')

    elif message.content.startswith('!booru'):
        search_query = message.content[7:]
        url = 'https://booru.allthefallen.moe/post/index.json?limit=30&tags=' + search_query
        response = requests.get(url)
        data = json.loads(response.text)
        nsfw_posts = [post for post in data if 'file_url' in post and post['rating'] == 'e']
        if len(nsfw_posts) > 0:
            post = nsfw_posts[random.randint(0, len(nsfw_posts)-1)]
            image_url = post['file_url']
            await message.channel.send(image_url)
        else:
            await message.channel.send('No NSFW image found')

client.run('MTA4NDM0OTc5NjA3NDEyNzQzMA.GKvpvK.EgYXslb8fb-VgRIuaDITr7Ql0lD7NR0VHZzo_I')