from tkinter import *
from app import App
import requests


try:
    all_words = open('word_list.txt', 'r')
except FileNotFoundError:
    words = requests.get('https://random-word-api.herokuapp.com/all')
    all_words = open('word_list.txt', 'w+')
    for word in words.json():
        all_words.write(word + '\n')
finally:
    with open('word_list.txt', 'r') as data_file:
        word_list = [word.strip('\n') for word in data_file if len(word) < 8]

window = Tk()
window.title('Pocket Speed Test')
window.minsize(400, 600)
window.config(bg='#F0D9FF')
window.resizable(width=False, height=False)

BTN_IMG = PhotoImage(file='images/button_start.png')
TEXT_IMG = PhotoImage(file='images/text_box.png')
HVR_IMG = PhotoImage(file='images/button_hover.png')
CIRCLE_IMG = PhotoImage(file='images/circle.png')


app = App(window,
          btn_img=BTN_IMG,
          text_img=TEXT_IMG,
          hvr_img=HVR_IMG,
          words=word_list,
          circle=CIRCLE_IMG)

window.mainloop()
