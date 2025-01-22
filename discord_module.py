import requests

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


if __name__ == "__main__":
    pass
    