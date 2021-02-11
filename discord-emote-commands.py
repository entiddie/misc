@client.command()
async def emotes(ctx):
    guild = ctx.guild

    emo = guild.emojis

    n_animated = 0
    n_normal = 0

    emos = []

    for emote in emo:
        if emote.animated:
            n_animated += 1

            emos.append(f'<a:{emote.name}:{emote.id}>')

        else:
            n_normal += 1

            emos.append(f'<:{emote.name}:{emote.id}>')

    if len(emos) < 25:

        a = ' '.join(emos)

        e = discord.Embed(
            title=f"Emote List — Animated: {n_animated} Regular: {n_normal}",
            description=a
        )

        await ctx.send(embed=e)

    else:
        li = list_slice(emos, 25)

        a = ' '.join(li[0])

        li.pop(0)

        e = discord.Embed(
            title=f"Emote List — Animated: {n_animated} Regular: {n_normal}",
            description=a
        )

        await ctx.send(embed=e)

        for i in range(len(li)):
            e = discord.Embed(
                description=' '.join(li[i])
            )

            await ctx.send(embed=e)


@client.command()
async def emote(ctx, emo: discord.Emoji=None):
    if not emo:
        return await ctx.send("You need to provide me an emote")

    e = discord.Embed(
        title="Emote Information",
        description=f"""
Emote Name: {emo.name}
Emote ID: {emo.id}
Animated: {emo.animated}
Guild belonging to: {emo.guild.name} ({emo.guild.id})
Created At: {emo.created_at}
[Download]({emo.url})
"""
    )

    e.set_thumbnail(url=emo.url)

    await ctx.send(embed=e)
