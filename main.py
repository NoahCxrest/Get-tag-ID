'''
Simple, but effective.
To get the tags, you need to add all of them to the forum, and run /get_tags in the channel.
I am making this public because there is currently no way to get tag IDs easily.
'''

@bot.hybrid_command(name="get_tags", with_app_command=True, description="Get tag and tag IDs applied to channel.")
async def get_tags(ctx):
    # Check if the channel has the applied_tags property
    if not hasattr(ctx.channel, 'applied_tags'):
        await ctx.send("The applied_tags property is not supported in this channel.")
        return

    # Get information about applied tags
    tag_info = [(tag.name, tag.id) for tag in ctx.channel.applied_tags]

    # Format and send the response
    response = "\n".join(f"Tag Name: {name}, Tag ID: {tag_id}" for name, tag_id in tag_info)
    await ctx.send(f"Tags applied to this thread:\n{response}")
