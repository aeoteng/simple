import os
from keep_alive import keep_alive
from discord.ext import commands

bot = commands.Bot(
	command_prefix="!",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 486086967411474433  # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier


extensions = [
	'cogs.cog_example',
    'cogs.api_pat',
    'cogs.api_kpop',
    'cogs.api_wink'
    # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('> Please use required args or check in **help**')

    elif isinstance(error, commands.CommandNotFound):
        await ctx.send('> Invalid or Unavailable Command')

keep_alive()  # Starts a webserver to be pinged.
my_secret = os.environ['TOKEN']
bot.run(my_secret)  # Starts the bot