import discord
from discord.ext import commands  
from colorama import Fore as C
from discord_webhook import DiscordWebhook
import time
import os
###################################################
os.system(f'cls & title Finessed')
intents = discord.Intents.all()
client = discord.Client()
client = commands.Bot(command_prefix="$", self_bot=True, help_command=None, intents=intents)
token = input("Enter Token: ")
image_types = ["png", "jpeg", "gif", "jpg"]
#####################################################
async def scrape():
  chan = input(f"\x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mEnter channel id:{C.RESET} ")
  channel = await client.fetch_channel(chan)
  messages = await channel.history(limit=500).flatten()
  try:
      os.remove("images.txt")
  except:
      pass
  for x in messages:
    if x.attachments:
      attachment = x.attachments[0] 
      f = open("images.txt", "a")
      f.write(attachment.url + '\n')
      f.close()
      print(C.MAGENTA + "["+ C.RESET + "~" + C.MAGENTA + "]" + C.RESET + attachment.url)
    else:
      print(f"{C.MAGENTA}[{C.RESET}~{C.MAGENTA}]Message Not An Image | Skipping {C.RESET}")
      pass   
###################################################
async def paste():
  send = input(f"\x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mEnter channel id: {C.RESET}")
  channel = await client.fetch_channel(send)
  f = open("images.txt", "r")
  for line in f:
    print(C.MAGENTA + "["+ C.RESET + "~" + C.MAGENTA + "]" + C.RESET + line + C.RESET)
    await channel.send(line)
    pass
##################################################
async def websend():
  url = input(f"\x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mEnter Webhook Url: {C.RESET}")
  f = open("images.txt", "r")
  for line in f:
    print(C.MAGENTA + "["+ C.RESET + "~" + C.MAGENTA + "]" + C.RESET + line + C.RED)
    webhook = DiscordWebhook(url=url, content=line, rate_limit_retry=True)
    response = webhook.execute()
###################################################
os.system('cls')

async def menu():
  with open('images.txt') as f:
      L = len(f.readlines())
  os.system('cls')
  print(f'''\x1b[38;5;199m
                 ╔═╗╦╔╗╔╔═╗╔═╗╔═╗╔═╗╔╦╗
                 ╠╣ ║║║║║╣ ╚═╗╚═╗║╣  ║║
                 ╚  ╩╝╚╝╚═╝╚═╝╚═╝╚═╝═╩╝
\x1b[38;5;199m       ╔═════════════════════════════════════════╗
       ║\x1b[38;5;199m[{C.RESET}1\x1b[38;5;199m] {C.RESET}Scrape Pfps/gifs\x1b[38;5;199m                     ║
\x1b[38;5;199m       ║\x1b[38;5;199m[{C.RESET}2\x1b[38;5;199m] {C.RESET}Send to Server\x1b[38;5;199m                       ║
       ║\x1b[38;5;199m[{C.RESET}3\x1b[38;5;199m] {C.RESET}Send to Webhook (Ratelimits a lot)\x1b[38;5;199m   ║
       ║\x1b[38;5;199m[{C.RESET}4\x1b[38;5;199m] {C.RESET}Credits\x1b[38;5;199m                              ║
       ║\x1b[38;5;199m[{C.RESET}5\x1b[38;5;199m] {C.RESET}Exit\x1b[38;5;199m                                 ║
\x1b[38;5;199m       ╚═════════════════════════════════════════╝

  {C.RESET}''')
  while True:
    choice = input(f"\x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mChoice\x1b[38;5;199m: \x1b[0m")
    if choice == "1":
      await scrape()
      print("\x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mScraped Icons")
      time.sleep(1)
      await menu()
    elif choice == "2":
      await paste()
      print("\x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mFinished Sending Scraped Icons")
      time.sleep(3)
      await menu()
    elif choice == "3":
      await websend()
      print("\x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mFinished Sending Scraped Icons")
      time.sleep(3)
      await menu()
    elif choice == "4":
      os.system('cls')
      print('''
      Credits:\x1b[38;5;199m
╔══════════════════════╗
║\x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mSwishy            \x1b[38;5;199m║
\x1b[38;5;199m║\x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mRoover            \x1b[38;5;199m║
\x1b[38;5;199m╚══════════════════════╝
''')
      time.sleep(3)
      await menu()
    elif choice == "5":
      print("\x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mClosing...")
      time.sleep(2)
      os._exit(0)
    else:
      print(f"{C.RED}Thats not an option!{C.RESET}")
      time.sleep(1)
      await menu()

#####################################################

@client.event
async def on_connect():
	await menu()

client.run(token, bot=False) 