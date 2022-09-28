from pyrogram import filters

from config import BANNED_USERS
from CilikMusic import app
from CilikMusic.utils.misc import extract_user
from CilikMusic.utils.decorators import AdminRightsCheck
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, Message

@app.on_message(filters.command("pm", [".", "^", "-", "!", "/"]))
async def promote(_, message: Message):
    yanto = message.reply_to_message.from_user.id 
    await app.promote_chat_member(message.chat.id,
    user_id=yanto,
        can_change_info=True,
        can_invite_users=True,
        can_delete_messages=True,
        can_restrict_members=True,
        can_pin_messages=True,
        can_promote_members=True,
        can_manage_chat=True,
        can_manage_voice_chats=True,
    )
    await message.reply_text("Promoted Succes")
    
  
@app.on_message(filters.command("dm", [".", "^", "-", "!", "/"]))
async def demote(_, message: Message):   
    yanto = message.reply_to_message.from_user.id     
    await message.chat.promote_member(
        user_id=yanto,
        can_change_info=False,
        can_invite_users=False,
        can_delete_messages=False,
        can_restrict_members=False,
        can_pin_messages=False,
        can_promote_members=False,
        can_manage_chat=False,
        can_manage_voice_chats=False,
    )
    await message.reply_text("Demoted Succes")
