import asyncio
from wechaty import Wechaty, Message

async def on_message(msg: Message):
    if msg.text() == 'ding':
        await msg.say('dong')
    
async def main():
    bot = Wechaty()
    bot.on('message', on_message)
    await bot.start()

asyncio.run(main())
