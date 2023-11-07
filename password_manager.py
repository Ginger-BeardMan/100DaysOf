from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():

    new_pass_result.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    new_letters = [choice(letters) for _ in range(randint(8, 10))]

    new_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    new_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = new_letters + new_symbols + new_numbers

    shuffle(password_list)

    password = "".join(password_list)

    new_pass_result.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_information():

    website_address = website_entry.get()
    username_email = email_username_entry.get()
    password = new_pass_result.get()
    new_data = {
        website_address: {
            'email': username_email,
            'password': password,
        }
    }

    if len(website_address) == 0 or len(password) == 0:
        messagebox.showinfo(title='Warning', message="Please don't leave any fields empty!")

    else:
        try:
            with open("data.json", 'r') as data_file:
                # non-json version: data_file.write(f"{website_address} | {username_email} | {password}\n")
                data = json.load(data_file)  # read the file:

        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)  # update entirety of the data from the file, not append new data
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)  # write all data to the file

        finally:
            website_entry.delete(0, END)
            new_pass_result.delete(0, END)


def find_password():
    website_address = website_entry.get()
    # open json file if there and read
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
        # display information to a window in the correct format
        messagebox.showinfo(title=website_address, message=f"Email/Username: {data[website_address]['email']}"
                                                           f"\nPassword: {data[website_address]['password']}")

    # if not, show error message
    except FileNotFoundError:
        messagebox.showinfo(title='Warning', message="No Data File Found")

    except KeyError:
        messagebox.showinfo(title='Warning', message='No details for the website exists.')


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# website label
website = Label(text='Website:')
website.grid(column=0, row=1)

# website entry
website_entry = Entry(width=20)
website_entry.grid(column=1, row=1)

# information search
search = Button(text='Search', width=14, command=find_password)
search.grid(column=2, row=1)

# email/username label
email_username = Label(text='Email/Username:')
email_username.grid(column=0, row=2)

# email/username entry
email_username_entry = Entry(width=39)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, 'myemail@myemail.com')

# password label
new_pass = Label(text='Password:')
new_pass.grid(column=0, row=3)

# password entry
new_pass_result = Entry(width=20)
new_pass_result.grid(column=1, row=3)

# generate password button
gen_pass_button = Button(text='Generate Password', width=14, command=generate_password)
gen_pass_button.grid(column=2, row=3)

# add button
add_pass_button = Button(text='Add', width=36, command=save_information)
add_pass_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
