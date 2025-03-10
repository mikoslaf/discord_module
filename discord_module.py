import requests
import dotenv
import os
import discord

class discord_Webhooks:
    
    def __init__(self, webhook_link: str) -> None:
        self.webhook_link = webhook_link

    def send_message(self, content: str) -> int:
        return requests.post(self.webhook_link, json = {"content": content})
    
    def get_webhook_link(self) -> str:
        return requests.get(self.webhook_link)

    def send_basic_embed(self, title: str, description: str, color: str) -> int:
        embed_data = {
            "title": title, 
            "description": description, 
            "color": color 
            }
        return requests.post(self.webhook_link, json = {"embeds": [embed_data]})
    
class discord_bot:
    
    def __init__(self, token: str) -> None:
        self.client = discord.Client(intents=discord.Intents.all())
        self.client.run(token)

    def get_client(self) -> discord.Client:
        return self.client

    def get_guilds(self) -> list:
        return self.client.guilds

    def get_guild(self, guild_id: int) -> discord.Guild:
        return self.client.get_guild(guild_id)

    def get_channels(self, guild: discord.Guild) -> list:
        return guild.channels

    def get_channel(self, guild: discord.Guild, channel_id: int) -> discord.TextChannel:
        return guild.get_channel(channel_id)

    def get_messages(self, channel: discord.TextChannel) -> list:
        return channel.history(limit = 200).flatten()

    def get_message(self, channel: discord.TextChannel, message_id: int) -> discord.Message:
        return channel.fetch_message(message_id)

    def send_message(self, channel: discord.TextChannel, content: str) -> discord.Message:
        return channel.send(content)

    def send_embed(self, channel: discord.TextChannel, title: str, description: str, color: str) -> discord.Message:
        embed = discord.Embed(title = title, description = description, color = color)
        return channel.send(embed = embed)

    def send_file(self, channel: discord.TextChannel, file_path: str) -> discord.Message:
        return channel.send(file = discord.File(file_path))

    def send_embed_file(self, channel: discord.TextChannel, title: str, description: str, color: str, file_path: str) -> discord.Message:
        embed = discord.Embed(title = title, description = description, color = color)
        return channel.send(embed = embed, file = discord.File(file_path))

    def get_user(self, user_id: int) -> discord.User:
        return self.client.get_user(user_id)

    def get_users(self, guild: discord.Guild) -> list:
        return guild.members

    def get_user_roles(self, user: discord.User) -> list:
        return user.roles

if __name__ == "__main__":
    dotenv.load_dotenv()
    bot_token = os.getenv("API_BOT_KEY")
    discord_bot = discord_bot(bot_token)
    print(discord_bot.get_guilds())
    print("Bot is running!")