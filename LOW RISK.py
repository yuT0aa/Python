
import discord  # Import the discord.py library

# Define the intents your bot needs
intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent
intents.guilds = True  # Enable guilds intent (for server-related events)
intents.messages = True  # Enable messages intent

client = discord.Client(intents=intents)  # Create the client with intents

# Event: When the bot is ready and connected
async def on_ready():
    print(f'The bot is online and ready! Logged in as {client.user}.')  # Updated print statement

# Event: When a message is sent in a channel
async def on_message(message):
    if message.author == client.user:  # Ignore messages from the bot itself
        return
    
    if message.content.startswith('!'):  # Check if the message starts with '!'
        args = message.content[1:].strip().split()  # Split the message into command and arguments
        command = args[0].lower()  # Get the first word as the command
        
        if command == 'ping':
            await message.channel.send('Pong!')  # Reply to the channel
        elif command == 'hello':
            await message.reply('Hello! How can I help you?')  # Reply directly to the user
        else:
            await message.channel.send('Unknown command. Try !ping or !hello.')  # Handle unknown commands

# Register the events
client.event(on_ready)  # Register the on_ready event
client.event(on_message)  # Register the on_message event

# Run the bot with your token
client.run('bot_token')  # Replace with your actual bot token
# Note: Keep your bot token secure and do not share it publicly.






