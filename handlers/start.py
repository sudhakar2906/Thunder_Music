from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (CallbackContext, CallbackQueryHandler, CommandHandler,
                          Filters, MessageHandler)

@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>

I am Lightning Music Bot, that lets you play music in your Telegram groups voice chat.
 . 



Use The Button 🔘 Bellow To Know About Me And My Comandas. 
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎶 Lightning Music Player", url="t.me/vcmusicplayerlightning"
                    )
                ],
                [    InlineKeyboardButton(
                            text="☑️ Add Saitama to your group",
                            url="t.me/{}?startgroup=true".format(
                                context.bot.username))
                ],
                [
                    InlineKeyboardButton(
                        "💬 Support Group", url="https://t.me/chattingwithothers"
                    ),
                    InlineKeyboardButton(
                        "Our Group Management Bot", url="https://t.me/Thunderking_ro_bot"
                    ),
                    InlineKeyboardButton(
                        "CoMes Under Wasp ", url="https://t.me/WaspGroupcommunity" )
                ],
                [
                    InlineKeyboardButton(
                        "Commands How To Use Bot", url="https://telegra.ph/Developer-03-31"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
