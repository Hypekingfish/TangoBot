import discord
import logging

from discord.ext.commands import (
    NoEntryPointError,
)
from discord.ext import commands  # ! commands
from discord import app_commands  # slash commands
from rich.logging import RichHandler
from pathlib import Path

FORMAT = '[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s'
file_handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
rich_handler = RichHandler(show_path=True, show_time=True, show_level=True, markup=True)
logging.basicConfig(
    level='NOTSET',
    format=FORMAT,
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[rich_handler, file_handler],
)


# Start of slash commands
class HypeSquadCommandTree(app_commands.CommandTree):
    async def interaction_check(self, interaction: discord.Interaction, /) -> bool:
        return True


# Normal commands
class HypeSquad(commands.Bot):
    def __init__(self, sync: bool = False) -> None:
        super().__init__(
            command_prefix='!',
            intents=discord.Intents.all(),
            tree_cls=HypeSquadCommandTree,
        )
        self.sync = sync
        self.logger = logging.getLogger('hypebot')
        self.logger.info(f'Starting HypeSquad with: sync={sync}')
        self.home_guild = discord.Object(id=1161725747476566027)

    async def _sync(self) -> None:
        if self.sync:
            self.logger.info('Syncing the bot...')
            await self.tree.sync(guild=self.home_guild)
            print("Commands synced")

    async def _load_cogs(self) -> None:
        self.logger.info('Loading cogs...')
        cog_dir = Path.cwd() / 'cogs'
        for cog in cog_dir.glob('*.py'):
            try:
                self.logger.info(f'Loading {cog.stem}')
                await self.load_extension(f'cogs.{cog.stem}')
            except NoEntryPointError:
                self.logger.error(f'No entry point found in {cog.stem}')

        self.logger.info('Cogs loaded!')

    async def setup_hook(self) -> None:
        await self._load_cogs()
        await self._sync()
        self.logger.info('HypeBot is ready!')