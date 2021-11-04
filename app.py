from tkinter import *
import random


class App:

    def __init__(self, window, btn_img, text_img, hvr_img, words, circle):
        # ---------------------------- VARIABLES ------------------------------- #
        self.index = 0
        self.score = 0
        self.animation_time = 3
        self.btn_img = btn_img
        self.hvr_img = hvr_img
        self.circle_img = circle
        self.window = window
        self.user_words = []
        self.words = words
        random.shuffle(self.words)
        # ---------------------------- WIDGETS --------------------------------- #
        self.button = Button(self.window,
                             text='Start',
                             bg='#F0D9FF',
                             bd=0,
                             activebackground='#F0D9FF',
                             command=self.display_info_screen)
        self.button.config(image=self.btn_img)
        self.button.bind('<Enter>', self.button_on_enter)
        self.button.bind('<Leave>', self.button_on_leave)
        self.button.place(x=100, y=250)

        self.canvas = Canvas(self.window,
                             width=400,
                             height=600,
                             bg='#F0D9FF',
                             highlightthickness=0)
        self.info_img = self.canvas.create_image(200, 300, image=text_img)
        self.info_text = self.canvas.create_text(200,
                                                 240,
                                                 text="Press 'space'\nto move onto\nthe next word",
                                                 font=('Montserrat', 30, 'bold'),
                                                 justify='left',
                                                 fill='#262626')

        self.label = Label(self.window,
                           text=f'{self.words[self.index]}',
                           bg='#F0D9FF',
                           fg='#BFA2DB',
                           font=('Montserrat', 50),
                           pady=100)

        self.entry = Entry(self.window, font=('Montserrat', 20),
                           width=15,
                           bd=0,
                           highlightthickness=0,
                           bg='#F3F1F5',
                           fg='#7F7C82')
        self.entry.bind('<KeyRelease-space>', self.next_word)
        self.entry.focus()

    def button_on_enter(self, event):
        self.button.config(image=self.hvr_img)

    def button_on_leave(self, event):
        self.button.config(image=self.btn_img)

    def display_info_screen(self):
        self.button.destroy()
        self.canvas.place(x=0, y=0)
        self.canvas.after(2000, self.display_countdown)
        self.window.after(120000, self.display_results_screen)

    def display_countdown(self):
        self.canvas.itemconfig(self.info_text, text=f'{self.animation_time}', font=('Montserrat', 60, 'bold'))
        if self.animation_time > 0:
            self.animation_time -= 1
            self.canvas.after(1000, self.display_countdown)
        else:
            self.canvas.place_forget()
            self.display_typing_screen()

    def next_word(self, event):
        self.user_words.append(self.entry.get().strip(' '))
        if self.words[self.index] == self.user_words[self.index]:
            self.score += 1
        self.entry.delete(0, END)
        self.index += 1
        self.label.config(text=f'{self.words[self.index]}')

    def display_typing_screen(self):
        self.label.pack()
        self.entry.pack()

    def display_results_screen(self):
        self.label.pack_forget()
        self.entry.pack_forget()
        self.canvas.delete(self.info_img, self.info_text)
        self.canvas.create_text(150,
                                50,
                                text='Results',
                                font=('Montserrat', 50),
                                fill='#BFA2DB')
        self.canvas.create_text(150,
                                200,
                                text=f'{self.score}\nWPM',
                                font=('Montserrat', 30),
                                fill='#BFA2DB',
                                justify='center')
        self.canvas.config(bg='#F0D9FF', width=300, height=500)
        self.canvas.create_image(150, 200, image=self.circle_img)
        self.canvas.create_text(150,
                                400,
                                text=f'{round(self.score/self.index * 100)}%\nACC',
                                font=('Montserrat', 30),
                                fill='#BFA2DB',
                                justify='center')
        self.canvas.create_image(150, 400, image=self.circle_img)
        self.canvas.place(x=50, y=50)

