# Darninator

## A unique chat censorship bot for Discord

## Description
The Darninator bot attempts match words that any users send in a message, with a long list of swear words. However, instead of only deleting the message and giving the user a warning, the Darninator will first alter the swear word to some variation of "darn" based on a set of rules, send this variation to the respective channel, and delete the original message. For example:

> User1: It's ****ing hot out today, I'm sweating my ****ing ***s off in my room.\
> Darninator: User1 says: It's darning hot out today, I'm sweating my darning darn off in my room.

Of course, User1 would have said the actual words without asterisks in order for the Darninator to intervene.

## Installation
This bot is not properly hosted at the moment, and is therefore private. Check back soon for installation instructions.

## Usage
At the moment, the Darninator will not alter any messages other than those sent by "darnified" users. To darnify a user, type the command: `!darnify user1' , and then any message will be scanned for words listed under "nonowords.txt". I plan to change this in the future, so that all users can be "darnified" by one single command.

## Support
To be posted

## Roadmap
Here is the general outline for future changes:
* Fix known issues
    * Since Discord automatically replaces emoticons with the emoji equivalent, this will cause an error, as the character is "out of range."
    * If a word that would match normally has extra characters, it will not be replaced properly
* Change "Moderator" list so that specific roles will automatically be able to change functionality. The owner and users with administrative roles will be able to darnify all users in the respective server with a single command.
* Add an extreme version of darnification
    * It's possible to circumvent the darnification by using non-standard characters. Therefore, I plan to implement an extreme version of `!darnify`, where any user specified will have *every* word they send changed to some variation of darn. For example, "table" will become "darnble", etc.
* Properly host the bot on my own server
    * Before this is properly made public, I need to find a way to host the bot without wasting my PC's resources 24/7. After this is issue is fixed, the bot will be able to go public.
* Add manual entries, accessed by typing `!help`

## License
None

## Project status
Active
