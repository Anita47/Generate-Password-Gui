from tkinter import *
from tkinter import messagebox
import random
def password():

    #8print("Welcome to the pypassword Generator")
    user_range=int(10)
    user_symbols=int(2)
    user_number=int(3)
    letter='abcdefghijklmnopqrstuvwxyz'
    cap_letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols="!@#$%^&*"
    number_num='1234567890'

    total=user_symbols+user_number
    total_letter=user_range-total

    password=[]

    p=0
    j=0

    for i in range(1):
        for k in range(total_letter):
            number=random.randint(0,25)
            number1=random.randint(1,2)
            if number1==1:
                password.append(letter[number])
            else:
                password.append(cap_letter[number])

            for l in range(1,user_symbols+1):
                if p==1:
                   break
                number=random.randint(0,7)
                password.append(symbols[number])
            p=1
            for f in range(user_number):
                if j==1:
                    break
                number=random.randint(0,9)
                password.append(number_num[number])
            j=1

    random.shuffle(password)
    password_list=''
    for char in password:
        password_list+=char
    password_entry.insert(0,password_list)








def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()


    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title='Ooops',message="Please make sure you haven't left any field empty")
    else:
        is_ok=messagebox.askokcancel(title=website ,message=f"These are the details entered: \nEmail: {email}" f"\npassword: {password} \n Is it ok to save?")
        


        if is_ok:
            with open('data.txt','a') as data_file:
                data_file.write(f"{website} | {email} | {password}\n") 
                website_entry.delete(0,END)
                password_entry.delete(0,END)
            
    
    




    

window=Tk()

window.title("Password Manager")

window.config(padx=20,pady=20)

canvas=Canvas(height=200,width=200)

logo_img=PhotoImage(file='logo.png')

canvas.create_image(100,100,image=logo_img)
canvas.pack()
canvas.grid(row=0,column=1)


#Lables
website_label=Label(text='Website:')
website_label.grid(row=1,column=0)

email_label=Label(text='Email/Username:')
email_label.grid(row=2,column=0)

password_label=Label(text='Password:')
password_label.grid(row=3,column=0)


#Entries
website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()


email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"kumarianitakumari111@.gmail.com")



password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)


#buttons
generate_password_button=Button(text='Generate Paassword',command=password)
generate_password_button.grid(row=3,column=2)

add_button=Button(text='Add' ,width=35,command=save)
add_button.grid(row=4,column=1,columnspan=2)








window.mainloop()
