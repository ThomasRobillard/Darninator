import settings
from nonosearch import TrieNode, Trie, darn_replace
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")
def run():
    root = Trie()
    with open("nono.txt", "r") as file:
        for word in file:
            root.insert_trie(word.strip())
    


    # check if Moderators.txt exists, if not, create it
    try:
        with open('Moderators.txt', 'x') as file:
            file.close
    except FileExistsError:
        ...
    
    darnified_users = []
    def check_Mod(ctx):
        with open('Moderators.txt') as f:
            if str(ctx.author.id) in f.read():
                return ctx.author.id

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
            matches = []
            msg = message.content
            matches = root.check_present(msg)
            
            if matches:
                updated_msg = darn_replace(msg, root)
                await message.delete()
                await message.channel.send(f"{message.author} says: {updated_msg}")
    
    # Add user to censorship (darnified) list
    @bot.command()
    @commands.check(check_Mod)
    async def darnify(ctx, user:discord.Member=None):
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
            await ctx.send(f"The user {user} has already been Darnified.")
        else:
            add_Darnified(user.id)
            await ctx.send(f"{user} has been Darnified.")

    # Remove user from censorship (darnified) list
    @bot.command()
    @commands.check(check_Mod)
    async def undarnify(ctx, user:discord.Member=None):
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
            await ctx.send(f"The user {user} is not Darnified.")
        else:
            remove_Darnified(user.id)
            await ctx.send(f"{user} has been UnDarnified.")
    
    # Add to mod list
    @bot.command()
    @commands.check(check_Mod)
    async def addmod(ctx, user:discord.Member=None):
        if user == None:
            await ctx.send("Please provide a user to add to the Moderator list.")
            return
        
        # check if user is already in mod list
        def is_Moderator(user_id):
            with open('Moderators.txt', 'r') as f:
                if str(user_id) in f.read():
                    return True
                else:
                    return False
            
        # Add user to mod list
        def add_Moderator(user_id):
            with open('Moderators.txt', 'a') as f:
                f.write(f"{str(user_id)}\n")
                f.close()

        if is_Moderator(user.id) == True:
            await ctx.send(f"The user {user} is already a Moderator.")
        else:
            add_Moderator(user.id)
            await ctx.send(f"{user} has been added to Moderator list.")

    # Remove from mod list
    @bot.command()
    @commands.check(check_Mod)
    async def removemod(ctx, user:discord.Member=None):
        if user == None:
            await ctx.send("Please provide a user to remove from the Moderator list.")
            return
        
        # check if user is in mod list
        def is_Moderator(user_id):
            with open('Moderators.txt', 'r') as f:
                if str(user_id) in f.read():
                    return True
                else:
                    return False
            
        # remove user from mod list
        def remove_Moderator(user_id):
            with open('Moderators.txt', 'r') as f:
                content = f.read()
                updated_content = content.replace(str(user_id), '')
            with open('Moderators.txt', 'w') as f:
                f.write(updated_content)

                
        if is_Moderator(user.id) == False:
            await ctx.send(f"The user {user} is not a Moderator.")
        else:
            remove_Moderator(user.id)
            await ctx.send(f"{user} has been removed from Moderator list.")
    

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

     
if __name__ == "__main__":
    run()