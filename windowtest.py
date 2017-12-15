from tkinter import Tk, Label, Button
import random

class MyFirstGUI:


       
    def main():
        frame=Tk()
        frame.title("Some buttons")
        frame.label = Label(frame, text="This is our first GUI!")
        frame.label.pack()
        new_label=Label(frame, text="")
        x="failed"
        def flip(frame):
            coin=["heads","tails"]
            global x
            x = random.choice(coin)
            new_label.configure(frame, text="".join(x))
        frame.greet_button = Button(frame, text="flip a coin", command=flip(frame))
        frame.greet_button.pack()
        new_label=Label(frame, text="")
        new_label.pack()
        def flip(frame):
            new_label=Label(frame, text="")
            new_label.pack()
            coin=["heads","tails"]
            global x
            x = random.choice(coin)
            new_label.configure(text="".join(x))

MyFirstGUI.main()
