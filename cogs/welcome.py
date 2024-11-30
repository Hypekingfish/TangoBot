import discord
from discord.ext import commands
from hypebot import HypeSquad

class WelcomeEmbed(discord.Embed):
    """Welcome embed that's sent when new members join"""
    def __init__(self):
        super().__init__(
            title='Welcome to HypeSquad! 🎉',
            description='Thanks for joining our community! Here\'s some information to help you get started.',
            color=discord.Color.blue()
        )
        
        self.add_field(
            name='📜 Rules',
            value='Please make sure to read our server rules in <#rules-channel-id>',
            inline=False,
        )
        self.add_field(
            name='🎮 Getting Started',
            value='• Introduce yourself in <#introductions-channel-id>\n'
                  '• Get your roles in <#roles-channel-id>\n'
                  '• Check out our channels and have fun!',
            inline=False,
        )
        self.add_field(
            name='❓ Need Help?',
            value='Feel free to ask questions in <#help-channel-id> or contact our moderators!',
            inline=False
        )
        self.set_footer(
            text='Welcome to the community!',
            icon_url='https://your-server-icon-url.png'  # Optional: Add your server's icon URL
        )

class Welcome(commands.Cog):
    def __init__(self, bot: HypeSquad) -> None:
        self.bot = bot

    @commands.command(
        name='welcome',
        aliases=['wel', 'start', 'info'],
        help='Shows the server welcome message and information'
    )
    async def welcome(self, ctx: commands.Context) -> None:
        """Sends the welcome embed when command is used"""
        await ctx.send(embed=WelcomeEmbed())

async def setup(bot: HypeSquad) -> None:
    await bot.add_cog(Welcome(bot), guild=bot.home_guild)
