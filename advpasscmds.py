# cogs/advpasscmds.py
import discord
from discord.ext import commands

class AdvPassCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='advpasscmds')
    async def advpasscmds(self, ctx):
        embed = discord.Embed(title="Advanced Pass Commands", color=0x00ff00)
        embed.set_author(name="Brezel • AdvPass")
        embed.set_footer(text="Brezel Bot〢since 2024")

        user_commands = [
            ("!advpasslevel", "Zeigt das aktuelle Level des Nutzers an."),
            ("!advpass", "Zeigt die Belohnungen und ihre Level für die aktuelle Saison an.")
        ]

        admin_commands = [
            ("!advpasskanal #KANAL", "Setzt den Kanal für Belohnungs- und Level-Up-Benachrichtigungen."),
            ("!ap_setgiftnormal Belohnung1, Belohnung2, Belohnung3", "Setzt Belohnungen für den normalen Pass bei Level 5, 10, 15 usw."),
            ("!ap_setgiftvip Belohnung1, Belohnung2, Belohnung3", "Setzt Belohnungen für den VIP-Pass bei Level 2, 4, 6 usw."),
            ("!advpass_newseason", "Startet eine neue Saison und setzt alle Nutzer-Daten zurück."),
            ("!ap_reset @USER", "Setzt die Daten eines spezifischen Nutzers zurück."),
            ("!ap_reset @ALL", "Setzt die Daten aller Nutzer im Server zurück.")
        ]

        for name, value in user_commands:
            embed.add_field(name=name, value=value, inline=False)

        embed.add_field(name="\u200b", value="\u200b", inline=False)  # Spacer zwischen User- und Admin-Befehlen

        for name, value in admin_commands:
            embed.add_field(name=name, value=value, inline=False)

        await ctx.send(embed=embed)

async def setup(bot):

    await bot.add_cog(AdvPassCommands(bot))