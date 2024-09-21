import sqlite3
from db_module import create_connection
from datetime import datetime


# Uçuş arama fonksiyonu
def search_flights(departure_city, arrival_city):
    conn = create_connection()
    c = conn.cursor()
    c.execute('''
        SELECT * FROM flights 
        WHERE departure_city = ? AND arrival_city = ?
    ''', (departure_city, arrival_city))
    flights = c.fetchall()
    conn.close()
    return flights


# Uçuş rezervasyonu fonksiyonu
def book_flight(flight_id, username):
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT user_id FROM users WHERE username = ?', (username,))
    user_id = c.fetchone()[0]

    # Rezervasyon tarihi
    booking_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    c.execute('''
        CREATE TABLE IF NOT EXISTS Bookings (
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            flight_id INTEGER,
            booking_date TEXT NOT NULL,
            seat_number TEXT,
            status TEXT NOT NULL DEFAULT 'confirmed',
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (flight_id) REFERENCES flights(flight_id)
        )
    ''')

    c.execute('INSERT INTO bookings (user_id, flight_id, booking_date) VALUES (?, ?, ?)',
              (user_id, flight_id, booking_date))
    conn.commit()
    conn.close()
    print("Rezervasyon başarılı!")


# Kullanıcının rezervasyonlarını listeleyen fonksiyon
def list_reservations(username):
    conn = create_connection()
    c = conn.cursor()

    # Kullanıcı kimliği almak için sorgu
    c.execute('SELECT user_id FROM users WHERE username = ?', (username,))
    user_id = c.fetchone()

    if user_id:  # Eğer kullanıcı bulunduysa, devam et
        user_id = user_id[0]

        # Rezervasyonları listeleme sorgusu
        c.execute('''
            SELECT b.booking_id, f.airline, f.departure_city, f.arrival_city, f.departure_time, f.arrival_time, f.price, b.booking_date
            FROM bookings b
            JOIN flights f ON b.flight_id = f.flight_id
            WHERE b.user_id = ?
        ''', (user_id,))

        reservations = c.fetchall()
        conn.close()

        return reservations  # Rezervasyonları döndür
    else:
        conn.close()
        return []  # Eğer kullanıcı yoksa, boş liste döndür