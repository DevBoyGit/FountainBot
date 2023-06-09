import discord
import responses


async def send_message(message, user_message, channel, is_private):
    try:
        response = responses.handle_response(message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def execute_bot():
    TOKEN = ""
    with open("TOKEN.txt", "r") as token:
        TOKEN = token.readline()

    client = discord.Client()

    @client.event
    async def on_ready():
        print(f"{client.user} is now up and running!")

    client.run(TOKEN)

