from telegram import Update, Bot


async def handle_update(update: Update, bot: Bot):
    """Route incoming updates to command handlers.

    Add new commands here. The webhook core (api/index.py) calls
    this function for every incoming message — no changes needed
    in the core to add features.
    """
    text = update.message.text

    if text == "/start":
        await bot.send_message(
            chat_id=update.effective_chat.id,
            text="Hello World"
        )
    elif text == "/help":
        await bot.send_message(
            chat_id=update.effective_chat.id,
            text="Available commands:\n/start - Hello World\n/help - This message"
        )
