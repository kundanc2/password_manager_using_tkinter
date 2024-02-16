import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json

END="end"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_entry.delete(0,END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    web_name=web_entry.get()
    eu=eu_entry.get()
    password=password_entry.get()
    # is_empty=True
    # if web_name!="" and eu!="" and password!="":
    #     is_empty=False
    # if is_empty==False:
    #      is_ok=messagebox.askokcancel(title=web_name,message=f"Email: {eu}\n Password: {password}\nDo you want to save?")
    #      if is_ok:
    #         with open("./saved_passwords.txt","a") as paswdfile:
    #             paswdfile.write(f"{web_name} | {eu} | {password}\n")
    #             web_entry.delete(0, END)
    #             eu_entry.delete(0,END)
    #             password_entry.delete(0,END)
    #             web_entry.focus()    
    # else:
    #     messagebox.showwarning(title="Empty field",message="Website/Email/Password can not be empty")
    new_data={
         web_name:{
              "email":eu,
              "password":password
         }
    }
    try:
        with open("./password.json","r") as paswdfile:
                data=json.load(paswdfile)
                data.update(new_data)
    except FileNotFoundError:
        with open("./password.json","w") as paswdfile:
            json.dump(new_data, paswdfile,indent=4)
    else:
        with open("./password.json","w") as paswdfile:
            json.dump(data, paswdfile,indent=4)
    finally:        
        web_entry.delete(0, END)
        eu_entry.delete(0,END)
        password_entry.delete(0,END)
        web_entry.focus()    


# ---------------------------- search password ------------------------------- #
def search_password():
    try:
        with open("./password.json","r") as paswdfile:
            data=json.load(paswdfile)
    except FileNotFoundError:
        messagebox.showwarning(title=" ",message="NO PASSWORDS WET")
    else:
        website=web_entry.get()
        try:
            email=data[website]["email"]
            password=data[website]["password"]
        except KeyError:
            messagebox.showwarning(title="password not found!",message=f"NO PASSWORDS FOR {website} !")
        else:
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
        



# ---------------------------- UI SETUP ------------------------------- #

window=tk.Tk()
window.title("Password Mannager")
window.config(padx=50,pady=50)

canvas=tk.Canvas()
canvas.config(width=200,height=200)
canvas.grid(row=0,column=1)

website_label=tk.Label(text="Website:")
website_label.grid(row=1,column=0)
web_entry=tk.Entry(width=30)
web_entry.grid(row=1,column=1)
web_entry.focus()

search_button=tk.Button(text="Search",width=15,command=search_password)
search_button.grid(row=1,column=2)

eu_label=tk.Label(text="Email/Username:")
eu_label.grid(row=2,column=0)
eu_entry=tk.Entry(width=52)
eu_entry.grid(row=2,column=1,columnspan=2)
eu_entry.insert(0,"defaultemail@gamil.com")

password_label=tk.Label(text="Password:")
password_label.grid(row=3,column=0)
password_entry=tk.Entry(width=30)
password_entry.grid(row=3,column=1)

generate_button=tk.Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2)

add_button=tk.Button(text="ADD",width=50,command=save_data)
add_button.grid(row=4,column=1,columnspan=2)

image=tk.PhotoImage(file="./logo.png")
canvas.create_image(100,100,image=image)


window.mainloop()



