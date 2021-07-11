# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from . import *


@asst.on_message(
    filters.command(["listvc", f"listvc@{vcusername}"])
    & filters.user(VC_AUTHS())
    & ~filters.edited
)
async def list_handler(_, message):
    await message.reply_text(f"{CallsClient.active_calls}")


@Client.on_message(filters.me & filters.command("listvc", HNDLR) & ~filters.edited)
async def llhnf(_, message):
    await message.edit_text(f"{CallsClient.active_calls}")
