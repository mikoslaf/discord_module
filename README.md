# Project Discord_module

## Your Simple Solution for Discord Webhooks

This repository contains a Python module for interacting with Discord. It is intended to provide a set of tools and functionalities to easily create and manage Discord bots.

## Features

- Easy-to-use interface for creating Discord bots
- Support for various Discord Webhook functionalities
- Extensible and customizable for specific use cases

## Installation

### Requirements

- [Python 3.12](https://www.python.org/)
- [discord-webhook](https://pypi.org/project/discord-webhook/)

### Steps

1. Run `git clone https://github.com/mikoslaf/discord_module.git` in your project.
2. Install necessary packages, for example, you can run `pip install discord-webhook`.

## Usage

Here is a basic example of how to use the `discord_module` to create a simple Discord bot:

1. Add import in your project
```python
import discord_module
```

2. Create a new instance
```python
webhook = discord_module.Webhooks(webhook_link="https://discord.com/api/webhooks/LINK", user_allowed_mentions=["user"])
```

3. Send a message
```python
webhook.send_discord_simple_message(content="Your content here")
# or 
webhook.send_discord_embed_message(title="Your title", description="Your description", color="03b2f8")
```
