import discord
import responses


COMMAND_PREFIX = "."


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

    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now up and running!")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said '{user_message}' in {channel}")

        if user_message[0] == COMMAND_PREFIX:
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True, channel=channel)
        else:
            await send_message(message, user_message, is_private=False, channel=channel)

    client.run(TOKEN)

