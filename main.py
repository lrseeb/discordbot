from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
import asyncio

from responses import question_handler
from results import result

# Loading our token from somewhere safe
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Bot setup
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)

# Global variable to track whether the bot should be listening for messages
listening_for_trivia: bool = False


# Handling the startup for our bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# Handling incoming messages
@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return
    
    if message.content.startswith('-t'):

        await message.channel.send('Halutko pelata trivia peliä ? :DD (y/e)')

        global listening_for_trivia
        
        username: str = str(message.author)
        user_message: str = message.content
        channel: str = str(message.channel)

        print(f'[{channel}] {username}: "{user_message}"')

    if message.content.startswith('y'):
            
            await message.channel.send('Valitse kategoria (Kirjoita vain numero (1-6)):\n1. Maantieto\n2. Viihde\n3. Historia\n4. Kirjallisuus ja taide\n5. Tiede ja luonto\n6. Urheilu ja vapaa-aika')

            try:
                response = await client.wait_for('message', timeout=900.0, check=lambda m: m.author == message.author)
                category_choice = int(response.content.strip())
                
                kysymys, vastaus = question_handler(category_choice)
                await message.channel.send(f'{kysymys}\nVastaa vain kirjaimin (a-d)')
                print(kysymys)
                print("tämä on vastaus =", vastaus)

                def check(m):
                    return m.author == message.author and m.content.isalpha()
                    
                try:
                    guess = await client.wait_for('message', check=check, timeout=900.0)
                except asyncio.TimeoutError:
                    await message.channel.send('Sorry, aika kului loppuun :(')
                    await client.http.connector.close()
                    await client.close()
                    
                if str(guess.content) == vastaus:
                    oikein = result.get(category_choice)
                    result[category_choice] = oikein + 1 
                    print(result)

                    if all(score >= 1 for score in result.values()):
                        await message.channel.send('Yay, voitit "pelin", eli olet vastannut oikein ainakin yhteen kysymykseen jokaisesta kategoriasta!\nHaluatko silti jatkaa ? :0 (y/n)')
                    else:
                        await message.channel.send('Oikein!\nHaluatko jatkaa peliä? (y/n)')

                elif str(guess.content) != vastaus:
                    await message.channel.send(f'nah, oikea vastaus olisi ollut {vastaus}\nHaluatko jatkaa peliä? (y/n)')
                
            except asyncio.TimeoutError:
                await message.channel.send('Sorry, aika kului loppuun :(')
                await client.http.connector.close()
                await client.close()

    elif message.content.startswith('n'):
        await message.channel.send('Heipähei!')
        print('lopetus')
        await client.http.connector.close()
        await client.close()
            

# STEP 5: Main entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__== '__main__':
    main()
