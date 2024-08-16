import settings
import re
from nono import nono_words_mapping
from nonosearch import TrieNode, Trie, darn_replace
import discord
from discord.ext import commands



logger = settings.logging.getLogger("bot")
def run():
    
    darnified_users = []

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

    @bot.event
    async def on_message(message):
        await bot.process_commands(message)
        if message.author == bot.user:
            return
        
        if str(message.author.id) in darnified_users:
            msg = message.content
            delete_flag = False

            for pattern, darn_variation in nono_words_mapping.items():
                new_msg, num_replacements = re.subn(pattern, darn_variation, msg, flags=re.IGNORECASE)
                if num_replacements > 0:
                    delete_flag = True
                    msg = new_msg
            if delete_flag:
                await message.delete()
                await message.channel.send(f"{message.author.display_name} says: {msg}")
            
    
    # Add user to censorship (darnified) list
    @bot.command(
            help = "Adds the specified user to the darnify list. Any swear "
            + "words sent by users in this list will be censored with \"darn\".",
            brief = "Censors the specified user."
    )
    async def darnify(ctx, user:discord.Member=
                      commands.parameter(default=None, description="%USERNAME%")):
        if user == None:
            await ctx.send("Please provide a user to Darnify.")
            return
        
        # check if user is already in darnified_users[]
        def is_Darnified(user_id):
            if str(user_id) in darnified_users:
                return True
            else:
                return False
            
        # Add user to darnified users
        def add_Darnified(user_id):
            darnified_users.append(str(user_id))

        if is_Darnified(user.id) == True:
            await ctx.send(f"The user {user.display_name} has already been Darnified.")
        else:
            add_Darnified(user.id)
            await ctx.send(f"{user.display_name} has been Darnified.")

    # Remove user from censorship (darnified) list
    @bot.command(
            help = "Removes specified user from the darnify list. Swear words"
            + " sent by the user will send as normal.",
            brief = "Uncensored the specified user."
    )
    async def undarnify(ctx, user:discord.Member=
                        commands.parameter(default=None, description="%USERNAME%")):
        if user == None:
            await ctx.send("Please provide a user to UnDarnify.")
            return
        
        # check if user is in darnified_users[]
        def is_Darnified(user_id):
            if str(user_id) in darnified_users:
                return True
            else:
                return False
            
        # remove user from darnified_users
        def remove_Darnified(user_id):
            darnified_users.remove(str(user_id))

        if is_Darnified(user.id) == False:
            await ctx.send(f"The user {user.display_name} is not Darnified.")
        else:
            remove_Darnified(user.id)
            await ctx.send(f"{user.display_name} has been UnDarnified.")

    @undarnify.error
    async def undarnify_error(ctx, error):
        if isinstance(error, commands.MemberNotFound):
            if error.argument == "all":
                ...
                # x = ctx.guild.members
                # for member in x:
                #     print(member.name)
                
    
    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

     
if __name__ == "__main__":
    run()