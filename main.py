import settings
from nonosearch import TrieNode, insert_trie, check_present, darnReplace
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")
def run():
    root = TrieNode()
    with open("nono.txt", "r") as file:
        for word in file:
            insert_trie(root, word.strip())
    
    darnified_users = []
    def check_Darnified(ctx):
        if (ctx.author.id) in darnified_users:
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
            deleteflag = False
            msg = message.content.split()
            updated_words = []
            for word in msg:
                if check_present(root, word):
                    updated_word = darnReplace(word)
                    deleteflag = True
                else:
                    updated_word = word
                updated_words.append(updated_word)
                    
            if deleteflag:
                updated_msg = ' '.join(updated_words)
                await message.delete()
                await message.channel.send(f"{message.author} says: {updated_msg}")
        
    @bot.command()
    async def darnify(ctx, user:discord.Member=None, level = 1):
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
        
    

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

     
if __name__ == "__main__":
    run()