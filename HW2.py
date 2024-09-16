import uuid
import hashlib
from tkinter import *
from tkinter.messagebox import showerror, showinfo

users = {}

def f(name, info):
    if len(users) == 0:
        users[name] = [len(users), hashlib.md5((e2.get()+str(info)).encode()), info]
    else:
        first_user = list(users.keys())[0]
        old_info = users[first_user][-1]
        users[name] = [len(users), hashlib.md5((e2.get()+str(info)).encode()), old_info]
        users[first_user][-1] = info

def create_password():
    name = e1.get()
    if name in users.keys(): 
        showerror("Ошибка", "Данное имя уже занято")
    else:
        f(name, uuid.uuid4())
    e1.delete(0, END)
    e2.delete(0, END)
    print(users)
    

def check():
    if e3.get() not in users.keys(): 
        showerror("Ошибка", "Такого пользователя не зарегистрировано")
        return
    if users[e3.get()][1].digest() == hashlib.md5((e4.get()+str(users[list(users.keys())[(users[e3.get()][0]+1)%len(users)]][-1])).encode()).digest():
        showinfo("Успех", "Вы авторизовались")
    else:
        showerror("Неудача", "Вы ввели неверный пароль")

root = Tk()
root.geometry("400x250+300+400")

l = Label(text="Регистрация", width=20).grid(row=1, column=1)
e1 = Entry()
e1.grid(row=2, column=1)
e2 = Entry()
e2.grid(row=3, column=1)
l = Label().grid(row=2, column=2)
l = Label().grid(row=3, column=2)
b1 = Button(text='Создать пользователя', width=30, command=create_password).grid(row=2, column=3, rowspan=2)

l = Label(text="Авторизация", width=20).grid(row=4, column=1)
e3 = Entry()
e3.grid(row=5, column=1)
e4 = Entry()
e4.grid(row=6, column=1)
b2 = Button(text='Войти', width=30, command=check).grid(row=5, column=3, columnspan=2)

root.mainloop()

###
# Написанный далее текст раскрывает секрет прятание соли, поэтому если хотите догадаться сами, не читайте дальше
# 
# Соль данного пользователя хронится в информации следующего пользователя. У последнего в первом
# ###