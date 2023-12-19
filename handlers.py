from aiogram import types, F, Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.filters import StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.state import default_state
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import aiogram.types
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from aiogram import Bot
from aiogram.enums.parse_mode import ParseMode

import config
import db
import kb
import text


bot = Bot(token=config.TOKEN, parse_mode=ParseMode.HTML)


available_languages = ["c++", "python"]
available_levels = ["professional", "intermediate", "junior"]
available_themes = ["multithreading", "network", "improving skills","overview","patterns"]

router = Router()
dp = Dispatcher(storage=MemoryStorage())

customDir = "D:\\Programming\\Bots\\ItLibrarian\\Books\\"

class Data:
    def __init__(self):
        self.dir = ""
        self.name = ""
        self.language = ""
        self.level = ""
        self.main_theme = ""
        self.adiitional_theme = ""
        self.short_review = ""
        
        
    
data = Data()


class Book(StatesGroup):
    search = State()
    enter_file = State()
    enter_name = State()
    enter_language = State()
    enter_level = State()
    enter_main_theme = State()
    enter_additional_theme = State()
    enter_short_review = State()


@router.message(Command("search_name"))
async def add_book(message: Message, state: FSMContext):
    await message.answer(
        text="Write name of the book: ",
    )
    await state.set_state(Book.search)
    
@router.message(Book.search)
async def main_theme_chosen(message: Message, state: FSMContext):
    s = message.text.lower()
    books = await db.get_by_name(s)
    for i in books:
        name, dr, *middle, review = i
        await message.answer(name + ": ",)
        file  = FSInputFile(dr)
        await bot.send_document( message.chat.id,file)
        await message.answer(review)
    state.clear
    await message.answer(text.menu, reply_markup=kb.menu)


@router.message(Command("all_books"))
async def all_books(message: Message, state: FSMContext):
    
    books =await db.get_all_books()
    for i in books:
        name, dr, *middle, review = i
        await message.answer(name + ": ",)
        file  = FSInputFile(dr)
        await bot.send_document( message.chat.id,file)
        await message.answer(review)
       
    await message.answer(text.menu, reply_markup=kb.menu)

@router.message(Command("add_book"))
async def add_book(message: Message, state: FSMContext):
    await message.answer(
        text="Write name of the book: ",
    )
    await state.set_state(Book.enter_name)


@router.message(Book.enter_file)
async def file_upload(message: Message, state: FSMContext):
    data.dir =customDir + data.name + ".pdf"
    document = message.document
    await bot.download(document,data.dir)
    
    await message.answer(
        text="Choose language",
        reply_markup=kb.kbLanguages
    )
    await state.set_state(Book.enter_language)
    


@router.message(Book.enter_name)
async def main_theme_chosen(message: Message, state: FSMContext):
    data.name = message.text.lower()
    await state.update_data(name=message.text.lower())
    await message.answer(
        text="Upload file: "
    )
    await state.set_state(Book.enter_file)


@router.message(Book.enter_language, Command("python"))
@router.message(Book.enter_language, Command("cpp"))
async def language_chosen(message: Message, state: FSMContext):
    data.language =message.text.lower()
    await state.update_data(chosen_language=message.text.lower())
    await message.answer(
        text="Next choose level to this book",
        reply_markup=kb.kbLevels
    )
    await state.set_state(Book.enter_level)
       
       
@router.message(Book.enter_level, Command("professional"))    
@router.message(Book.enter_level, Command("intermediate"))
@router.message(Book.enter_level, Command("junior"))
async def level_chosen(message: Message, state: FSMContext):
    data.level =message.text.lower()
    await state.update_data(chosen_level=message.text.lower())
    await message.answer(
        text="Main theme: ",
        reply_markup=kb.kbThemes
    )
    await state.set_state(Book.enter_main_theme)
    

@router.message(Book.enter_main_theme, Command("multithreading"))
@router.message(Book.enter_main_theme, Command("network"))
@router.message(Book.enter_main_theme, Command("improving_skills"))    
@router.message(Book.enter_main_theme, Command("overview"))
@router.message(Book.enter_main_theme, Command("patterns"))
async def main_theme_chosen(message: Message, state: FSMContext):
    data.main_theme =message.text.lower()
    await state.update_data(chosen_main_theme=message.text.lower())
    await message.answer(
        text="Additional theme: ",
        reply_markup=kb.kbThemes
    )
    await state.set_state(Book.enter_additional_theme)


@router.message(Book.enter_additional_theme, Command("multithreading"))
@router.message(Book.enter_additional_theme, Command("network"))
@router.message(Book.enter_additional_theme, Command("improving_skills"))    
@router.message(Book.enter_additional_theme, Command("overview"))
@router.message(Book.enter_additional_theme, Command("patterns"))
async def main_theme_chosen(message: Message, state: FSMContext):
    data.adiitional_theme = message.text.lower()
    await state.update_data(chosen_additional_theme=message.text.lower())
    await message.answer(
        text="Write a short review for the book: "
    )
    await state.set_state(Book.enter_short_review)
    

@router.message(Book.enter_short_review)
async def main_theme_chosen(message: Message, state: FSMContext):
    data.short_review =message.text.lower()
    await state.update_data(short_review=message.text.lower())
    await message.answer(
        "Thanks for adding",
        reply_markup=ReplyKeyboardRemove(),
    )
    state.clear
    
    await db.sql_add()
    
    await message.answer(text.menu, reply_markup=kb.menu)


    
@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)