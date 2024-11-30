import traceback

import discord

from discord import Member

from discord.ext.commands import (
    Cog,
)

from discord.ext import commands

from embeds import WelcomeEmbed
from hypebot import HypeSquad

from discord import Interaction
from discord.app_commands import AppCommandError


class Core(commands.Cog):
    """Core bot functionality, statistics, and backend work."""

    def __init__(self, bot: HypeSquad) -> None:
        self.bot: HypeSquad = bot

    @Cog.listener()
    async def on_ready(self) -> None:
        self.bot.logger.info('HypeBot online.')

    @Cog.listener()
    async def on_disconnect(self) -> None:
        self.bot.logger.info('Disconnected')

    @Cog.listener()
    async def on_resumed(self) -> None:
        self.bot.logger.info('Reconnected')


    @Cog.listener()
    async def on_member_join(self, member: Member) -> None:
        """Auto welcome message listener. Sends a message to #general with the embed from welcome.py"""
        channel = discord.utils.get(member.guild.text_channels, name='general')
        
        if channel is None:
            # Log error or notify that channel wasn't found
            print(f"Error: Could not find 'general' channel in {member.guild.name}")
            return
        
        try:
            await channel.send(f'{member.mention} has joined the server!')
            await channel.send(embed=WelcomeEmbed())
        except discord.Forbidden:
            print(f"Error: Bot doesn't have permission to send messages in general")
        except Exception as e:
            print(f"Error sending welcome message: {str(e)}")


    @Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: Exception) -> None:
        if ctx.command:
            command = ctx.command.name
            self.bot.logger.error(f'command:{command}\nerror:{error}')

        if isinstance(error, commands.CommandNotFound):
            msg = 'That command was not found, please check `/help`.'
            await ctx.send(msg)

        elif isinstance(error, commands.MissingRole):
            msg = f'You do not have the role(s) needed to use this command.\n{error}'
            await ctx.send(msg)

        elif isinstance(error, commands.CommandOnCooldown):
            msg = f'This command is on cooldown for {error.retry_after}s.'
            await ctx.send(msg)
        else:
            msg = 'An error occured, please check `/help`.'
            await ctx.send(msg)
            self.bot.logger.error(error.with_traceback(error.__traceback__))
            self.bot.logger.error(traceback.format_exc())

    @Cog.listener()
    async def on_app_command_error(self, interaction: Interaction, error: AppCommandError) -> None:
        """Handles errors for all application commands."""
        command = interaction.command.name

        self.bot.logger.error(f'Command: {command} error!')
        self.bot.logger.error(error)
        self.bot.logger.error(error.__traceback__)


async def setup(bot: HypeSquad) -> None:
    await bot.add_cog(Core(bot), guild=bot.home_guild)
