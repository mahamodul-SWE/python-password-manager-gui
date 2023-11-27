from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    # coping to clipboard generated password
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = website_entry.get()
    email = user_name_entry.get()
    password = password_entry.get()

    if (website and password) == "":
        messagebox.showinfo(title="error", message="Email or Password are empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"You entered:\n Email: {email}\n Password: {password}\n is it correct?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Making Main Window
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)


# canvas UI
canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Website label and entry
website_name_label = Label(text="Website:")
website_name_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Email/Username label and entry
user_name_label = Label(text="Email/Username:")
user_name_label.grid(column=0, row=2)

user_name_entry = Entry(width=35)
user_name_entry.grid(column=1, row=2, columnspan=2)
user_name_entry.insert(END, "midul@gmail.com")

# Password label and entry
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)


# Generate Button
generate_btn = Button(text="Generate Password", command=pass_generator)
generate_btn.grid(column=2, row=3)


# Add Button
add_btn = Button(text="Add", width=36, command=save_info)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()