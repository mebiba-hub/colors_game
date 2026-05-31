#ranking, opcje(inne języki, tryb dla osób bez ręki, tryb ciemny), koniec gry, start gry

import random
import tkinter as tk

colors = [
    'white',
    'black',
    'red',
    'green',
    'blue',
    'yellow',
    'pink',
    'magenta',
    'cyan',
    'orange',
    'brown'
]

word = ''
color = ''
points = 0
max_time = 30
play_time = 30

czy_gra = False

def next_color():
    global color
    global word

    color = random.choice(colors)
    word = random.choice(colors)

    slowo.config(text=word, fg=color)


def time_left():
    global play_time
    global czy_gra
    if play_time > 0:
        play_time -= 1
        napis.config(text=f"Czas: {play_time} | Punkty: {points}")
        root.after(1000, time_left)
    else:
        czy_gra = False
        slowo.config(text="KONIEC", fg="red")

def opcje():
    optionsy.pack(fill="both", expand=True)

    opcje.pack_forget()
    start_gry.pack_forget()
    napis.pack_forget()

    opcje_powrot.grid(pady=20, padx=5, column=0, row=0)
    zmiana_jezykow.grid(pady=5, padx=5, column=1, row=1)
    polski.grid(pady=5, padx=5, column=0, row=2)
    angielski.grid(pady=5, padx=5, column=1, row=2)
    niemiecki.grid(pady=5, padx=5, column=2, row=2)


def check_answer():
    global points
    if pole.get().lower() == color:
        points += 1

    pole.delete(0, tk.END)
    next_color()

def check_click(event):
    global czy_gra
    if czy_gra:
        start_game()
    else:
        pass

def start_game():
    global play_time
    global czy_gra
    czy_gra = True
    if play_time == max_time:
        slowo.pack(pady=5, padx=5, side=tk.TOP)
        pole.pack(pady=5, padx=5, side=tk.TOP)
        pole.focus_set()

        start_gry.pack_forget()
        opcje.pack_forget()

        time_left()
        next_color()
    else:
        check_answer()


root = tk.Tk()
root.geometry('500x400')

optionsy = tk.Canvas(root, width=500, height=400)

#napisy
napis = tk.Label(root, text='KOLOLOLKI', font=('Comic Sans MS', 15))
napis.pack(pady=5, padx=5, side=tk.TOP)

zmiana_jezykow = tk.Label(optionsy, font=('Comic Sans MS', 8), text="Wybierz język z poniższych: ")

#języki
polski = tk.Button(optionsy, font=('Comic Sans MS', 10), text="Polski", bg='white')

angielski = tk.Button(optionsy, font=('Comic Sans MS', 10), text="Angielski", bg='white')

niemiecki = tk.Button(optionsy, font=('Comic Sans MS', 10), text="Niemiecki", bg='white')

#przyciski główne
start_gry = tk.Button(root, text='Rozpocznij grę', command=start_game, fg='white', bg='green', width=15, height=2)
start_gry.pack(pady=5, padx=5, side=tk.TOP)

opcje = tk.Button(root, text='Opcje', fg='white', bg='blue', width=15, height=2, command=opcje)
opcje.pack(pady=5, padx=5, side=tk.TOP)

opcje_powrot = tk.Button(optionsy, text='Powrót', fg='white', bg='red', width=5, height=1)

#mechaniczne do gry
slowo = tk.Label(root, font=('Comic Sans MS', 15))

pole = tk.Entry(root, font=('Comic Sans MS', 10))


root.bind('<Return>', check_click)

root.mainloop()