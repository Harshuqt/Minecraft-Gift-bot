
# Minecraft Item Drop Bot

## Description
This Python script is a Discord bot designed to drop random Minecraft items into players' inventory on your Discord server. It includes mechanisms to prevent server lag by sending kill command to entities items nearby.

### Key Features:
1. **Random Item Dropping**: Drops random items based on the provided list of items.
2. **Quantity Control**: Allows setting a maximum quantity (`max_amount`) for each item type drop.
3. **Kill Command**: Sends a kill command to remove any nearby items boats & minecraft and any entitys this is to prevent if too many items are dropped, the server can cause lag thus preventing server lag. ( You can remove this kil command by removing line 23 and 24 )
4. **Discord Integration**: Requires DiscordSRV installed on your Minecraft server with a DiscordSRV Console channel configured.

### Prerequisites
- [DiscordSRV](https://discordsrv.com/) must be installed and running on your Minecraft server.
- You need to:
  - Create a Discord account for the bot (to access DiscordSRV)
  - whitelist this bot in DiscordSRV console so it can send messages
  - Replace placeholder values with your actual credentials

### Setup Instructions
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Script**:
   ```bash
   python3 minecraft_item_drop.py
   ```
   This will start the bot in DiscordSRV console channel after it has whitelisted your bot.

### Usage Guide

#### 1. Configuring the Pastebin URL
The script uses a raw Pastebin URL to extract item names from a text file. Replace `PASTEBIN_RAW_URL` with your actual Pastebin URL for item list 

#### 2. Providing Your Bot Token
Replace `<bot_token>` in the code with your Discord bot's access token.

#### 3. Specifying the Server Channel ID
Replace `<CHANNEL_ID>` with your server's DiscordSRV Console channel ID where you want the bot to send messages.


#### Example Pastebin URL Format:
```
https://pastebin.com/raw
```

your pastebin url list items

#### 4. Setting Maximum Quantity
Adjust `max_amount` parameter when initializing the bot. Default is set to 64.


### Deployment
1. After setup and configuration, run your bot in the background.
2. whitelist the bot in DiscordSRV console so it can send messages.


```

### Notes
- Make sure to replace all placeholder values with your actual information.
- This script should only be used with server owners' tokens and whitelisted users.
- Always respect bot permissions in DiscordSRV.

This README provides a comprehensive guide for setting up, running, and configuring the Minecraft Item Drop Bot. Let me know if you have any questions!