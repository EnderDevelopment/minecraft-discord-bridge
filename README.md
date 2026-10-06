# Minecraft Discord Bridge

Bridge your Minecraft server and Discord community with live chat and server management.

## Features

- Live chat bridge between Discord and Minecraft server
- Server status monitoring
- Player list and team finder
- Account linking between Discord and Minecraft
- Rewards system

## Requirements

- Node.js v16 or higher
- Discord.js v14
- Python 3.8 or higher
- Minecraft server with RCON enabled

## Installation

1. Clone the repository
2. Install the required packages using `npm install`
3. Create a `.env` file based on `.env.example` and fill in the required values
4. Run the bot using `node bot.js`

## Usage

### Commands

| Command | Description |
| --- | --- |
| !ping | Check if the bot is online |
| !server_status | Get the current server status |
| !player_list | List all online players |
| !team_finder | Find a team to play with |
| !link_account <minecraft_username> | Link your Discord account to your Minecraft account |

### Permissions

The bot requires the following Discord permissions:

- Send Messages
- Read Message History
- Manage Roles

## Configuration

Create a `.env` file in the root directory with the following variables:

```env
DISCORD_TOKEN=your_discord_bot_token
RCON_HOST=your_rcon_host
RCON_PASSWORD=your_rcon_password
RCON_PORT=your_rcon_port
MINECRAFT_SERVER_IP=your_minecraft_server_ip
MINECRAFT_SERVER_PORT=your_minecraft_server_port
```

---

## Generated with EnderDevelopment

This plugin was generated in minutes with [EnderDevelopment](https://enderdevelopment.com) — the AI platform that turns your ideas into working Minecraft plugins, Discord bots and FiveM scripts.

**Want your own?** [Generate this project on EnderDevelopment](https://dash.enderdevelopment.com?utm_source=github&utm_medium=readme&utm_campaign=minecraft-discord-bridge&utm_content=bottom) — describe it in one sentence and get the full source code.