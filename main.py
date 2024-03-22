from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message

from responses import get_response, got_response

# STEP 0: Loading our token from somewhere safe
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# STEP 1: Bot setup
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)

# Global variable to track whether the bot should be listening for messages
listening_for_trivia: bool = False

# STEP 2: Message functionality
async def send_message(message: Message, user_message: str) -> None:
    global listening_for_trivia
    
    if not user_message:
        print('(Message NULL)')
        return
    
    if is_private := user_message.startswith('?'):
        user_message = user_message[1:]
        
    try:
        if user_message == '-t':
            listening_for_trivia = True
            response: str = get_response(user_message)
            await message.channel.send(response)
        elif listening_for_trivia:
            response: str = got_response(user_message)
            await message.channel.send(response)
        else:
            response: str = get_response(user_message)
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# STEP 3: Handling the startup for our bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# STEP 4: Handling incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    global listening_for_trivia
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

# STEP 5: Main entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__== '__main__':
    main()
