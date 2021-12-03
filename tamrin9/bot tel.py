
from telebot import *
from pyrogram import Client
app = Client(
    session_name="robot",
    bot_token="5000367924:AAGyDRKiwlMBHh_BkvVpJPJs_V1skONfhMM",
    api_id=16272049,
    api_hash="9368a3f041a1debf915ad0dad5b36750"
)


@app.on_message()
async def start(client, message):
    if message.text == "/start":
        await app.send_message(message.chat.id, "سلام خوش اومدی")


@app.on_message()
async def game(client, message):
    if message.text == "/game":
        await app.send_message(message.chat.id, "شروع بازی")


@app.on_message()
async def age(client, message):
    if message.text == "/age":
        z = str(1400)
        q = message.text
        await app.send_message(message.chat.id, "z-q")


@app.on_message()
async def max(client, message):
    if message.text == "/max":
        w = message.text
        await  app.send_message(message.chat.id, print(max(w)))


@app.on_message()
async def argmax(client, message):
    if message.text == "/argmax":
        e = message.text
        await app.on_message(message.chat.id, print(len(e)))


async def help(client, message):
    if message.text == "/help":
        await  app.send_message(message.chat.id, """
    با توجه به اسم دکمه ها کاربرد آن ها مشخص است
    """)

app.run()
