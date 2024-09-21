import sqlite3
import hashlib
from db_module import create_connection


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password):
    conn = create_connection()
    c = conn.cursor()
    c.execute('''
        INSERT INTO users (username, password)
        VALUES (?, ?)
    ''', (username, hash_password(password)))
    conn.commit()
    conn.close()
    print("Kayıt başarılı")


def login_user(username, password):
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT password FROM users WHERE username = ?', (username,))
    result = c.fetchone()
    conn.close()

    if result and result[0] == hash_password(password):
        print("Giriş başarılı")
        return True
    else:
        print("Hatalı kullanıcı adı veya şifre")
        return False
