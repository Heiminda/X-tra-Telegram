@command(pattern="^.wel", outgoing=True)
async def BA_welcome(event):
    if event.fwd_from:
        return
    await event.edit("**Welcome to Brillante Amore.We are happy to have you here. Have a nice chat and make new friends**")
