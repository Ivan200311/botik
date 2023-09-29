import sqlite3

connect = sqlite3.connect('bd.db', check_same_thread=False)
cursor = connect.cursor()

def registr(tg_id):
    connect = sqlite3.connect('bd.db', check_same_thread=False)
    cursor = connect.cursor()
    cursor.execute('''
            INSERT INTO "users" (tg_id) 
            VALUES (?, ?)''', (tg_id))
    connect.commit()

def check(tg_id):
    connect = sqlite3.connect('bd.db', check_same_thread=False)
    cursor = connect.cursor()
    return cursor.execute('''
        SELECT tg_id 
        FROM "users" 
        WHERE tg_id = ?''', (tg_id,)).fetchone()


resull = cursor.execute('''
CREATE TABLE IF NOT EXISTS
"users"
("id" INTEGER NOT NULL,
"tg_id" INTEGER NOT NULL,
primary key("id" AUTOINCREMENT)
)''')

resull = cursor.execute('''
CREATE TABLE IF NOT EXISTS
"categories"
("id" INTEGER NOT NULL,
"name" TEXT NOT NULL,
primary key("id" AUTOINCREMENT)
)''')

resull = cursor.execute('''
CREATE TABLE IF NOT EXISTS
"subscribes"
("id_user" INTEGER NOT NULL,
"id_category" INTEGER NOT NULL,
FOREIGN KEY (id_user) REFERENCES users(id) ON DELETE CASCADE,
FOREIGN KEY (id_category) REFERENCES categories(id) ON DELETE CASCADE
)''')
connect.commit()
# cursor.execute('''INSERT INTO categories (name) VALUES("sports")''')
# cursor.execute('''INSERT INTO categories (name) VALUES("business")''')
# cursor.execute('''INSERT INTO categories (name) VALUES("entertainment")''')
# cursor.execute('''INSERT INTO categories (name) VALUES("general")''')
# cursor.execute('''INSERT INTO categories (name) VALUES("health")''')
# cursor.execute('''INSERT INTO categories (name) VALUES("science")''')
# cursor.execute('''INSERT INTO categories (name) VALUES("technology")''')
# connect.commit()


def searchUserCategory(user_id):
    connect = sqlite3.connect('bd.db', check_same_thread=False)
    cursor = connect.cursor()
    return cursor.execute('''SELECT categories.name
        FROM subscribes 
        INNER JOIN categories ON subscribes.id_category = categories.id
        WHERE subscribes.id_user = ?
        ''',(user_id,)).fetchall()


def findCategory(name):
    connect = sqlite3.connect('bd.db', check_same_thread=False)
    cursor = connect.cursor()
    return cursor.execute('''SELECT id
        FROM categories 
        WHERE name = ?
        ''',(name,)).fetchone()

def findCategoryName(id_category):
    connect = sqlite3.connect('bd.db', check_same_thread=False)
    cursor = connect.cursor()
    return cursor.execute('''SELECT name
    FROM categories
    WHERE id = ?
    ''',(id_category,)).fetchone()


def deleteSubscribes(tg_id,id_category):
    connect = sqlite3.connect('bd.db', check_same_thread=False)
    cursor = connect.cursor()
    cursor.execute('''DELETE FROM subscribes 
        WHERE user_id = ?
        AND category_id = ?
        ''', (tg_id, id_category))
    connect.commit()
    return "Вы отписались"

def findUserSubscribes(id_user):
    connect = sqlite3.connect('bd.db', check_same_thread=False)
    cursor = connect.cursor()
    return cursor.execute('''SELECT categories.name FROM subscribes
    INNER JOIN categories ON categories.id = subscribes.id_category
    WHERE subscribes.id_user = ?
    ''',(id_user,)).fetchall()

def findUserId(tg_id):
    print(tg_id)
    connect = sqlite3.connect('bd.db', check_same_thread=False)
    cursor = connect.cursor()
    return cursor.execute('''SELECT id
    FROM users
    WHERE tg_id = ?
    ''', (tg_id,)).fetchone()

cursor.close()
