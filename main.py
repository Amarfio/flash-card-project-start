from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
current_card = {}
to_learn= {}
try:
# data = pandas.read_csv("data/french_words.csv")
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# print(to_learn)
# print(data)
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    # print(current_card["French"])
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


#the flash card
canvas =Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img =PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_back_img = PhotoImage(file="images/card_back.png")
card_title = canvas.create_text(400, 150, text="title", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#first button
button_one_img = PhotoImage(file="images/wrong.png")
button_one = Button(image=button_one_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
button_one.grid(column=0, row=1)

#second button
button_two_img = PhotoImage(file="images/right.png")
button_two = Button(image=button_two_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
button_two.grid(column=1, row=1)

next_card()

window.mainloop()