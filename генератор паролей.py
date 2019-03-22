import random as r
from tkinter import *
import os

a = ["!", "@", "#", "%", "?", "*"]
b = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]
c = ["a","b","c","d","e","f","g","h","i","g","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
d = ["A","B","C","D","E","F","G","H","I","G","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
sl = ""
pas = []

def exitall(): #функция для закрытия программы по нажатию на кнопку
    tk.destroy()
   
def buttons():
    #функции по генерации пароля         
    def one():
        while len(pas) != 8:
            pas.append(r.choice(a))
            pas.append(r.choice(b))
            pas.append(r.choice(c))
            pas.append(r.choice(d))
        sl = pas[0]+pas[1]+pas[2]+pas[3]+pas[4]+pas[5]+pas[6]+pas[7] 
        my_file = open(f"C:\\Users\\{os.getlogin()}\\Desktop\\пароль.txt", "w" )
        my_file.write(sl)
        my_file.close()
        pas.clear()
        sl = ""
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        btn4.destroy()
        canvass.delete("all")
        canvass.create_text(192, 50, text = "Я создал пароль и добавил его", font = "arial 18")
        canvass.create_text(149, 100, text = "в папку под названием -", font = "arial 18")
        canvass.create_text(335, 100, text = "Пароль", font = "arial 19")
        canvass.create_text(192, 150, text = "   Файл с паролем находится на рабочем столе", font = "arial 14")
        canvass.create_text(192, 200, text = "Спасибо за использование программы)", font = "arial 15")
        btn5 = Button(tk, text="Закрыть программу", bg = "grey", fg = "white", command = exitall, width = 20, height = 3)
        btn5.place(x=120, y=250)

    def two():
        while len(pas) != 8:
            pas.append(r.choice(c))
            pas.append(r.choice(d))
        sl = pas[0]+pas[1]+pas[2]+pas[3]+pas[4]+pas[5]+pas[6]+pas[7] 
        my_file = open(f"C:\\Users\\{os.getlogin()}\\Desktop\\пароль.txt", "w" )
        my_file.write(sl)
        my_file.close()
        pas.clear()
        sl = ""
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        btn4.destroy()
        canvass.delete("all")
        canvass.create_text(192, 50, text = "Я создал пароль и добавил его", font = "arial 18")
        canvass.create_text(149, 100, text = "в папку под названием -", font = "arial 18")
        canvass.create_text(335, 100, text = "Пароль", font = "arial 19")
        canvass.create_text(192, 150, text = "   Файл с паролем находится на рабочем столе", font = "arial 14")
        canvass.create_text(192, 200, text = "Спасибо за использование программы)", font = "arial 15")
        btn5 = Button(tk, text="Закрыть программу", bg = "grey", fg = "white", command = exitall, width = 20, height = 3)
        btn5.place(x=120, y=250)

    def three():    
        while len(pas) != 9:
            pas.append(r.choice(b))
            pas.append(r.choice(c))
            pas.append(r.choice(d))
        sl = pas[0]+pas[1]+pas[2]+pas[3]+pas[4]+pas[5]+pas[6]+pas[7] 
        my_file = open(f"C:\\Users\\{os.getlogin()}\\Desktop\\пароль.txt", "w" )
        my_file.write(sl)
        my_file.close()
        pas.clear()
        sl = ""
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        btn4.destroy()
        canvass.delete("all")
        canvass.create_text(192, 50, text = "Я создал пароль и добавил его", font = "arial 18")
        canvass.create_text(149, 100, text = "в папку под названием -", font = "arial 18")
        canvass.create_text(335, 100, text = "Пароль", font = "arial 19")
        canvass.create_text(192, 150, text = "   Файл с паролем находится на рабочем столе", font = "arial 14")
        canvass.create_text(192, 200, text = "Спасибо за использование программы)", font = "arial 15")
        btn5 = Button(tk, text="Закрыть программу", bg = "grey", fg = "white", command = exitall, width = 20, height = 3)
        btn5.place(x=120, y=250)

    def four():
        while len(pas) != 8:
            pas.append(r.choice(b))
        canvass.create_text(150, 322, text = "Я создал пароль и добавил его в папку 'пароль'")
        sl = pas[0]+pas[1]+pas[2]+pas[3]+pas[4]+pas[5]+pas[6]+pas[7] 
        my_file = open(f"C:\\Users\\{os.getlogin()}\\Desktop\\пароль.txt", "w" )
        my_file.write(sl)
        my_file.close()
        pas.clear()
        sl = ""
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        btn4.destroy()
        canvass.delete("all")
        canvass.create_text(192, 50, text = "Я создал пароль и добавил его", font = "arial 18")
        canvass.create_text(149, 100, text = "в папку под названием -", font = "arial 18")
        canvass.create_text(335, 100, text = "Пароль", font = "arial 19")
        canvass.create_text(192, 150, text = "   Файл с паролем находится на рабочем столе", font = "arial 14")
        canvass.create_text(192, 200, text = "Спасибо за использование программы)", font = "arial 15")
        btn5 = Button(tk, text="Закрыть программу", bg = "grey", fg = "white", command = exitall, width = 20, height = 3)
        btn5.place(x=120, y=250)

    #создание 2 части программы        
    btnstart.destroy()
    btnexit.destroy()
    canvass.delete("all")
    canvass.create_text(205, 12, text = "Пароль из символов букв и цифр.", font = "arial 17")
    canvass.create_text(115, 112, text = "Пароль из букв.", font = "arial 18")
    canvass.create_text(159, 212, text = "Пароль из букв и цифр.", font = "arial 18")
    canvass.create_text(120, 312, text = "Пароль из цифр.", font = "arial 18")

    btn1 = Button(tk, text="1", bg = "grey", fg = "white", command=one)
    btn1.place(x=0, y=0)


    btn2 = Button(tk, text="2", bg = "grey", fg = "white", command=two)
    btn2.place(x=0, y=100)

    btn3 = Button(tk, text="3", bg = "grey", fg = "white", command=three)
    btn3.place(x=0, y=200)

    btn4 = Button(tk, text="4", bg = "grey", fg = "white", command=four)
    btn4.place(x=0, y=300)


#начальное окно приложения
tk = Tk()
tk.title("ГЕНЕРАТОР ПАРОЛЕЙ")
tk.resizable(False,False)
tk.geometry("400x327+400+200")
canvass = Canvas(tk, width=400, height=335,)
canvass.pack()
canvass.create_text(200, 30, text = "Генератор паролей", font = "arial 30")
btnstart = Button(tk, text="Генерация пароля", width = 19, height = 3, font = "arial 15", bg = "grey",fg = "white", command = buttons)
btnstart.place(x = 93, y = 100)
btnexit = Button(tk, text="Выход", width = 19, height = 3, font = "arial 15", bg = "grey", fg = "white", command = exitall)
btnexit.place(x = 93, y = 190)
tk.mainloop()


     
    
    


    
    


        
