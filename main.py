import threading

import discord
import datetime
import asyncio
import random
from flask import Flask
from flask import render_template
from data.parametrs.get_data import get_result, list_words_1, id_1, list_words_2, id_2

id_channel_chatting = 695558777805471764
member_list = []
global list_words_1
get_result('data/parametrs/data.db')
app = Flask(__name__)
letters_1 = []

for i in range(len(id_1) // 3):
    letter = str(list_words_1[0][i]) + ")" + " " + list_words_1[1][i]
    letters_1.append(letter)

letters_2 = []
for i in range(len(id_2) // 3):
    letter = str(list_words_2[0][i]) + ")" + " " + list_words_2[1][i]
    letters_2.append(letter)


@app.route('/year/1')
def year_1():
    return render_template('index.html', letters=letters_1)


@app.route('/year/2')
def year_2():
    return render_template('index.html', letters=letters_2)


# server_id = 695558777360875581

def read_the_token():
    with open('data/key/key.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_the_token()
client = discord.Client()


@client.event
async def on_ready():
    print('Зашёл как {0.user}'.format(client))


@client.event
async def on_message(message):
    global id_channel_chatting, member_list, count
    channel = client.get_channel(id_channel_chatting)
    true_users = ['misa#0364']
    channels_for_commands = ['commands']  # Список каналов в котором можно воспроизводить команды бота.
    if str(message.channel) in channels_for_commands and str(message.author) in true_users:
        if message.content.startswith("!hello"):

            await channel.send('Hi {0.author}!'.format(message))
        elif message.content.startswith("!question"):
            question = message.content[10:]
            message = await channel.send(f"""{question} @everyone""")
            await message.add_reaction('✅')
            await message.add_reaction('❎')
        elif message.content.startswith('!random'):
            x = member_list[random.randint(0, int(count))]
            print(x)
            while x == 'Baisic#6103':
                x = member_list[random.randint(0, int(count))]
                print(x)
            await channel.send(f"""К доске пойдёт @{x}""")
        elif message.content.startswith('!list'):
            if message.content.find("!list 1") != -1:
                await message.channel.send('http://127.0.0.1:8080/year/1')
                app.run(port=8080, host='127.0.0.1')
            elif message.content.find("!list 2") != -1:
                await message.channel.send('http://127.0.0.1:8080/year/2')
                app.run(port=8080, host='127.0.0.1')
        elif message.content.startswith("!get_url"):
            parametr = message.content[9:].split(" ")
            if parametr[0] == '1':
                await channel.send(
                    list_words_1[1][int(parametr[1]) - 1] + " " + "-" + " " + list_words_1[2][int(parametr[1]) - 1])

    else:
        print("Юзер {0.author} написал: {0.content}".format(message))


async def time_message():
    await client.wait_until_ready()
    global id_channel_chatting
    channel = client.get_channel(id_channel_chatting)
    while not client.is_closed():
        try:
            time = str(datetime.datetime.now().time())[:5]
            date = str(datetime.datetime.now().weekday())
            if (time == "17:55" and date == '0') or (time == "17:55" and date == "4"):
                await channel.send('Скоро начнётся занятие, заходите в канал! @everyone')

            await asyncio.sleep(60)

        except Exception as e:
            print(e)
            await asyncio.sleep(60)


async def update_members_list():
    global member_list, count
    await client.wait_until_ready()

    try:
        count = 0
        users_list = client.get_all_members()
        for member in users_list:
            if member != "Baisic#6103":
                member_list.append(member)
            count += 1
        await asyncio.sleep(3600)

    except Exception as e:
        print(e)
        await asyncio.sleep(3600)


client.loop.create_task(update_members_list())
client.loop.create_task(time_message())


def start():
    client.run(token)


if __name__ == '__main__':
    th = threading.Thread(target=start)
    th.start()
