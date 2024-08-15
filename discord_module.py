from discord_webhook import DiscordWebhook, DiscordEmbed

class discord_Webhooks:
    _webhook : DiscordWebhook
    #allowed_mentions: list[dict[list[str]]]
    deafult_color: str

    def __init__(self, webhook_link: str, user_allowed_mentions: list[str] = [], deafult_color: str = "03b2f8") -> None:
        allowed_mentions = {
            "parse": ["everyone", "here"],
            "users": user_allowed_mentions
        }
        self.deafult_color = deafult_color
        self._webhook = DiscordWebhook(webhook_link, allowed_mentions=allowed_mentions)

    def send_discord_simple_message(self, content: str) -> int:
        self._webhook.set_content(content=content) 
        response = self._webhook.execute()
        return response.status_code

    def send_discord_embed_message(self, title: str, description: str, color: str) -> int:
        embed = DiscordEmbed(title=title, description=description, color=color)
        self._webhook.add_embed(embed=embed)
        response = self._webhook.execute()
        return response.status_code