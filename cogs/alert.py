import discord

from discord.ext import commands
from discord import app_commands

from hypebot import HypeSquad


class Alert(commands.Cog):
    def __init__(self, bot: HypeSquad) -> None:
        self.bot = bot

    @app_commands.command(
        name='alert',
        description='Alert staff that you need assistance'
    )
    @app_commands.describe(
        location='Where you need assistance',
        reason='Why you need assistance'
    )
    async def alert(self, interaction: discord.Interaction, location: str, reason: str) -> None:
        # Send ephemeral confirmation to user
        await interaction.response.send_message(
            'Staff has been notified. Someone will assist you shortly.',
            ephemeral=True
        )
        
        # Send alert to staff channel
        staff_channel = self.bot.get_channel(1161725747908587602)  # Replace with your staff channel ID
        await staff_channel.send(
            f'🚨 **ALERT:** {interaction.user.mention} needs assistance!\n'
            f'📍 **Location:** {location}\n'
            f'❓ **Reason:** {reason}'
        )


async def setup(bot: HypeSquad) -> None:
    await bot.add_cog(Alert(bot), guild=bot.home_guild)
