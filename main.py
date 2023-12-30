from pyrogram import Client, filters, idle, types
import re


app = Client(
    "name",
    api_id=656565,#aqui pon tu api id no se pone entre parentesis solo cambiala por la que esta escrita 
    api_hash="",
    bot_token="",
    in_memory=True
)

app.start()
start_string = '''
◆ ▬▬▬ ❴ĊØPУ ßØ†❵ ▬▬▬ ◆

[🎭] 🙋 ¡Bienvenido {}! 

[🎭] Soy un bot 🤖 AnonNews _irc que copia contenido de cualquier canal de contenido restringido.

[🎭] Simplemente envía el enlace de la publicación desde un canal público.

[🎭] Ejemplo: `https://t.me/telegram/259`

◆ ▬▬▬ ❴ ÐξעξĿØPξÐ ❵ ▬▬▬ ◆

⎇ Telegram : https://t.me/addlist/iZfJw-LVfYthNzYx
'''
@app.on_message(filters.text & filters.private)
async def on_text(c: Client, m: types.Message):
    text = m.text
    if re.findall("((www\.|http://|https://)(www\.)*.*?(?=(www\.|http://|https://|$)))", text):
        url = re.findall("((www\.|http://|https://)(www\.)*.*?(?=(www\.|http://|https://|$)))", text)[0][0]
        print(url)
        if "t.me/" in url:
            if "c/" in url:
                return await m.reply("Enviar un enlace 🔗 desde un canal público", quote=True)
            else:
                channel = url.split("t.me/")[1].split("/")[0]
                msg_id = int(url.split("t.me/")[1].split("/")[1])
                reply = await m.reply(" Espera ....⏳", quote=True)
                msg = await c.get_messages(channel, msg_id)
                await reply.delete()
                if not msg.chat.has_protected_content:
                    return await m.reply("El contenido no está restringido🚯.", quote=True)
                if msg.text:
                    return await m.reply(msg.text.html, quote=True, reply_markup=msg.reply_markup)
                if msg.media_group_id:
                    return await c.copy_media_group(m.chat.id, msg.chat.id, msg.id)
                if msg.media:
                    return await msg.copy(m.chat.id, reply_markup=msg.reply_markup)
        else:
            return await m.reply("Se requiere un enlace 🔗 a una publicación de un canal.", quote=True)
    else:
        return await m.reply(start_string.format(m.from_user.mention))

print(app.me.username)
idle()

