import sqlite3

my_db = '/tmp/my_example.db'

# Create db and insert data
con1 = sqlite3.connect(my_db)
cur = con1.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS books (id number, title text, dir text, price real)')
cur.execute("INSERT INTO books VALUES(1, 'sewing magic', '/home/deepa/books', 10.34)")
cur.execute('INSERT INTO books VALUES(2, "combinatorics", "/media/backup2/books", 100.56)')
cur.execute('INSERT INTO books VALUES(3, "harry potter 1", "/media/backup2/books", 8.17)')
cur.execute('INSERT INTO books VALUES(4, "harry potter 4", "/media/backup2/books", 25.44)')
cur.execute('INSERT INTO books VALUES(5, "harry potter 7", "/media/backup2/books", 83.29)')
con1.commit()
con1.close()

# Queries
con2 = sqlite3.connect(my_db)
cur = con2.cursor()
for row in cur.execute('SELECT * FROM books ORDER BY id'):
    print(row)
print()

for row in cur.execute('SELECT * FROM books WHERE id > ?', (3, )):
    print(row)
print()

for row in cur.execute("SELECT * FROM books WHERE title LIKE ?", ("harry potter %", )):
    print(row)
print()
