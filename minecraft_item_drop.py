import discord
import random
import asyncio
import aiohttp

CHANNEL_ID = # Your Discord Channel id of DiscordSRV console
PASTEBIN_RAW_URL = 'https://pastebin.com/raw/'  # replace xxxxxxxx with your paste ID

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def give_item(max_amount=1):
    await client.wait_until_ready()
    while not client.is_closed():
        async with aiohttp.ClientSession() as session:
            async with session.get(PASTEBIN_RAW_URL) as resp:
                item_data = await resp.text()
        items = item_data.strip().split('\n')
        item = random.choice(items)
        amount = random.randint(1, max_amount)
        command = f'give @r {item} {amount}'
        await client.get_channel(CHANNEL_ID).send(command)
        await asyncio.sleep(30) # wait for 30 seconds
        kill_command = 'kill @e[type=item]'
        await client.get_channel(CHANNEL_ID).send(kill_command)
        await asyncio.sleep(1) # wait for 1 second before generating next item

@client.event
async def on_ready():
    print('Bot is ready!')
    client.loop.create_task(give_item(max_amount=64))

client.run('bot_token')
