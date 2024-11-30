import discord


class BaseEmbed(discord.Embed):
    FOOTER_TEXT = 'Hype Squad Studios stands with the LGBTQIA+ community.'
    FOOTER_ICON = 'https://utfs.io/f/oVjEq7vmvrGsVXCEnu3gkl7wPpJdGaX29EzcosfO4BL3YD8x'
    
    def __init__(self, title: str, description: str, color: int = 0x5865F2) -> None:  # Discord blurple
        super().__init__(title=title, description=description, color=color)
        self.set_footer(text=self.FOOTER_TEXT, icon_url=self.FOOTER_ICON)


class WelcomeEmbed(BaseEmbed):
    BANNER_IMAGE = 'https://utfs.io/f/oVjEq7vmvrGsWBr7tUjMCPyLIBe7OJUp21rs5ETXn9ZfQgwx'
    FOUNDER_ICON = 'https://utfs.io/f/oVjEq7vmvrGsaJExa6yFZ2Sl9dEI587GFsnKg6buxkqPUm4f'

    def __init__(self) -> None:
        super().__init__(
            title='Welcome to Hype Squad Studios!',
            description='Please see our <#1292486286522716180> channel for more information about our organization. Also, please do familiarize yourself with our <#1292455806779916489>.'
        )
        self.set_image(url=self.BANNER_IMAGE)
        
        # More descriptive field names and organized structure
        self.add_field(
            name='❓ Questions?',
            value='Before asking a question, please see if it has already been answered in the <#1292486781987586108> section.',
            inline=False,
        )
        self.add_field(
            name='🤝 Join Us',
            value='If you are interested in joining Hype Squad Studios, please see <#858404365852606494> for the rules.',
            inline=False,
        )
        self.add_field(name='👋 Welcome', value='Thank you and enjoy your stay.', inline=False)
        
        self.set_author(
            name="Trenton Sergeant, Founder",
            icon_url=self.FOUNDER_ICON,
        )
