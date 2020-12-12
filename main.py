from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters)for char in range(randint(8, 10))]
    password_symbols = [choice(symbols)for sym in range(randint(2, 4))]
    password_number = [choice(numbers) for num in range(randint(2, 4))]

    password_list = password_letters + password_number + password_symbols
    shuffle(password_list)

    password1 = "".join(password_list)
    password_entry.insert(0, password1)
    pyperclip.copy(password1)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web_name = website_entry.get()
    user_name = user_name_entry.get()
    password = password_entry.get()

    if web_name and user_name and password:
        is_ok = messagebox.askokcancel(title=web_name, message=f"These are the details entered: \nEmail: {user_name} "
                                                               f"\nPassword: {password} \nIs it ok to save")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{web_name} | {user_name} | {password}\n")
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")
    else:
        messagebox.showerror(title="Oops", message="please don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manger")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=(FONT_NAME, 15))
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

user_name_label = Label(text="Email/Username:", font=(FONT_NAME, 15))
user_name_label.grid(column=0, row=2)
user_name_entry = Entry(width=35)
user_name_entry.grid(column=1, row=2, columnspan=2)
user_name_entry.insert(0, "anwar@gmail.com")

password_label = Label(text="Password:", font=(FONT_NAME, 15))
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
