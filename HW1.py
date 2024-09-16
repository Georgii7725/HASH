import uuid
import hashlib
from tkinter import *
from tkinter.messagebox import showerror, showinfo

def create_password():
    global tlas, password
    tlas = uuid.uuid4()
    password = hashlib.md5((e1.get()+str(tlas)).encode())

def check():
    p = e2.get()
    if password.digest() == hashlib.md5((p+str(tlas)).encode()).digest():
        showinfo("Успех", "Вы ввели верный пароль")
    else:
        showerror("Неудача", "Вы ввели НЕверный пароль")

root = Tk()
root.geometry("400x250+300+400")
e1 = Entry()
e1.grid(row=1, column=1)
e2 = Entry()
e2.grid(row=2, column=1)
l = Label().grid(row=1, column=2)
l = Label().grid(row=2, column=2)
b1 = Button(text='Создать пароль', width=30, command=create_password).grid(row=1, column=3)
b2 = Button(text='Проверить пароль', width=30, command=check).grid(row=2, column=3, columnspan=2)

root.mainloop()