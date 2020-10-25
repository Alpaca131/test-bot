import discord

client = discord.Client()
TOKEN = 'NzY5NTY2MDE1ODA5OTEyODMz.X5Q4NA.-O-1cHbBc1C-FJlbwJ4Q8-1vQ4I'

"""
TOKENがここ(https://teratail.com/questions/300166)から漏れています。
Botを乗っ取られるので、今すぐ変更して下さい。
"""


@client.event
async def on_ready():
    print('Ready')


client.run(TOKEN)
