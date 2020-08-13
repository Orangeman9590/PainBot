import discord
from discord.ext import commands, tasks
import random
import os

quotes = ['💀"Sometimes you must hurt in order to know, fall in order to grow, lose in order to gain because lifes greatest lessons are learned through pain."💀',
          '💀"Even the most ignorant, innocent child will eventually grow up as they learn what true pain is. It affects what they say, what they think… and they become real people."💀',
          '💀"Religion, ideology, resources, land, spite, love or just because. No matter how pathetic the reason, its enough to start a war."💀',
          '💀"Justice comes from vengeance, but that justice only breeds more vengeance."💀',
          '💀"Feel pain, think about pain, accept pain, know pain... Shinra Tensei!"💀',
          '💀"We are but men, drawn to act in the name of revenge that we deem to be justice. But... if there is justice in revenge then that same justice will breed only more revenge... and trigger a cycle of hatred."💀',
          '💀"Love breeds sacrifice... which in turn breeds hatred. Then you can know pain."💀',
          '💀"Even innocent foolish children will grow up in the face of pain, until their thoughts and beliefs are the same as their doubts."💀',
          '💀"Even children are forced to grow up in the face of pain."💀',
          '💀"Human nature pursues strife."💀',
          '💀"Pain is the way to bring peace."💀']


WUR = ['Sleep With Worms Or Bathe With Cockroaches',
       'Would you rather eat cat poop for a year OR eat cow patty for a year',
       'Would you rather use boiling water as eye drops or gargle with hot sauce?',
       'Would you rather be a tissue paper OR toilet paper',
       'Would you rather rip your favorite shirt OR your dirty ass butthole',
       'What do you prefer vomit cactus OR shit cactus',
       'Would you rather suck a fart out of a butthole with a straw OR drink cat piss',
       'Would you rather slowly shove a needle into one of your eyes or have your skin peeled off with a carrot peeler',
       'Would you rather lick a dogs butt OR lick a homeless person’s waxy ear']

coin = ['Heads👦', 'Tails🦨']

class Ext(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.idle, activity=discord.Game('Destroying The Leaf Village'))
        print('RUNNING')

    @commands.Cog.listener()
    async def on_member_join(self,member) :
        channel = self.client.get_channel(729920503502077992)
        guild = member.guild
        message = 'Hello {}, Welcome to {} Discord server'.format(member.mention, guild.name)
        await channel.send(message)
    @commands.Cog.listener()
    async def on_member_remove(self,member) :
        channel = self.client.get_channel(729920503502077992)
        message = 'Goodbye {}, We are not sad to see you go'.format(member.mention)
        await channel.send(message)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.channel.send('Command Not Found')



    @commands.command()
    async def ping(self, ctx):
        await ctx.channel.send(f'Pong {round(self.client.latency * 1000)}ms')

    @commands.command()
    async def pain(self,ctx) :
        embedVar = discord.Embed(title="🔥𝓣𝓱𝓮 𝓦𝓸𝓻𝓵𝓭 𝓢𝓱𝓪𝓵𝓵 𝓚𝓷𝓸𝔀 𝓟𝓪𝓲𝓷🔥", color=0xff7400)
        embedVar.add_field(name="?quote", value="Sends random quote by Pain", inline=False)
        embedVar.add_field(name="?ping", value="Tests latency from bot to server", inline=False)
        embedVar.add_field(name="?flipcoin", value="Flips a coin, 50/50", inline=False)
        embedVar.add_field(name="?playWUR", value="Plays Would You Rather", inline=False)
        await ctx.channel.send(embed=embedVar)

    @commands.command()
    async def flipcoin(self,ctx) :
        await ctx.channel.send(random.choice(coin))

    @commands.command()
    async def quote(self,ctx) :
        await ctx.channel.send(random.choice(quotes))

    @commands.command()
    async def playWUR(self,ctx) :
        embedVa = discord.Embed(title="Would you rather?", color=0xff7400)
        embedVa.add_field(name=random.choice(WUR), value='?_1 or ?_2', inline=False)
        await ctx.channel.send(embed=embedVa)

    @commands.command()
    async def _1(self,ctx) :
        embedVa = discord.Embed(title="Would you rather?", color=0xff7400)
        embedVa.add_field(name=random.choice(WUR), value='?_1 or ?_2', inline=False)
        await ctx.channel.send(embed=embedVa)

    @commands.command()
    async def _2(self,ctx) :
        embedVa = discord.Embed(title="Would you rather?", color=0xff7400)
        embedVa.add_field(name=random.choice(WUR), value='?_1 or ?_2', inline=False)
        await ctx.channel.send(embed=embedVa)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx, amount=5) :
        await ctx.channel.purge(limit=amount)



def setup(client):
    client.add_cog(Ext(client))
