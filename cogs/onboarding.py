import discord

from discord.ext import commands

from hypebot import HypeSquad


class onboarding(commands.Cog):
    def __init__(self, bot: HypeSquad) -> None:
        self.bot = bot

    @commands.command(name='onb-welcome')
    async def onboarding_welcome(self, ctx: commands.Context) -> None:
        embed = discord.Embed(
            title='Welcome to Rainier Guard!',
            description='We are a VATSIM Special Operations Partner that primarily simulates search and rescue, disaster response, and medivac missions. We also support ATC by providing an alert mission. We are not in any was affiliated with any real world agencies or organizations. Nor do we support any operations or activies that any real world agencies or organizations may be involved in.',
        )
        embed.set_image(url='https://utfs.io/f/oVjEq7vmvrGsWBr7tUjMCPyLIBe7OJUp21rs5ETXn9ZfQgwx')
        embed.add_field(
            name='',
            value='In order to access our Discord or other services, you must agree to our discord policy which can be found on our website or by going to the <#1292455806779916489> channel. You also agree to our privacy policy which can be found on our website https://www.rainierguard.org/',
            inline=False,
        )
        embed.add_field(
            name='',
            value='If you are interested in joining Rainier Guard, please see <#1299550819477225473> for more information.',
            inline=False,
        )
        embed.add_field(name='', value='Thank you and enjoy your stay.', inline=False)
        embed.set_author(
            name="Ellie 'Coug' Reed, Commanding Officer",
            icon_url='https://utfs.io/f/oVjEq7vmvrGsaJExa6yFZ2Sl9dEI587GFsnKg6buxkqPUm4f',
        )
        embed.set_footer(
            text='Rainier Guard stands with the LGBTQIA+ community.',
            icon_url='https://utfs.io/f/oVjEq7vmvrGsVXCEnu3gkl7wPpJdGaX29EzcosfO4BL3YD8x',
        )
        await ctx.send(embed=embed)
    @commands.command(name='onb-rules-1')
    async def onboarding_rules_1(self, ctx: commands.Context) -> None:
        embed = discord.Embed(
            title='Rainier Guard Discord Policy v1.0',
            description='',
        )
        embed.add_field(
            name='1. PURPOSE',
            value='This document contains rules and regulations governing access to and appropriate use of the Rainier Guard ("RAI") Discord Server ("Discord").',
            inline=False,
        )
        embed.add_field(
            name='2. ROLES AND RESPONSIBILITIES',
            value='The Office of Primary Responsibility (OPR) for this policy is the Officer of the Commanding Officer. This policy shall be maintained, revised, updated or canceled by the Rainier Guard Commanding Officer',
            inline=False,
        )
        embed.add_field(
            name='3. DISTRIBUTION',
            value='Rainier Guard members, visitors, or guests using or wishing to use the RAI Discord.',
            inline=False,
        )
        await ctx.send(embed=embed)
    @commands.command(name='onb-rules-2')
    async def onboarding_rules_2(self, ctx: commands.Context) -> None:
        embed = discord.Embed(
            title='',
            description='',
        )
        embed.add_field(
            name='4. DEFINITIONS',
            value='1. “Bot” - Any software that connects to Discord and has the ability to execute preprogrammed commands, reply to messages, or play music.\n 2. “Record” - Using any external program (streaming software, audio recording software, etc.) to capture audio from Discord and subsequently rebroadcast or store information.\n 3. RAI Senior Staff members include the Commanding Officer (CO), Executive Officer (XO), the Public Affairs Officer (PAO), the Training Officer (TO), and the Information Systems Officer (ISO).',
            inline=False,
        )
        embed.add_field(
            name='5. CODE OF CONDUCT',
            value='1. The RAI Discord is an inclusive environment intended for RAI members, visitors, staff, and guests. All members should be courteous and respectful to each other.\n 2. When connecting to Discord, your nickname must comply with the following format (at a minimum): “[first name] [pronouns)]” Example: Ellie (She/Her)\n 3a. Anyone wishing to stream to an external location (such as Twitch, Youtube, etc.) must obtain consent from everyone present in the channel prior to going live. They must also mark themselves as streaming.\n Example 1: “Live/Twitch - Ellie (She/Her)”\n Example 2: “Live/YouTube - Ellie (She/Her)”\n 3b. Anyone wishing to record at any time must obtain consent from all parties and mark themselves as “recording.”\n Example: “Recording - Ellie (She/Her)”\n 4. The Discord text and voice rooms shall be utilized per the channel name/description.',
            inline=False,
        )
        embed.add_field(
            name='',
            value='3b. Anyone wishing to record at any time must obtain consent from all parties and mark themselves as “recording.”\n Example: “Recording - Ellie (She/Her)”\n 4. The Discord text and voice rooms shall be utilized per the channel name/description.',
            inline=False,
        )
        embed.set_footer(
            text='Rainier Guard stands with the LGBTQIA+ community.',
            icon_url='https://utfs.io/f/oVjEq7vmvrGsVXCEnu3gkl7wPpJdGaX29EzcosfO4BL3YD8x',
        )
        await ctx.send(embed=embed)


async def setup(bot: HypeSquad) -> None:
    await bot.add_cog(onboarding(bot), guild=bot.home_guild)
