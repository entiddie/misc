# displays date and time on a voice channel

import discord
from discord.ext import commands
import asyncio
from datetime import datetime
from pytz import timezone

client = commands.Bot(command_prefix=",")


months = {
    '01': 'Jan',
    '02': 'Feb',
    '03': 'Mar',
    '04': 'Apr',
    '05': 'May',
    '06': 'Jun',
    '07': 'Jul',
    '08': 'Aug',
    '09': 'Sep',
    '10': 'Oct',
    '11': 'Nov',
    '12': 'Dec',
}


async def time():
    await client.wait_until_ready()

    while not client.is_closed():

        location = timezone('Asia/Kolkata')  # timezone
        now_time = datetime.now(location)
        month = months[str(now_time.strftime('%m'))]
        day = now_time.strftime('%d')
        hour = now_time.strftime('%H')
        minute = round(int(now_time.strftime('%M')), -1)
        print(now_time.strftime('%m %d - %H %M'))

        vc = client.get_channel(voice channel id)

        await vc.edit(name=f"🕗 {month} {day} {hour}:{minute}")

        await asyncio.sleep(1800)  # intervals the bot should update the time in seconds


client.loop.create_task(time())


client.run('token')
