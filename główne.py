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

pl = {
    'white':'biały',
    'black':'czarny',
    'red':'czerwony',
    'green':'zielony',
    'blue':'niebieski',
    'yellow':'żółty',
    'pink':'różowy',
    'magenta':'purpura',
    'cyan':'cyjan',
    'orange':'pomarańczowy',
    'brown':'brązowy'
}

de = {
    'white': 'weiß',
    'black': 'schwarz',
    'red': 'rot',
    'green': 'grün',
    'blue': 'blau',
    'yellow': 'gelb',
    'pink': 'rosa',
    'magenta': 'magenta',
    'cyan': 'cyan',
    'orange': 'orange',
    'brown': 'braun'
}

word = ''
color = ''
points = 0
max_time = 30
play_time = 30
language = "en"

czy_gra = False

def set_language(lang):
    global language
    language = lang

def next_color():
    global color
    global word

    color = random.choice(colors)
    word = random.choice(colors)

    if language == "pl":
        display_word = pl[word]
    elif language == "de":
        display_word = de[word]
    else:
        display_word = word

    slowo.config(text=display_word, fg=color)


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
        pole.pack_forget()
        wroc.pack(pady=5, padx=5, side=tk.TOP)


def pokarz_opcje():
    optionsy.pack(fill="both", expand=True)

    opcje.pack_forget()
    start_gry.pack_forget()
    napis.pack_forget()

    opcje_powrot.grid(pady=20, padx=5, column=0, row=0)

    zmiana_jezykow.grid(pady=5, padx=5, column=2, row=1)
    polski.grid(pady=5, padx=5, column=1, row=2)
    angielski.grid(pady=5, padx=5, column=2, row=2)
    niemiecki.grid(pady=5, padx=5, column=3, row=2)

def powrot():
    global play_time
    global points

    optionsy.pack_forget()
    wroc.pack_forget()
    slowo.pack_forget()
    play_time = 30
    points = 0
    napis.config(text='KOLOLOLKI')

    napis.pack(pady=5, padx=5, side=tk.TOP)
    start_gry.pack(pady=5, padx=5, side=tk.TOP)
    opcje.pack(pady=5, padx=5, side=tk.TOP)

def check_answer():
    global points

    answer = pole.get().lower()

    if language == "pl":
        correct = pl[color]
    elif language == "de":
        correct = de[color]
    else:
        correct = color

    if answer == correct:
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
polski = tk.Button(optionsy, font=('Comic Sans MS', 10), text="Polski", bg='white', command=lambda: set_language("pl"))

angielski = tk.Button(optionsy, font=('Comic Sans MS', 10), text="Angielski", bg='white', command=lambda: set_language("en"))

niemiecki = tk.Button(optionsy, font=('Comic Sans MS', 10), text="Niemiecki", bg='white', command=lambda: set_language("de"))

#przyciski główne
start_gry = tk.Button(root, text='Rozpocznij grę', command=start_game, fg='white', bg='green', width=15, height=2)
start_gry.pack(pady=5, padx=5, side=tk.TOP)

opcje = tk.Button(root, text='Opcje', fg='white', bg='blue', width=15, height=2, command=pokarz_opcje)
opcje.pack(pady=5, padx=5, side=tk.TOP)

opcje_powrot = tk.Button(optionsy, text='Powrót', fg='white', bg='red', width=5, height=1, command=powrot)

wroc = tk.Button(root, text='wróć', fg='black', bg='yellow', width=10, height=1, command=powrot)

#mechaniczne do gry
slowo = tk.Label(root, font=('Comic Sans MS', 15))

pole = tk.Entry(root, font=('Comic Sans MS', 10))


root.bind('<Return>', check_click)

root.mainloop()
