import random
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


def load_images(card_images):
    suits=['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    # for each suit, retrieve the image for the cars
    for suit in suits:
        # first the number cards 1 to 10
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        # then face cards
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


# deal cards
def deal_card(frame):
    # pop the next cards off the top of the deck
    next_card = deck.pop(0)
    # and add it to the back of the pack
    deck.append(next_card)
    # add the image to a Label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # return the card's face value
    return next_card


def score_hand(hand):
    #Calculate the total score of all cards in the list
    # Only one ace can be 11, which changes to 1 if the hand goes bust
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            card_value = 11
            ace = True
        score += card_value
        # Check for ace at bust
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    global dealer_record
    global player_record
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set('Dealer Wins!')
        dealer_record += 1
        dealer_record_label.set(dealer_record)
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set('Player Wins!')
        player_record += 1
        player_record_label.set(player_record)
    elif dealer_score > player_score:
        result_text.set('Dealer Wins!')
        dealer_record += 1
        dealer_record_label.set(dealer_record)
    else:
        result_text.set('Draw!')


def deal_player():
    global player_record
    global dealer_record
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_hit_count = 0
    player_hit_count += 1

    player_score_label.set(player_score)
    if player_score == 21 and player_hit_count == 2:
        result_text.set('Blackjack!')
        player_record += 1
        player_record_label.set(player_record)
    elif player_score > 21:
        result_text.set('Dealer Wins!')
        dealer_record += 1
        dealer_record_label.set(dealer_record)

    #
    # global player_score
    # global player_ace
    # card_value = deal_card(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     player_ace = True
    #     card_value = 11
    # player_score += card_value
    # # if bust, check for ace
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set('Dealer wins!')
    # print(locals())


def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand

    # Create a new deck of cards and shuffle 'em
    deck = list(cards)
    random.shuffle(deck)
    #embedded frame to hold the card images
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background='green')
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background='green')
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    result_text.set('')

    # Create the lists to store the dealer's & player's hands
    dealer_hand = []
    player_hand = []
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


# Instantiate screen and frames for the dealer and player
mainWindow = tkinter.Tk()

mainWindow.title('Black Jack')
mainWindow.geometry('640x480')
mainWindow.configure(background='green')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1, background='green')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Dealer', background='green', fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background='green', fg='white').grid(row=1, column=0)
# embedded frame holds the dealer's card images
dealer_card_frame = tkinter.Frame(card_frame, background='green')
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Player', background='green', fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)
# embedded frame holds the player's card images
player_card_frame = tkinter.Frame(card_frame, background='green')
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)
dealer_record_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Dealer Wins', background='green', fg='white').grid(row=0, column=4)
tkinter.Label(card_frame, textvariable=dealer_record_label, background='green', fg='white').grid(row=1, column=4)
player_record_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Player Wins', background='green', fg='white').grid(row=2, column=4)
tkinter.Label(card_frame, textvariable=player_record_label, background='green', fg='white').grid(row=3, column=4)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=2, sticky='w')

dealer_button = tkinter.Button(button_frame, text='Dealer', command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text='Player', command=deal_player)
player_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text='New Game', command=new_game)
new_game_button.grid(row=0, column=2)

# load cards
cards = []
load_images(cards)
print(cards)

# Create a new deck of cards and shuffle 'em
deck = list(cards) + list(cards) + list(cards)
random.shuffle(deck)

# Create the lists to store the dealer's & player's hands
dealer_hand = []
player_hand = []
new_game()

# Create win record
dealer_record = 0
player_record = 0

mainWindow.mainloop()