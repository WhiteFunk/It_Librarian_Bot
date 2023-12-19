import sqlite3 as sq

from handlers import data

def sql_start():
    global base, cur
    base = sq.connect('books.db')
    cur = base.cursor()
    base.execute('CREATE TABLE IF NOT EXISTS books(name TEXT, directory TEXT, language TEXT, level TEXT, main_theme TEXT, additional_theme  TEXT, short_review TEXT)')
    base.commit()
    
async def get_all_books():
    
    books = cur.execute("SELECT * FROM books").fetchall()
    
    return books

async def get_by_name(s):
    
    books = cur.execute("SELECT * FROM books WHERE name=?",(s)).fetchall()
    
    return books

async def sql_add():
    cur.execute("INSERT INTO books (name, directory, language, level, main_theme, additional_theme, short_review) VALUES (?,?,?,?,?,?,?)",(data.name,data.dir,data.language,data.level,data.main_theme,data.adiitional_theme,data.short_review))
    base.commit()