from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

new_letters = [random.choice(letters) for let in range(nr_letters)]

new_symbols = [random.choice(symbols) for sym in range(nr_symbols)]

new_numbers = [random.choice(numbers) for num in range(nr_numbers)]

password_list = new_letters + new_symbols + new_numbers

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_information():

    website_address = website_entry.get()
    username_email = email_username_entry.get()
    password = new_pass_result.get()

    if len(website_address) == 0 or len(password) == 0:
        messagebox.showinfo(title='Warning', message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website_address,
                                       message=f'These are the details entered:\nEmail: {username_email}'
                                               f'\n Password: {password} \n Is this okay to save?')

        if is_ok:
            with open("data.txt", 'a') as new_passwords:
                new_passwords.write(f"{website_address} | {username_email} | {password}\n")
                website_entry.delete(0, END)
                new_pass_result.delete(0, END)

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
website_entry = Entry(width=39)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

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
new_pass_result = Entry(width=21)
new_pass_result.grid(column=1, row=3)

# generate password button
gen_pass_button = Button(text='Generate Password', width=13)
gen_pass_button.grid(column=2, row=3)

# add button
add_pass_button = Button(text='Add', width=36, command=save_information)
add_pass_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
