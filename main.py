import discord,time,random,asyncio
from discord.ext.tasks import loop
bot = discord.Client(description="xddd", self_bot=True)
token = "token"
print("Initializing bot...")
print("Starting discord...")
part=-1
@bot.event
async def on_ready():
  print("Logged in")
  print("Bot is ready")
t0=time.time()
lap=False
ign=False
@bot.event
async def on_message(message):
  global running, part, mess,oldm, t0,lap,ign
  mining_channel=#mining channel id goes here
  if (time.time()-t0)>60:
    t0=time.time()
    chan=bot.get_channel(mining_channel)
    await chan.send("pls beg")
    part=1
    print("reboot cycle")
    return
  if message.channel.id!=mining_channel:
    return
  if len(message.content.lower().split("\n")[-1].split("type"))>1:
    chrs=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ']
    wr=list("".join((" "+message.content.lower().split("\n")[-1]).split("type")[1].split('`')))
    wr2=[]
    for x in wr:
      if x in chrs:
        wr2.append(x)
    wr2="".join(wr2)
    await message.channel.send(wr2)
    return
  if message.author.id==270904126974590976 and ign:
    return
  if message.author.id==270904126974590976:
    ign=True
  else:
    ign=False
  part+=1
  if message.author==bot.user:
    return
  t0=time.time()
  await asyncio.sleep(0.5)
  channel=message.channel
  if part==28:
    await channel.send("pls buy laptop")
    part=1
  elif part==26:
    await asyncio.sleep(15)
    await channel.send("pls beg")
    if not(len(message.content.split("broken"))>1):
      part=1
  elif part==24:
    a=list("FRICK")
    await channel.send(random.choice(a))
  elif part==22:
    await channel.send("pls postmemes")
  elif part==20:
    await channel.send("pls hunt")
  elif part==18:
    await channel.send("pls fish")
  elif part==16:
    a=list("ABCD")
    await channel.send(random.choice(a))
  elif part==14:
    await asyncio.sleep(15)
    await channel.send("pls trivia")
  elif part==12:
    a=list("ABCD")
    await channel.send(random.choice(a))
  elif part==10:
    await asyncio.sleep(15)
    await channel.send("pls trivia")
  elif part==8:
    a=list("ABCD")
    await channel.send(random.choice(a))
  elif part==6:
    await channel.send("pls trivia")
  elif part==4:
    await channel.send("high")
  elif part==2:
    await channel.send("pls highlow")
  elif part==0:
    await channel.send("pls beg")
@loop(seconds=60)
async def hold():
  chan=bot.get_channel()#put another channel id here
  await chan.send("text")
hold.before_loop(bot.wait_until_ready())    
hold.start()
bot.run(token, bot=False)
