from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter import Menu
from tkinter import Radiobutton
from tkinter import scrolledtext
from tkinter.ttk import Combobox
window = Tk()
window.title("Быцань Алёна Ивановна")
window.geometry('400x350')
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1,text='1')
tab_control.add(tab2,text='2')
tab_control.add(tab3,text='3')
tab_control.pack(expand=1,fill='both')
number_1=Entry(tab1,width=5)
number_1.grid(column= 0,row = 0)
number_2 = Entry(tab1,width=10)
number_2.grid(column=2,row=0)
def click1():
    b=0
    c=number_1.get()
    d=number_2.get()
    z=combox.get()
    if z=='*':
        b=int(c) * int(d)
    elif z=='/':
        b=int(c)/int(d)
    elif z=='+':
        b=int(c)+int(d)
    elif z=='-':
        b=int(c)-int(d)
    label_1['text']=b
button_1=Button(tab1,text='=',command=click1)
button_1.grid(column=3,row=0)
combox = Combobox(tab1)
combox['values']=('*','/','+','-')
combox.grid(column=1,row=0)
combox.current(0)
label_1=Label(tab1,text='')
label_1.grid(column=4,row=0)
def click3():
    txt.delete('1.0',END)
    a=filedialog.askopenfilename(filetypes=(("Text files", "*.txt"),("All files", "*.*")))
    file=open(a,'r')
    lines=file.readlines()
    row=len(lines)
    for i in range(row):
        txt.insert(INSERT, lines[i])
menu = Menu(tab3)
new_item = Menu(menu)
menu.add_cascade(label='главное меню',menu=new_item)
new_item.add_command(label='добавить файл',command=click3)
new_item.add_separator()
window.config(menu=menu)
def click2():
    messagebox.showinfo('ответ',' вы выбрали '+str(selected.get())+' вариант ответа')
selected = StringVar()
radiobutton_1 = Radiobutton(tab2,text='1',value='первый',variable=selected)
radiobutton_2 = Radiobutton(tab2,text='2',value='второй',variable=selected)
radiobutton_3 = Radiobutton(tab2,text='3',value='третий',variable = selected)
radiobutton_1.grid(column=0,row=1)
radiobutton_2.grid(column=0,row=2)
radiobutton_3.grid(column=0,row=3)
button_2 = Button(tab2,text='перейти к ответу',command = click2)
button_2.grid(column=0,row=4)
txt = scrolledtext.ScrolledText(tab3, width=100, height=100)
txt.grid(column=0,row=0)
window.mainloop()