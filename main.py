import tkinter as tk
from tkinter import *
import os
from time import strftime
import locale

root = tk.Tk()
root.title('Relógio digital')
root.geometry("600x320")
root.maxsize(600, 320)
root.minsize(600, 320)
root.configure(background='#1d1d1d')

light = PhotoImage(file='light.png')
dark = PhotoImage(file='dark.png')

# FUNÇÃO
def toggle_dark_mode():
    if root['bg'] == '#1d1d1d':
        root['bg'] = 'white'
        margem['bg'] = 'white'
        saudacao['bg'] = 'white'
        data['bg'] = 'white'
        horario['bg'] = 'white'
        dark_mode_button['image'] = light
        dark_mode_button['bg'] = 'white'
    else:
        root['bg'] = '#1d1d1d'
        margem['bg'] = '#1d1d1d'
        saudacao['bg'] = '#1d1d1d'
        data['bg'] = '#1d1d1d'
        horario['bg'] = '#1d1d1d'
        dark_mode_button['image'] = dark
        dark_mode_button['bg'] = '#1d1d1d'

# def get_saudacao():
#     nome_usuario = os.getlogin()
#     saudacao.config(text='Olá, '  + nome_usuario)
def get_data():
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')
    data_atual = strftime('%A, %d %B %Y')
    data.config(text=data_atual )
def get_horario():
    hora_atual = strftime('%H:%M:%S')
    horario.config(text=hora_atual )
    horario.after(1000, get_horario)

# CONFIGURAÇÕES DA TELA
margem = tk.Canvas(root, width=600, height=40, bg='#1d1d1d',
                    bd=0, highlightthickness=0, relief='ridge')
margem.pack()

# VARIÁVEL
dark_mode_button = Button(root, command=toggle_dark_mode)
dark_mode_button.config(image=dark, bd=0, bg='#1d1d1d')
dark_mode_button.pack(pady=10)

saudacao = Label(root, bg='#1d1d1d', fg='#c8a2c8', font=('Poppins', 18))
saudacao.pack()

data = Label(root, bg='#1d1d1d', fg='#c8a2c8', font=('Poppins', 14))
data.pack(pady=2)

horario = Label(root, bg='#1d1d1d', fg='#c8a2c8', font=('Montserrat', 64, 'bold'))
horario.pack(pady=2)

# ONDE CHAMA A FUNÇÃO PRA APARECER NA TELA
# get_saudacao()
get_data()
get_horario()
root.mainloop()