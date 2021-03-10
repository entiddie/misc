    @commands.command()
    async def pagination(self, ctx):
        pages = ['page 1', 'page 2', 'page 3']

        buttons = ['◀', '▶', '🗑']

        m = await ctx.send(pages[0])

        for reaction in buttons:
            await m.add_reaction(reaction)


        def check(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) in buttons

        
        page_track = 0


        while True:

            try:

                reaction, user = await self.client.wait_for('reaction_add', timeout=90, check=check)

                if reaction.emoji == buttons[0]:
                    if page_track != 0:
                        page_track -= 1
                        await m.edit(content=pages[page_track])

                    else:
                        pass
                    

                if reaction.emoji == buttons[1]:
                    if page_track < len(pages) - 1:
                        page_track += 1
                        await m.edit(content=pages[page_track])

                    else:
                        pass
                    

                elif reaction.emoji == buttons[2]:
                    await m.edit(content='Pagination Ended')
                    return

            except asyncio.TimeoutError:
                await m.edit(content='Pagination Ended')
                return

            except Exception as e:
                await ctx.send(e)
                return

            
    # Embed version        
            
            
    @commands.command()
    async def page(self, ctx):

        e1 = discord.Embed(description="page 1")
        e2 = discord.Embed(description="page 2")
        e3 = discord.Embed(description="page 3")


        pages = [e1, e2, e3]

        buttons = ['◀', '▶', '🗑']

        m = await ctx.send(embed=pages[0])

        for reaction in buttons:
            await m.add_reaction(reaction)


        def check(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) in buttons

        
        page_track = 0


        while True:

                try:

                    reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check)

                    if reaction.emoji == buttons[0]:
                        if page_track != 0:
                            page_track -= 1
                            await m.edit(embed=pages[page_track])

                        else:
                            pass
                        

                    if reaction.emoji == buttons[1]:
                        if page_track < len(pages) - 1:
                            page_track += 1
                            await m.edit(embed=pages[page_track])

                        else:
                            pass
                        

                    elif reaction.emoji == buttons[2]:
                        await m.clear_reactions()
                        return

                except asyncio.TimeoutError:
                    await m.clear_reactions()
                    return

                except Exception as e:
                    await ctx.send(e)
                    return
