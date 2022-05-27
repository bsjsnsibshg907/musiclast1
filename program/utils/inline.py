""" inline section button """

from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)


def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="- الـقـائـمـه .", callback_data=f'cbmenu | {user_id}'),
      InlineKeyboardButton(text="- الـتـحـديـثـات .", url=f'https://t.me/APP_YOUTUBE'),
    ],
    [
    InlineKeyboardButton(
                        "- ضـيـف الـبـوت لـمـجـموعـتـك .",
                        url=f'https://t.me/BBSBBOT?startgroup=true'),
    ],
  ]
  return buttons


def menu_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="⏹", callback_data=f'cbstop | {user_id}'),
      InlineKeyboardButton(text="⏸", callback_data=f'cbpause | {user_id}'),
      InlineKeyboardButton(text="▶️", callback_data=f'cbresume | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🔇", callback_data=f'cbmute | {user_id}'),
      InlineKeyboardButton(text="🔊", callback_data=f'cbunmute | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="- اغـلاق .", callback_data='cls'),
    ]
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "- رجـوع .", callback_data="cbmenu"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "- رجـوع .", callback_data="cbmenu"
      )
    ]
  ]
)
