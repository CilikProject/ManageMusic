from pyrogram import filters

from config import BANNED_USERS
from strings import get_command
from CilikMusic import app
from CilikMusic.utils.misc import extract_user
from CilikMusic.utils.decorators import AdminRightsCheck
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, Message

@app.on_message(
    filters.command(["promote", "fullpromote"], [".", "/"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def promote(cli, message: Message, chat_id):
    user_id = await extract_user(message)
    umention = (await app.get_users(user_id)).mention
    Cilik = await app.reply("💈 `Processing...`")
    if not user_id:
        return await Cilik.edit("I can't find that user.")
    bot = await app.get_chat_member(message.chat.id, app.me.id)
    if not bot.can_promote_members:
        return await Cilik.edit("I don't have enough permissions")
    if message.command[0][0] == "f":
        await message.chat.promote_member(
            user_id=user_id,
            can_change_info=bot.can_change_info,
            can_invite_users=bot.can_invite_users,
            can_delete_messages=bot.can_delete_messages,
            can_restrict_members=bot.can_restrict_members,
            can_pin_messages=bot.can_pin_messages,
            can_promote_members=bot.can_promote_members,
            can_manage_chat=bot.can_manage_chat,
            can_manage_voice_chats=bot.can_manage_voice_chats,
        )
        return await Cilik.edit(f"🎖 Fully Promoted! {umention}")

    await message.chat.promote_member(
        user_id=user_id,
        can_change_info=False,
        can_invite_users=bot.can_invite_users,
        can_delete_messages=bot.can_delete_messages,
        can_restrict_members=False,
        can_pin_messages=False,
        can_promote_members=False,
        can_manage_chat=bot.can_manage_chat,
        can_manage_voice_chats=bot.can_manage_voice_chats,
    )
    await Cilik.edit(f"🏅 Promoted! {umention}")
