import sqlite3

#Task 1 and 2
try:
    with sqlite3.connect('../db/magazines.db') as conn:
       conn.execute('PRAGMA foreign_keys = 1')
       cursor = conn.cursor()

       cursor.execute('''CREATE TABLE IF NOT EXISTS publishers(
               publisher_id INTEGER PRIMARY KEY, 
               name TEXT NOT NULL UNIQUE)''')
       cursor.execute('''CREATE TABLE IF NOT EXISTS magazines(
               magazine_id INTEGER PRIMARY KEY, 
               name TEXT NOT NULL UNIQUE,
               publisher_id INTEGER NOT NULL, 
               FOREIGN KEY(publisher_id) REFERENCES publishers(publisher_id))''')
       cursor.execute('''CREATE TABLE IF NOT EXISTS subscribers(
               subscriber_id INTEGER PRIMARY KEY, 
               name TEXT NOT NULL,
               address TEXT NOT NULL)''')
       cursor.execute('''CREATE TABLE IF NOT EXISTS subscriptions(
               subscription_id INTEGER PRIMARY KEY, 
               subscriber_id INTEGER NOT NULL, 
               magazine_id INTEGER NOT NULL, 
               expiration_date TEXT NOT NULL,
               FOREIGN KEY(subscriber_id) REFERENCES subscribers(subscriber_id),
               FOREIGN KEY(magazine_id) REFERENCES magazines(magazine_id))''')

       print('Database created and connected successfully.')

except sqlite3.Error as e:
    print(f'Database file failed: {e}')

#Task 3
def add_publisher(cursor, name):
    try:
       cursor.execute('INSERT INTO publishers (name) VALUES (?)', (name,))
    except sqlite3.IntegrityError:
       print('Publisher already exists', name)
    
def add_magazine(cursor, name, publisher_id):
    try:
       cursor.execute('INSERT INTO magazines (name, publisher_id) VALUES (?, ?)', (name, publisher_id))
    except sqlite3.IntegrityError:
       print('Magazine already exists:', name)

def add_subscriber(cursor, name, address):
    try:
       cursor.execute('INSERT INTO subscribers (name, address) VALUES (?, ?)', (name, address))
    except sqlite3.IntegrityError:
       print('Subscriber already exists:', name)

def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
    try:
       cursor.execute('INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)', (subscriber_id, magazine_id, expiration_date))
    except sqlite3.IntegrityError as e:
       print('Subscription already exists:', e)

add_publisher(cursor, 'New York Times',)
add_publisher(cursor,'Conde Nast')
add_publisher(cursor, 'Time Inc')
add_magazine(cursor, 'NYT Magazine', 1)
add_magazine(cursor, 'Vogue', 2)
add_magazine(cursor, 'Time', 3)
add_subscriber(cursor, 'Ashley Johnson', '123 Main St')
add_subscriber(cursor, 'Bob Stone', '456 Oak Ave')
add_subscriber(cursor, 'Abel Tesfaye', '789 Pine Rd')
add_subscription(cursor, 1, 1, '2025-01-01')
add_subscription(cursor, 2, 2, '2025-03-15')
add_subscription(cursor, 3, 3, '2025-06-30')

conn.commit()

print('Sample data inserted successfully\n')

#Task 4
print('All subscribers:')
cursor.execute('SELECT * FROM subscribers')

for row in cursor.fetchall():
   print(row)

print('\nAll magazines:')
cursor.execute('SELECT * FROM magazines ')

for row in cursor.fetchall():
   print(row)

print('\nMagazines published by New York Times:')

cursor.execute("""SELECT m.name FROM magazines m
               JOIN publishers p ON m.publisher_id = p.publisher_id
               WHERE p.name = 'New York Times'""")

for row in cursor.fetchall():
   print(row)