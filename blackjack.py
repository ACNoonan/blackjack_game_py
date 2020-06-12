import random
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title('Black Jack')
mainWindow.geometry('640x480')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)

card_frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1, background='green')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Dealer', background='green', fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, text=dealer_score_label, background='green', fg='white').grid(row=1, column=0)
# embedded frame holds the dealer's card images
dealer_card_frame = tkinter.Frame(card_frame, background='green')
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Player', background='green', fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)
# embedded frame holds the player's card images
player_card_frame = tkinter.Frame(card_frame, background='green')
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspace=2, sticky='w')

dealer_button = tkinter.Button(button_frame, text='Dealer')
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text='PLayer')
player_button.grid(row=0, column=1)