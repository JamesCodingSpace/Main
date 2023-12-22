import tkinter as tk
from tkinter import messagebox

def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # Hier sollte die Überprüfung der Benutzerdaten erfolgen.
    # Dies ist nur ein einfaches Beispiel. In der Praxis sollte eine sichere Überprüfung implementiert werden.
    if entered_username == "admin" and entered_password == "password":
        messagebox.showinfo("Login erfolgreich", "Willkommen, {}".format(entered_username))
    else:
        messagebox.showerror("Login fehlgeschlagen", "Ungültiger Benutzername oder Passwort")

# GUI erstellen
root = tk.Tk()
root.title("Login")

# Benutzername
tk.Label(root, text="Benutzername:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Passwort
tk.Label(root, text="Passwort:").pack()
password_entry = tk.Entry(root, show="*")  # Das Passwort wird versteckt
password_entry.pack()

# Login-Button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

# GUI starten
root.mainloop()