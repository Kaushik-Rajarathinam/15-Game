# author: Kaushik Rajarathinam
# date: March 18, 2023
# file: the fifteen game with GUI
# input: User Interactions with GUI
# output: the game

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen


def onClick(val, x):
    game.update(game.tiles[val])
    update(x)

def shuffle(x):
    game.shuffle()
    onClick(i, x)

def update(x):
    for i in range(x):
        if game.tiles[i] == 0:
            buttons[i].config(text=' ',  bg='#ECE63D')
        else:
            buttons[i].config(text=str(game.tiles[i]), bg='#ECE63D')
    if game.is_solved():
        startButton.config(width=5, height=2, text='Solved! \n Play Again?')
        # print('Game Solved')
        gui.tk_setPalette(background='#880808')
        for i in range(x):
            buttons[i].config(fg='green', bg='#880808')
    else:
        startButton.config(width=0, height=0, text='Shuffle')
        gui.tk_setPalette(background='#880808')
        for i in range(x):
            buttons[i].config(fg='#880808')



if __name__ == '__main__':
    game = Fifteen(4) # You can input any number here to generate any sized grid, but leave the arguments blank to generate the classic 15 board.
    gui = Tk()
    gui.title("Fifteen")
    display = Entry(gui)
    display.grid(row=0, column=0, columnspan=game.size)
    font = font.Font(family='Fixedsys', size='30', weight='bold')

    # create buttons
    buttons = []
    for i in range(game.size**2):
        if game.tiles[i] != 0:
            text = str(game.tiles[i])
        else:
            text = ' '
        buttons.append(Button(gui, text=text, font=font, height=2, width=5, padx=0, command=lambda i=i: onClick(i, game.size**2)))
        buttons[i].grid(row=i//game.size, column=i%game.size, sticky='nesw')
        buttons[i].config(bg='#ECE63D', fg='#ECE63D', bd=10)
        gui.nametowidget(buttons[i].winfo_name()).grid(row=i//game.size, column=i % game.size, sticky='nesw')


    startButton = Button(gui, text='Click to Start',fg='#ECE63D', bg='#880808', font=font, height=0, width=0, padx=0, command=lambda: shuffle(game.size**2))
    startButton.grid(row=game.size, column=0, columnspan=game.size,sticky='nesw')
    gui.mainloop()
