import sqlite3


def create_connection():
    return sqlite3.connect("airline_booking.db")


def create_users():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def create_flights():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS flights (
            flight_id INTEGER PRIMARY KEY AUTOINCREMENT ,
            airline TEXT NOT NULL,
            departure_city TEXT NOT NULL,
            arrival_city TEXT NOT NULL,
            departure_time TEXT NOT NULL,
            arrival_time TEXT NOT NULL,
            price REAL NOT NULL 
        )
    ''')
    conn.commit()
    conn.close()


def create_bookings():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            flight_id INTEGER,
            booking_date TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (flight_id) REFERENCES flights(flight_id)
        )
    ''')
    conn.commit()
    conn.close()


def populate_flights():
    conn = create_connection()
    c = conn.cursor()
    flights = [
        ('Turkish Airlines', 'Istanbul', 'Ankara', '2024-09-10 08:00', '2024-09-10 09:00', 100.0),
        ('Pegasus', 'Izmir', 'Istanbul', '2024-09-11 15:00', '2024-09-11 16:30', 120.0),
        ('SunExpress', 'Antalya', 'Izmir', '2024-09-12 10:00', '2024-09-12 11:30', 90.0),
        ('Turkish Airlines', 'Istanbul', 'Berlin', '2024-09-13 12:00', '2024-09-13 14:30', 250.0)
    ]
    c.executemany('''
        INSERT INTO flights (airline, departure_city, arrival_city, departure_time, arrival_time, price)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', flights)
    conn.commit()
    conn.close()
