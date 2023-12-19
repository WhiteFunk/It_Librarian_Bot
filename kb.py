from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

available_languages = ["c++", "python"]
available_levels = ["professional", "intermediate", "junior"]
available_themes = ["multithreading", "network", "improving skills","overview","patterns"]

menu = [
    [InlineKeyboardButton(text="All books", callback_data="all_books"),
    InlineKeyboardButton(text="Adding a book", callback_data="add_book")],
    [InlineKeyboardButton(text="Search by name", callback_data="search_name")]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)

kbLanguages = [
    [InlineKeyboardButton(text="c++", callback_data="cpp"),
    InlineKeyboardButton(text="python", callback_data="python")]
]
kbLanguages = InlineKeyboardMarkup(inline_keyboard=kbLanguages)

kbLevels = [
    [InlineKeyboardButton(text="professional", callback_data="professional"),
    InlineKeyboardButton(text="intermediate", callback_data="intermediate"),
    InlineKeyboardButton(text="junior", callback_data="junior")]
]
kbLevels = InlineKeyboardMarkup(inline_keyboard=kbLevels)

kbThemes = [
    [InlineKeyboardButton(text="multithreading", callback_data="multithreading"),
    InlineKeyboardButton(text="network", callback_data="network")],
     [InlineKeyboardButton(text="improving skills", callback_data="improving skills")],
      [InlineKeyboardButton(text="overview", callback_data="overview"),
    InlineKeyboardButton(text="patterns", callback_data="patterns")]
]
kbThemes = InlineKeyboardMarkup(inline_keyboard=kbThemes)


exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Menu")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Menu", callback_data="menu")]])