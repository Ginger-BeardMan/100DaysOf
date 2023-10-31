import tkinter
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# website label
website = Label(text='Website:')
website.grid(column=0, row=1, pady=2)

# website entry
website_entry = Entry(width=43)
website_entry.grid(column=1, row=1, columnspan=2, pady=2, padx=5, sticky=tkinter.EW)

# email/username label
email_username = Label(text='Email/Username:')
email_username.grid(column=0, row=2, pady=2)

# email/username entry
email_username_entry = Entry(width=43)
email_username_entry.grid(column=1, row=2, columnspan=2, pady=2, padx=5, sticky=tkinter.EW)

# password label
new_pass = Label(text='Password:')
new_pass.grid(column=0, row=3, pady=2)

# password entry
new_pass_result = Entry(width=20)
new_pass_result.config(highlightthickness=0)
new_pass_result.grid(column=1, row=3, pady=2, padx=5, sticky=tkinter.W)

# generate password button
gen_pass_button = Button(text='Generate Password', width=14)
gen_pass_button.config(highlightthickness=0)
gen_pass_button.grid(column=2, row=3, pady=2, padx=0, sticky=tkinter.W)

# add button
add_pass_button = Button(text='Add', width=40)
add_pass_button.grid(column=1, row=4, columnspan=2, pady=2)

window.mainloop()
