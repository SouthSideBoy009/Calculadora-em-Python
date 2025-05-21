from tkinter import *
from tkinter import ttk


# janela calculadora
window = Tk()
window.title("calculadora")
window.geometry("235x318")
window.config(bg='black')

# onde os numeros vao aparecer
display = Frame(window, width=235, height=50, bg='green')
display.grid(row=0, column=0)

# parte em que os botoes vao ficar
body = Frame(window, width=235, height=268)
body.grid(row=1, column=0)

# função para mostrar os valores
all_values = ''

def show_values(value):
    global all_values
    all_values = all_values + str(value)

    #passando valores para tela 
    text_value.set(all_values)

# função para as operaçoes aritmeticas
def calculate():
    global all_values
    result = eval(all_values)
    text_value.set(str(result))

# função para limpar a tela
def clear():
    global all_values
    all_values = ''
    text_value.set('')

# criação de label
text_value = StringVar()

app_label = Label(display,fg='white' ,textvariable=text_value, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg='green')
app_label.place(x=0, y=0)


# criação de botões
# 1º camada

button_clear = Button(body, command=clear,text='C', width=11, height=2, bg='gray', fg='black', 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_clear.place(x=0, y=0)

button_percent = Button(body, command=lambda: show_values('%') ,text='%', width=5, height=2, bg='gray', fg='black', 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_percent.place(x=118, y=0)

button_divide = Button(body, command=lambda: show_values('/') , text='/', width=5, height=2, bg='orange', fg='white', 
                       font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_divide.place(x=177, y=0)

# 2º camada

button_7 = Button(body, command=lambda: show_values('7') , text='7', width=5, height=2, bg='gray', fg='black', 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_7.place(x=0, y=52)

button_8 = Button(body, command=lambda: show_values('8') , text='8', width=5, height=2, bg='gray', fg='black', 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_8.place(x=59, y=52)

button_9= Button(body, command=lambda: show_values('9') , text='9', width=5, height=2, bg='gray', fg='black', 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_9.place(x=118, y=52)

button_times = Button(body, command=lambda: show_values('*') , text='*', width=5, height=2, bg='orange', fg='white', 
                       font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_times.place(x=177, y=52)

# 3º camada de botoes

button_4 = Button(body, command=lambda: show_values('4') , text='4', width=5, height=2, bg='gray', fg='black', 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_4.place(x=0, y=104)

button_5 = Button(body, command=lambda: show_values('5') , text='5', width=5, height=2, bg='gray', fg='black', 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_5.place(x=59, y=104)

button_6= Button(body, command=lambda: show_values('6') , text='6', width=5, height=2, bg='gray', fg='black', 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_6.place(x=118, y=104)

button_minus = Button(body, command=lambda: show_values('-') , text='-', width=5, height=2, bg='orange', fg='white', 
                       font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_minus.place(x=177, y=104)

# 4º camada de botoes

button_1 = Button(body, command=lambda: show_values('1') , text='1', width=5, height=2, bg='gray', fg='black', 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_1.place(x=0, y=156)

button_2 = Button(body, command=lambda: show_values('2') , text='2', width=5, height=2, bg='gray', fg='black', 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_2.place(x=59, y=156)

button_3 = Button(body, command=lambda: show_values('3') , text='3', width=5, height=2, bg='gray', fg='black', 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_3.place(x=118, y=156)

button_plus = Button(body, command=lambda: show_values('+') , text='+', width=5, height=2, bg='orange', fg='white', 
                       font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_plus.place(x=177, y=156)

# 5º camada

button_0 = Button(body, command=lambda: show_values('0') , text='0', width=11, height=2, bg='gray', fg='black', 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_0.place(x=0, y=208)

button_dot = Button(body, command=lambda: show_values('.') , text='.', width=5, height=2, bg='gray', fg='black', 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_dot.place(x=118, y=208)

button_equals = Button(body, command=calculate, text='=', width=5, height=2, bg='orange', fg='white', 
                       font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_equals.place(x=177, y=208)






window.mainloop()