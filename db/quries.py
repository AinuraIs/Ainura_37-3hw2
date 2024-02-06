import sqlite3
from pathlib import Path
from pprint import pprint


def init_db():
    """
    Создается соединение с БД и курсор
    """
    global db, cursor
    db = sqlite3.connect(
        Path(__file__).parent.parent / "db.sqlite"
    )
    cursor = db.cursor()

def create_tables():

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER
        );
    """)
    db.commit()


def populate_db():
    """
    Заполнение таблиц
    """
    cursor.execute("""
         --sql
         INSERT INTO product (name, price) VALUES
             ("Белый пароход", 500),
             ("Плаха", 450),
         """
                   )
    db.commit()

def get_products():

    cursor.execute("""
        SELECT * FROM product Where id=id_book
    """)
    return cursor.fetchall()

if __name__== '__main__' :
    init_db()
    create_tables()
    print(get_products())