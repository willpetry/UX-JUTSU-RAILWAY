# made by @Kakashi_HTK/@ashwinstr

from userge import userge, Message

@userge.on_cmd(
    "copy",
    about={
        "header": "List one per line and copy",
        "description": "Instead of content in one line, shows in more systematic way and makes copyable.",
        "usage": "{tr}copy [text] or [reply to text]",
    },
)
async def _copy(message: Message):
    text = message.input_str or message.reply_to_message.text
    if not text:
        await message.edit("Text not found, provide text. See `{tr}help copy`")
        return
    text = text.replace(": ", ":").replace(":", ":\n").replace(", ", ",").replace(",", "\n")
    text = text.replace("\n", "</code>\n<code>")
    await message.edit(text)