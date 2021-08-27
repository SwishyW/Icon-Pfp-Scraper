import discord
from discord.ext import commands
import enquiries
from colorama import Fore as C
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
import time
import os
##################################################
intents = discord.Intents.all()
client = discord.Client()
client = commands.Bot(command_prefix="$", self_bot=True,help_command=None, intents=intents)
token = os.getenv("TOKEN")
headers = {'Authorization': f"{token}"}
def reset():
  os.system('clear')
  question()
#####################################################
def question():
  print(f'''{C.GREEN}
  ╔═╗╦╔╗╔╔═╗╔═╗╔═╗╔═╗╔╦╗
  ╠╣ ║║║║║╣ ╚═╗╚═╗║╣  ║║
  ╚  ╩╝╚╝╚═╝╚═╝╚═╝╚═╝═╩╝
-------------------------------------------
  ''')
  options = [f'  {C.RED}[!] Scrape', f'  {C.RED}[+] Paste', f'{C.RED}  [*] Reset']
  choice = enquiries.choose(f'\n {C.YELLOW}[?] {C.BLUE}Select Command{C.MAGENTA}${C.WHITE}:\n', options)
  if choice == f"  {C.RED}[!] Scrape":
      global chan
      chan = input(f"{C.MAGENTA}  [^] Enter channel id: ")
  elif choice == f"  {C.RED}[+] Paste":
      global send
      send = input(f"{C.MAGENTA}  [+] Enter Webhook URL: ")
  elif choice == f"{C.RED}  [*] Reset":
      reset()
  else:
      print(f"{C.RED}  [!] Invalid Option Selected")
      reset()
#####################################################
@client.command()
async def scrape(ctx):
  channel = await client.fetch_channel(chan)
  messages = await channel.history(limit=100).flatten()
  for x in messages:
    if x.attachments:
      attachment = x.attachments[0] 
      f = open("images.txt", "a")
      f.write(attachment.url + '\n')
      f.close()
      print("  " + attachment.url)
    else:
      print(f"{C.RED}Message Not An Image | Skipping")
      pass  
  reset()
  question() 
#####################################################
@client.command()
async def paste(ctx):
  async with aiohttp.ClientSession() as session:
    webhook = Webhook.from_url(send, adapter=AsyncWebhookAdapter(session))
    f = open("images.txt", "r")
    for line in f:
      print(f"{C.BLUE}  {line}")
      await webhook.send(line)
      time.sleep(1)
  os.remove('scraped.txt')
  os.mknod('scraped.txt')
  reset()
#####################################################
question()
client.run(token, bot=False)
