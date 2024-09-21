from user_module import register_user, login_user
from flight_module import search_flights, book_flight, list_reservations
from db_module import create_users, create_bookings, create_flights, populate_flights


def main_menu():
    print("1. Kullanıcı Kaydı")
    print("2. Giriş")
    print("3. Çıkış")
    choice = input("Bir seçim yapın: ")
    return choice


def flight_menu():
    print("1. Uçuş Ara")
    print("2. Uçuş Rezervasyonu Yap")
    print("3. Rezervasyonlarım")
    print("4. Çıkış")
    choice = input("Bir seçim yapın: ")
    return choice


def main():
    create_users()
    create_flights()
    create_bookings()
    populate_flights()

    while True:
        choice = main_menu()

        if choice == '1':
            username = input("Kullanıcı adı: ")
            password = input("Şifre: ")
            register_user(username, password)

        elif choice == '2':
            username = input("Kullanıcı adı: ")
            password = input("Şifre: ")

            if login_user(username, password):
                while True:
                    flight_choice = flight_menu()

                    if flight_choice == '1':
                        departure_city = input("Kalkış şehri: ")
                        arrival_city = input("Varış şehri: ")
                        flights = search_flights(departure_city, arrival_city)
                        for flight in flights:
                            print(
                                f"Uçuş ID: {flight[0]}, Havayolu: {flight[1]}, Kalkış: {flight[2]}, Varış: {flight[3]}, Fiyat: {flight[6]}")

                    elif flight_choice == '2':
                        flight_id = input("Rezervasyon yapmak istediğiniz uçuş ID: ")
                        book_flight(flight_id, username)

                    elif flight_choice == '3':
                        reservations = list_reservations(username)
                        for reservation in reservations:
                            print(reservation)

                    elif flight_choice == '4':
                        break

        elif choice == '3':
            print("Çıkış yapıldı.")
            break


if __name__ == '__main__':
    main()