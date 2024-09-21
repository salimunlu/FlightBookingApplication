import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from user_module import login_user, register_user


class FlightBookingApp:
    def __init__(self, root):
        self.register_password_entry = None
        self.register_username_entry = None
        self.password_entry = None
        self.username_entry = None
        self.logo_photo = None
        self.root = root
        self.root.title("Flight Booking System")
        self.active_user = None
        self.root.geometry("500x500")

        self.create_login_window()

    def create_login_window(self):
        self.clear_window()

        login_frame = ttk.Frame(self.root, padding="20")
        login_frame.grid(row=0, column=0, pady=20, sticky="nsew")

        logo_image = Image.open("images/logo.png")
        logo_image = logo_image.resize((300, 150), Image.Resampling.LANCZOS)

        self.logo_photo = ImageTk.PhotoImage(logo_image)

        logo_label = ttk.Label(login_frame, image=self.logo_photo)
        logo_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

        # Kullanıcı Adı widget'ları
        username_label = ttk.Label(login_frame, text="Kullanıcı Adı", font=("Helvetica", 12))
        username_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.username_entry = ttk.Entry(login_frame, font=("Helvetica", 12))
        self.username_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Şifre widget'leri
        password_label = ttk.Label(login_frame, text="Şifre", font=("Helvetica", 12))
        password_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.password_entry = ttk.Entry(login_frame, show="*", font=("Helvetica", 12))
        self.password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Giriş Butonu
        login_button = ttk.Button(login_frame, text="Giriş", command=self.login, style="TButton")
        login_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Kayıt Ol Buton
        register_button = ttk.Button(login_frame, text="Kayıt Ol", command=self.create_register_window, style="TButton")
        register_button.grid(row=3, column=1, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if login_user(username, password):
            messagebox.showinfo("Başarılı", "Giriş başarılı!")
            self.active_user = username
            self.create_flight_menu()
        else:
            messagebox.showerror("Hatalı", "Kullanıcı adı veya şifre yanlış!")

    def create_register_window(self):
        self.clear_window()

        register_frame = ttk.Frame(self.root, padding="20")
        register_frame.pack()

        register_username_label = ttk.Label(register_frame, text="Yeni Kullanıcı Adı", font=("Helvetica", 12))
        register_username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.register_username_entry = ttk.Entry(register_frame, font=("Helvetica", 12))
        self.register_username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        register_password_label = ttk.Label(register_frame, text="Yeni Şifre", font=("Helvetica", 12))
        register_password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.register_password_entry = ttk.Entry(register_frame, show="*", font=("Helvetica", 12))
        self.register_password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        register_button = ttk.Button(register_frame, text="Kayıt Ol", command=self.register)
        register_button.grid(row=2, column=0, columnspan=2, pady=10)

        back_button = ttk.Button(register_frame, text="Geri", command=self.create_login_window)
        back_button.grid(row=2, column=1, columnspan=2, pady=10)

    def register(self):
        username = self.register_username_entry.get()
        password = self.register_password_entry.get()
        register_user(username, password)
        messagebox.showinfo("Başarılı", "Kayıt başarılı!")
        self.create_login_window()


    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_flight_menu(self):
        self.clear_window()


if __name__ == "__main__":
    root = tk.Tk()
    app = FlightBookingApp(root)
    root.minsize(400, 400)
    root.maxsize(800, 800)
    root.mainloop()



        


