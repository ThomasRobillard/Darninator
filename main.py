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

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
             
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
        

    

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

     
if __name__ == "__main__":
    run()