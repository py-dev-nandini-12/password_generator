# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import string
import random
import pyperclip


def generate_passwords(n=12):
    all = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    all_list = list(all)
    # new_password = []
    # for _ in range(n):
    #     new= random.choice(all_list)
    #     new_password.append(new)

    new_password = [random.choice(all_list) for _ in range(n)]
    passes = ''.join(new_password)  # converts list to string

    password_entry.insert(0, passes)
    pyperclip.copy(passes)  # copies from clipboard
    # print(f"the new password is {passes}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox


def clear():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def save():
    websites = website_entry.get()
    email = email_entry.get()
    passwords = password_entry.get()

    if len(websites) == 0 or len(passwords) == 0:
        messagebox.showinfo(title="OOPS!! ", message="Do not leave empty fields..")
    else:

        is_ok = messagebox.askokcancel(title=websites, message=f"These are the entered details:"
                                                               f"\n Email:{email}\n passwords:{passwords}")

        if is_ok:
            with open("data.txt", "a") as d_file:
                d_file.write(f"{websites} | {email} |{passwords} \n")
            clear()


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Password Manager")
# window.config(width=800,height=600)
window.config(pady=30, padx=50, bg="ivory")

canvas = Canvas(width=200, height=200, bg="white")
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


def create_label(text, font, font_size, font_style, column, row, bg, fg):
    label = Label(text=text, font=(font, font_size, font_style), bg=bg, fg=fg)
    label.grid(column=column, row=row)
    return label


website = create_label("Website :", "Ariel", 20, "normal", 0, 1, "white", "black")
email_username = create_label("Email/Username :", "Ariel", 20, "normal", 0, 2, "white", "black")
password = create_label("Password :", "Ariel", 20, "normal", 0, 3, "white", "black")


def create_entries(width, column, row, columnspan):
    entry = Entry(width=width)
    entry.grid(column=column, row=row, columnspan=columnspan)

    return entry


website_entry = create_entries(35, 1, 1, 2)
website_entry.focus()

email_entry = create_entries(35, 1, 2, 2)
email_entry.insert(0, "caterpiller@email.com")
password_entry = create_entries(21, 1, 3, 2)


# website_entry = Entry(width=35)
# website_entry.grid(column= 1, row=1, columnspan=2)
# website_entry.focus()
#
# email_entry = Entry(width=35)
# email_entry.grid(column= 1, row=2, columnspan=2)
# email_entry.insert(0,"caterpiller@email.com")
#
# password_entry = Entry(width =21)
# password_entry.grid(column= 1, row=3, columnspan=2)


def create_buttons(text, width, command, row, column, columspan):
    button = Button(text=text, width=width, command=command)
    button.grid(row=row, column=column, columnspan=columspan)
    return button


generate_password = create_buttons("Generate Password", 21, generate_passwords, 3, 3, 1)
add = create_buttons("Add", 30, save, 4, 1, 2)

window.mainloop()
