import asyncio
from pytgcalls import idle
from driver.veez import call_py, bot, user


async def start_bot():
    await bot.start()
    print("[INFO]: BOT & UBOT CLIENT STARTED !!")
    await call_py.start()
    print("[INFO]: PY-TGCALLS CLIENT STARTED !!")
    await user.join_chat("G_RO_UP_1")
    await user.join_chat("APP_YOUTUBE")
    await user.join_chat("Egyption_group")
    await user.join_chat("Egyption_groub")
    await user.join_chat("CHAT_EGYPTION")
    await idle()
    print("[INFO]: STOPPING BOT & USERBOT")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
