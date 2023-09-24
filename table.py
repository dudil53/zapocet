import random
import time
import os
from tkinter import *
from combinations import *
from images import *
from PIL import ImageTk, Image


class PLAYER(): #player class
    def __init__(self, name, cash):
        self.info = 'Player'
        self.hand = []
        self.next = None
        self.cash = cash
        self.position = None
        self.name = name
        self.cashin = 0
        self.folded = False
        self.played = False
        self.pairs = {}
        self.suits = {}
        self.values = []
        self.hand_to_write = []




class DEALER():#dealer class
    def __init__(self):
        self.info = 'Dealer'
        self.next = None
        self.kolo = 0








def cards(): #this function creates and shuffles a new deck
    deck =[]
    suits = ['hearts', 'diamonds', 'spades', 'clubs']
    for i in range(0,4):
        for j in range(2,15):
            deck.append((j, suits[i]))
    random.shuffle(deck)
    return deck


                
                            
class TKTABLE():#table class
    def __init__(self, root, number :int, names : list, money : int):
        self.root = root
        self.cards = []
        self.cards_to_write = []
        self.trash = 0
        self.dealer = DEALER()
        self.deck = cards()
        self.pot = 0
        self.highest = 0
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.running = True
        self.situation = 'nothing'
        self.winners = []
        self.twins = []
        self.number = number

        if money == 200:
            self.small = 1
            self.big = 2
        elif money == 500:
            self.small = 2
            self.big = 5
        elif money == 1000:
            self.small = 5
            self.big = 10
        else:
            self.small = 50
            self.big = 100

        self.winner_label_var = StringVar()
        self.winner_label = Label(self.root, textvariable=self.winner_label_var, background ='red', font=('Arial', 20))
        self.winner_label.lift()
        

        self.action_var = StringVar()

        self.playing_label_var = StringVar()
        self.playing_label_var.set('')

        self.table_pot_var = StringVar()
        self.table_pot_var.set(f'There is {self.pot} $ on the table')

        #### table cards
        start_mini_image = ImageTk.PhotoImage(small_blank)
        self.first_card_label = Label(self.root, image = start_mini_image, background='lightgray')
        self.first_card_label.place(anchor=CENTER, x=290, y=220)
        self.second_card_label = Label(self.root, image = start_mini_image, background='lightgray')
        self.second_card_label.place(anchor=CENTER, x=370, y=220)
        self.third_card_label = Label(self.root, image = start_mini_image, background='lightgray')
        self.third_card_label.place(anchor=CENTER, x=450, y=220)
        self.fourth_card_label = Label(self.root, image = start_mini_image, background='lightgray')
        self.fourth_card_label.place(anchor=CENTER, x=530, y=220)
        self.fifthcard_label = Label(self.root, image = start_mini_image, background='lightgray')
        self.fifthcard_label.place(anchor=CENTER, x=610, y=220)

        self.playing_label = Label(self.root, textvariable=self.playing_label_var, background='lightgray')
        self.playing_label.place(anchor=W, x=330, y=580)

        start_image = ImageTk.PhotoImage(blank)
        self.playing_cards_label_left = Label(self.root, image = start_image, background='lightgray')
        self.playing_cards_label_left.place(anchor=CENTER, x=390, y=400)
        self.playing_cards_label_right = Label(self.root, image = start_image, background='lightgray')
        self.playing_cards_label_right.place(anchor=CENTER, x=520, y=400)


        self.playing_cashin_var = StringVar()
        self.playing_cashin_label = Label(self.root, textvariable=self.playing_cashin_var, background='lightgray')
        self.playing_cashin_label.place(anchor=CENTER, x=450, y=350)

        self.table_pot_label = Label(self.root, textvariable=self.table_pot_var, background = 'lightgray')
        self.table_pot_label.place(anchor=CENTER, x=450, y=300)



        ### first plater
        self.player_one_var = StringVar()
        self.player_one_var.set(names[0])
        self.player_one_label = Label(self.root, textvariable= self.player_one_var, background = 'lightgray')
        self.player_one_cashin_var = StringVar()
        self.player_one_cashin_label = Label(self.root, textvariable=self.player_one_cashin_var, background='lightgray')
        self.player_one_label.place(anchor=CENTER, x=80, y=250)        
        self.player_one_cashin_label.place(anchor=CENTER, x=150, y=250)
        self.one_left = Label(self.root, background = 'lightgray')
        self.one_right = Label(self.root, background = 'lightgray')
        #avatar1
        avatar1_photo = ImageTk.PhotoImage(avatar1)
        self.player_one_avatar = Label(self.root, image = avatar1_photo, background = 'lightgray')
        self.player_one_avatar.place(anchor=CENTER, x=80, y=180)



        ### second player
        self.player_two_var = StringVar()
        self.player_two_var.set(names[1])
        self.player_two_label = Label(self.root, textvariable= self.player_two_var, background = 'lightgray')
        self.player_two_cashin_var = StringVar()
        self.player_two_cashin_label = Label(self.root, textvariable=self.player_two_cashin_var, background='lightgray')
        self.player_two_label.place(anchor=CENTER, x=820, y=250)
        self.player_two_cashin_label.place(anchor=CENTER, x=730, y=250)
        self.two_left = Label(self.root, background = 'lightgray')
        self.two_right = Label(self.root, background = 'lightgray')
        #avatar2
        avatar2_photo = ImageTk.PhotoImage(avatar2)
        self.player_two_avatar = Label(self.root, image = avatar2_photo, background = 'lightgray')
        self.player_two_avatar.place(anchor=CENTER, x=820, y=180)



        if number >= 3:
            ## third player
            self.player_three_var = StringVar()
            self.player_three_var.set(names[2])
            self.player_three_label = Label(self.root, textvariable= self.player_three_var, background = 'lightgray')
            self.player_three_cashin_var = StringVar()
            self.player_three_cashin_label = Label(self.root, textvariable=self.player_three_cashin_var, background='lightgray')
            ###player two placement
            self.player_two_label.place(anchor=CENTER, x=450, y=130)
            self.player_two_cashin_label.place(anchor=CENTER, x=520, y=130)
            self.player_two_avatar.place(anchor=CENTER, x=450, y=60)
            ###player three placement
            self.player_three_label.place(anchor=CENTER, x=820, y=250)
            self.player_three_cashin_label.place(anchor=CENTER, x=730, y=250)
            self.three_left = Label(self.root, background = 'lightgray')
            self.three_right = Label(self.root, background = 'lightgray')
            #avatar3
            avatar3_photo = ImageTk.PhotoImage(avatar3)
            self.player_three_avatar = Label(self.root, image = avatar3_photo, background = 'lightgray')
            self.player_three_avatar.place(anchor=CENTER, x=820, y=180)

        if number >= 4:
            ## fourth player
            self.player_four_var = StringVar()
            self.player_four_var.set(names[3])
            self.player_four_label = Label(self.root, textvariable= self.player_four_var, background = 'lightgray')
            self.player_four_cashin_var = StringVar()
            self.player_four_cashin_label = Label(self.root, textvariable=self.player_four_cashin_var, background='lightgray')
            ###player two placement
            self.player_two_label.place(anchor=CENTER, x=300, y=130)
            self.player_two_cashin_label.place(anchor=CENTER, x=370, y=130)
            self.player_two_avatar.place(anchor=CENTER, x=300, y=60)
            ###player three placement
            self.player_three_label.place(anchor=CENTER, x=600, y=130)
            self.player_three_cashin_label.place(anchor=CENTER, x=670, y=130)
            self.player_three_avatar.place(anchor=CENTER, x=600, y=60)
            ###player four placement
            self.player_four_label.place(anchor=CENTER, x=820, y=250)
            self.player_four_cashin_label.place(anchor=CENTER, x=730, y=250)
            self.four_left = Label(self.root, background = 'lightgray')
            self.four_right = Label(self.root, background = 'lightgray')
            #avatar4
            avatar4_photo = ImageTk.PhotoImage(avatar4)
            self.player_four_avatar = Label(self.root, image = avatar4_photo, background = 'lightgray')
            self.player_four_avatar.place(anchor=CENTER, x=820, y=180)

        if number >= 5:
            ### fifth player
            self.player_five_var = StringVar()
            self.player_five_var.set(names[4])
            self.player_five_label = Label(self.root, textvariable= self.player_five_var, background = 'lightgray')
            self.player_five_cashin_var = StringVar()
            self.player_five_cashin_label = Label(self.root, textvariable=self.player_five_cashin_var, background='lightgray')
            ###player one placement
            self.player_one_label.place(anchor=CENTER, x=80, y=325)        
            self.player_one_cashin_label.place(anchor=CENTER, x=150, y=325)
            self.player_one_avatar.place(anchor=CENTER, x=80, y=255)
            ###player two placement
            self.player_two_label.place(anchor=CENTER, x=80, y=130)        
            self.player_two_cashin_label.place(anchor=CENTER, x=150, y=130)
            self.player_two_avatar.place(anchor=CENTER, x=80, y=60)
            ###player three placement
            self.player_three_label.place(anchor=CENTER, x=300, y=130)
            self.player_three_cashin_label.place(anchor=CENTER, x=370, y=130)
            self.player_three_avatar.place(anchor=CENTER, x=300, y=60)
            ###player four placement
            self.player_four_label.place(anchor=CENTER, x=600, y=130)
            self.player_four_cashin_label.place(anchor=CENTER, x=670, y=130)
            self.player_four_avatar.place(anchor=CENTER, x=600, y=60)
            ###player five placement
            self.player_five_label.place(anchor=CENTER, x=820, y=250)
            self.player_five_cashin_label.place(anchor=CENTER, x=730, y=250)
            self.five_left = Label(self.root, background = 'lightgray')
            self.five_right = Label(self.root, background = 'lightgray')
            #avatar5
            avatar5_photo = ImageTk.PhotoImage(avatar5)
            self.player_five_avatar = Label(self.root, image = avatar5_photo, background = 'lightgray')
            self.player_five_avatar.place(anchor=CENTER, x=820, y=180)

        if number == 6:
            ### sixth player
            self.player_six_var = StringVar()
            self.player_six_var.set(names[5])
            self.player_six_label = Label(self.root, textvariable= self.player_six_var, background = 'lightgray')
            self.player_six_cashin_var = StringVar()
            self.player_six_cashin_label = Label(self.root, textvariable=self.player_six_cashin_var, background='lightgray')
            ###player five placement
            self.player_five_label.place(anchor=CENTER, x=820, y=130)
            self.player_five_cashin_label.place(anchor=CENTER, x=730, y=130)
            self.player_five_avatar.place(anchor=CENTER, x=820, y=60)
            ###player six placement
            #self.player_six_cards_label.place(anchor=CENTER, x=820, y=350)
            self.player_six_label.place(anchor=CENTER, x=820, y=325)
            self.player_six_cashin_label.place(anchor=CENTER, x=730, y=325)
            self.six_left = Label(self.root, background = 'lightgray')
            self.six_right = Label(self.root, background = 'lightgray')
            #avatar6
            avatar6_photo = ImageTk.PhotoImage(avatar6)
            self.player_six_avatar = Label(self.root, image = avatar6_photo, background = 'lightgray')
            self.player_six_avatar.place(anchor=CENTER, x=820, y=255)

        ### action buttons
        self.call_button = Button(self.root, text='CALL', width=15, height=2, command = lambda: self.action_var.set('call'))
        self.check_button = Button(self.root, text='CHECK', width=15, height=2, command = lambda: self.action_var.set('check'))
        self.raise_button = Button(self.root, text='RAISE', width=15, height=2, command = lambda: self.action_var.set('raise'))
        self.allin_button = Button(self.root, text='ALL IN', command = lambda: self.action_var.set('allin'))
        self.fold_button = Button(self.root, text='FOLD', width=15, height=2, command = lambda: self.action_var.set('fold'))


        




        ### creating the linked list of players
        last = None
        for i in range(number):
            if last == None:
                last = PLAYER(names[i], money)
                last.position = i+1
                self.dealer.next = last
            else:
                last.next = PLAYER(names[i], money)
                last = last.next
                last.position = i+1
        last.next = self.dealer


        ### main game loop
        while self.running:
            self.winner_label.place_forget()
            self.next_var = StringVar()
            self.next_button = Button(self.root, text='NEXT', width=15, height=2, command=lambda: self.next_var.set(1))
            self.next_button.place(anchor=CENTER, x=450, y=500)
            if self.just_one_player():
                break
            self.next_button.wait_variable(self.next_var)
            if self.next_var.get() == 'quit':
                break
            self.refresh(0)
            self.deal()
            self.refresh(0)
            self.next_button.wait_variable(self.next_var)
            if self.next_var.get() == 'quit':
                break
            self.blinds()
            self.refresh(0)
            self.ready_to_bet()
            self.bet(1)
            if self.next_var.get() == 'quit':
                break
            if self.just_one_player():
                self.check_table()
                self.clear_table()
            else:
                self.flop()
                self.refresh(0)
                self.next_button.wait_variable(self.next_var)
                if self.next_var.get() == 'quit':
                    break
                self.ready_to_bet()
                self.bet(0)
                if self.next_var.get() == 'quit':
                    break
                if self.just_one_player():
                    self.check_table()
                    self.clear_table()
                else:
                    self.turn_river('turn')
                    self.refresh(0)
                    self.next_button.wait_variable(self.next_var)
                    if self.next_var.get() == 'quit':
                        break
                    self.ready_to_bet()
                    self.bet(0)
                    if self.next_var.get() == 'quit':
                        break
                    if self.just_one_player():
                        self.check_table()
                        self.clear_table()
                    else:
                        self.turn_river('river')
                        self.refresh(0)
                        self.next_button.wait_variable(self.next_var)
                        if self.next_var.get() == 'quit':
                            break
                        self.ready_to_bet()
                        self.bet(0)
                        if self.next_var.get() == 'quit':
                            break
                        self.refresh(0)
                        if self.just_one_player():
                            self.check_table()
                            self.clear_table()
                        else:
                            self.show_hands()
                            self.check_for_winners()
                            self.next_button.wait_variable(self.next_var)
                            self.hide_cards()
                            if self.next_var.get() == 'quit':
                                break
                            self.clear_table()
        if self.next_var.get() == 'quit':
            pass
        else:
            self.refresh(0)
            last = self.dealer
            while last.next.info != 'Dealer':
                last = last.next
                if last.folded == False and last.cash != 0:
                    win_name = last.name
            self.winner_label_var.set(f'The game has ended, {win_name} has won. Please close the game')
            self.winner_label.place(anchor=W, x = 0, y = 605)
            self.next_button.wait_variable(self.next_var)
    
    def refresh(self, position : int): # this function refreshes and updates what we see on screen - highlights the player whose turn it is and makes his cards visible...
        self.call_button.place(anchor=CENTER, x=150, y=550)
        self.check_button.place(anchor=CENTER, x=150, y=480)
        self.raise_button.place(anchor=CENTER, x=750, y=480)
        self.allin_button.place(anchor=CENTER, x=750, y=520)
        self.fold_button.place(anchor=CENTER, x=150, y=410)

        self.table_pot_var.set(f'There is {self.pot} $ on the table')

        position = position % (self.number + 1)

        last = self.dealer
        i = 0
        while last.next.info != 'Dealer':
                last = last.next
                if last.position == 1:
                    self.player_one_var.set(f'{last.name} has {last.cash} $')
                    if last.position == position:
                        self.player_one_label.config(bg='green')
                    else:
                        self.player_one_label.config(bg='lightgray')
                    self.player_one_cashin_var.set(last.cashin)
                elif last.position == 2:
                    self.player_two_var.set(f'{last.name} has {last.cash} $')
                    if last.position == position:
                        self.player_two_label.config(bg='green')
                    else:
                        self.player_two_label.config(bg='lightgray')
                    self.player_two_cashin_var.set(last.cashin)
                elif last.position == 3:
                    self.player_three_var.set(f'{last.name} has {last.cash} $')
                    if last.position == position:
                        self.player_three_label.config(bg='green')
                    else:
                        self.player_three_label.config(bg='lightgray')
                    self.player_three_cashin_var.set(last.cashin)
                elif last.position == 4:
                    self.player_four_var.set(f'{last.name} has {last.cash} $')
                    if last.position == position:
                        self.player_four_label.config(bg='green')
                    else:
                        self.player_four_label.config(bg='lightgray')
                    self.player_four_cashin_var.set(last.cashin)
                elif last.position == 5:
                    self.player_five_var.set(f'{last.name} has {last.cash} $')
                    if last.position == position:
                        self.player_five_label.config(bg='green')
                    else:
                        self.player_five_label.config(bg='lightgray')
                    self.player_five_cashin_var.set(last.cashin)
                elif last.position == 6:
                    self.player_six_var.set(f'{last.name} has {last.cash} $')
                    if last.position == position:
                        self.player_six_label.config(bg='green')
                    else:
                        self.player_six_label.config(bg='lightgray')
                    self.player_six_cashin_var.set(last.cashin)
                if last.position == position and last.folded == False:
                    self.playing_label_var.set(f"It is {last.name}'s turn, you have {last.cash} and you are in for {last.cashin}")
                    lefty = ImageTk.PhotoImage(show_card(last.hand[0]))
                    righty = ImageTk.PhotoImage(show_card(last.hand[1]))
                    self.playing_cards_label_left.configure(image = lefty)
                    self.playing_cards_label_left.image = lefty 
                    self.playing_cards_label_right.configure(image = righty)
                    self.playing_cards_label_right.image = righty
        if position == 0:
            self.call_button.place_forget()
            self.check_button.place_forget()
            self.raise_button.place_forget()
            self.allin_button.place_forget()
            self.fold_button.place_forget()
            img0 = ImageTk.PhotoImage(blank)
            self.playing_cards_label_left.configure(image = img0)
            self.playing_cards_label_left.image = img0
            self.playing_cards_label_right.configure(image = img0)
            self.playing_cards_label_right.image = img0
            self.playing_label_var.set(' ')
        return False
    
    

    def blinds(self): #### kdyz nema hrac na blind je treba ho vyradit ze hry a posunout blind na dalsiho - nejakej while loop
        just_one = False
        blind = self.dealer.next
        while blind.folded or blind.cash < self.small:
            blind.folded = True
            blind.cash = 0
            blind = blind.next
            if blind.info == 'Dealer':
                blind = blind.next
        blind.cashin += self.small
        blind.cash -= self.small
        self.pot += self.small
        blind = blind.next
        if blind.info == 'Dealer':
            blind = blind.next
        while blind.folded or blind.cash < self.big:
            blind.folded = True
            blind.cash = 0
            blind = blind.next
            if blind.info == 'Dealer':
                blind = blind.next
            if blind.cashin != 0:
                blind = blind.next
            if self.just_one_player():
                just_one = True
                break
        if just_one:
            self.highest = self.small
        else:
            blind.cashin += self.big
            blind.cash -= self.big
            self.pot += self.big
            self.highest = self.big

    def deal(self): #this deals cards to the players
        for i in range(2):
            last = self.dealer
            while last.next.info != 'Dealer':
                last = last.next
                if last.folded == False:
                    last.hand.append(self.deck.pop())
                    last.hand_to_write.append(str(last.hand[-1][0])+' '+str(last.hand[-1][1]))
    
    def ready_to_bet(self): #this prepares the players for the next round of bets
        last = self.dealer
        while last.next.info != 'Dealer':
            last = last.next
            last.played = False
        
    def bet(self, preflop :int):### preflop eithe 0 or 1 (true false), this function goes through the linked list of players and lets them play
        if preflop == 1:
            first = self.dealer.next.next
        else:
            first = self.dealer
        if first.next.info == 'Dealer':
            first = first.next

        while first.next.info != 'Dealer':
            self.refresh(first.next.position)
            self.next_button.place_forget()
            not_checked = False
            if first.next.folded == True or first.next.cash == 0:
                first = first.next
                self.next_button.place(anchor=CENTER, x=450, y=500)
                pass
            elif (first.next.played == True and first.next.cashin == self.highest) or (first.next.played and first.next.cash == 0):
                first = first.next
                self.next_button.place(anchor=CENTER, x=450, y=500)
                pass
            else:
                minimum = max(self.highest - first.next.cashin, 1)
                self.raise_value = IntVar()
                self.raise_scale = Scale(self.root, from_= minimum, to = first.next.cash, variable = self.raise_value, orient = HORIZONTAL, background = 'lightgray')
                self.raise_scale.place(anchor = CENTER, x = 750, y = 570)
                self.call_button.wait_variable(self.action_var)
                if self.action_var.get() == 'quit':
                    return
                if self.action_var.get() == 'call':
                    first = first.next
                    rozdil = self.highest - first.cashin
                    if rozdil > first.cash:
                        total = first.cash
                        self.pot += total
                        first.cashin += total
                        first.cash = 0
                    else:
                        first.cash -= rozdil
                        self.pot += rozdil
                        first.cashin += rozdil
                    first.played = True
                elif self.action_var.get() == 'check':
                    if first.next.cashin == self.highest:
                        first = first.next
                        first.played = True
                        pass
                    else:
                        not_checked = True
                elif self.action_var.get() == 'fold':
                    first = first.next
                    self.trash +=2
                    first.hand = []
                    first.cashin = 'FOLDED'
                    first.folded = True
                    first.played = True
                elif self.action_var.get() == 'raise':
                    first = first.next
                    first.played = True                    
                    amount = self.raise_value.get()
                    first.cashin += amount
                    first.cash -= amount
                    self.pot += amount
                    if first.cashin > self.highest:
                        self.highest = first.cashin
                elif self.action_var.get() == 'allin':
                    first = first.next
                    first.played = True
                    amount = first.cash
                    first.cashin += amount
                    first.cash -= amount
                    self.pot += amount
                    if self.highest < first.cashin:
                        self.highest = first.cashin
                self.raise_scale.place_forget()
                self.next_button.place(anchor=CENTER, x=450, y=500)
                self.call_button.place_forget()
                self.check_button.place_forget()
                self.raise_button.place_forget()
                self.allin_button.place_forget()
                self.fold_button.place_forget()
                self.raise_scale.place_forget()
                img0 = ImageTk.PhotoImage(blank)
                self.playing_cards_label_left.configure(image = img0)
                self.playing_cards_label_left.image = img0
                self.playing_cards_label_right.configure(image = img0)
                self.playing_cards_label_right.image = img0
                if self.just_one_player():
                        break
                if not not_checked:
                    self.next_button.wait_variable(self.next_var)
        first = first.next

        if preflop == 1:
            i = 0
            while i < 2:
                not_checked = False
                if first.next.info == 'Dealer':
                    first = first.next
                self.refresh(first.next.position)
                if first.next.folded == True or first.next.cash == 0:
                    first = first.next
                    i += 1
                    pass
                elif first.next.played == True and first.next.cashin == self.highest:
                    first = first.next
                    i += 1
                    pass
                else:
                    minimum = max(self.highest - first.next.cashin, 1)
                    self.raise_value = IntVar()
                    self.raise_scale = Scale(self.root, from_= minimum, to = first.next.cash, variable = self.raise_value, orient = HORIZONTAL, background = 'lightgray')
                    self.raise_scale.place(anchor = CENTER, x = 750, y = 570)
                    self.next_button.place_forget()
                    self.call_button.wait_variable(self.action_var)
                    if self.action_var.get() == 'quit':
                        return
                    if self.action_var.get() == 'call':
                        first = first.next
                        rozdil = self.highest - first.cashin
                        if rozdil > first.cash:
                            total = first.cash
                            self.pot += total
                            first.cashin += total
                            first.cash = 0
                        else:
                            first.cash -= rozdil
                            self.pot += rozdil
                            first.cashin += rozdil
                        first.played = True
                    elif self.action_var.get() == 'check':
                        if first.next.cashin == self.highest:
                            first = first.next
                            i += 1
                            first.played = True
                            pass
                        else:
                            not_checked = True
                    elif self.action_var.get() == 'fold':
                        first = first.next
                        i += 1
                        self.trash += 2
                        first.hand = []
                        first.cashin = 'FOLDED'
                        first.folded = True
                        first.played = True
                    elif self.action_var.get() == 'raise':
                        first = first.next
                        first.played = True                    
                        amount = self.raise_value.get()
                        first.cashin += amount
                        first.cash -= amount
                        self.pot += amount
                        if first.cashin > self.highest:
                            self.highest = first.cashin
                    elif self.action_var.get() == 'allin':
                        first = first.next
                        first.played = True
                        i += 1
                        amount = first.cash
                        first.cashin += amount
                        first.cash -= amount
                        self.pot += amount
                        if self.highest < first.cashin:
                            self.highest = first.cashin
                        self.raise_scale.place_forget()
                    elif self.action_var.get() == 'quit':
                        pass
                    self.next_button.place(anchor=CENTER, x=450, y=500)
                    self.call_button.place_forget()
                    self.check_button.place_forget()
                    self.raise_button.place_forget()
                    self.allin_button.place_forget()
                    self.fold_button.place_forget()
                    self.raise_scale.place_forget()
                    img0 = ImageTk.PhotoImage(blank)
                    self.playing_cards_label_left.configure(image = img0)
                    self.playing_cards_label_left.image = img0
                    self.playing_cards_label_right.configure(image = img0)
                    self.playing_cards_label_right.image = img0
                    if not not_checked:
                        self.next_button.wait_variable(self.next_var)
                if i == 2:
                    dalsi = first.next
                    if dalsi.info == 'Dealer':
                        dalsi = dalsi.next
                    while dalsi.folded == True:
                        dalsi = dalsi.next
                        if dalsi.info == 'Dealer':
                            dalsi = dalsi.next
                    if dalsi.cashin != self.highest:
                        self.bet(preflop)
        else:
            dalsi = first.next
            if dalsi.info == 'Dealer':
                dalsi = dalsi.next
            while dalsi.folded == True:
                dalsi = dalsi.next
                if dalsi.info == 'Dealer':
                    dalsi = dalsi.next
            if dalsi.cashin != self.highest:
                self.bet(preflop)

    def flop(self):#this function reveals the flop 
        burn = self.deck.pop() # this isnt necessary 
        self.trash += 1
        self.cards.append(self.deck.pop())
        first_card = ImageTk.PhotoImage(show_mini_cards(self.cards[-1]))
        self.cards.append(self.deck.pop())
        second_card = ImageTk.PhotoImage(show_mini_cards(self.cards[-1]))
        self.cards.append(self.deck.pop())
        third_card = ImageTk.PhotoImage(show_mini_cards(self.cards[-1]))
        self.first_card_label.configure(image = first_card)
        self.first_card_label.image = first_card
        self.second_card_label.configure(image = second_card)
        self.second_card_label.image = second_card
        self.third_card_label.configure(image = third_card)
        self.third_card_label.image = third_card
    
    def turn_river(self, turn): #this function reveals the turn/river card
        burn = self.deck.pop()
        self.trash += 1
        self.cards.append(self.deck.pop())
        if turn == 'turn':
            fourth_card = ImageTk.PhotoImage(show_mini_cards(self.cards[-1]))
            self.fourth_card_label.configure(image = fourth_card)
            self.fourth_card_label.image = fourth_card
        elif turn == 'river':
            fifth_card = ImageTk.PhotoImage(show_mini_cards(self.cards[-1]))
            self.fifthcard_label.configure(image = fifth_card)
            self.fifthcard_label.image = fifth_card
    
    def check_table(self):
        player_counter = 0
        last = self.dealer
        while last.next.info != 'Dealer':
            last = last.next
            if last.folded == False:
                player_counter += 1
        if player_counter == 1:
            last = self.dealer
            while last.next.info != 'Dealer':
                last = last.next
                if last.folded == False:
                    self.winner_label_var.set(f'vitez je {last.info}, {last.name}. Vyhral {self.pot}')
                    self.winner_label.place(anchor=W, x=50, y=350)
                    last.cash += self.pot
                    return False
        else:
            return True
    
    def just_one_player(self): #checks how many players are still in game, if theres only one player left, return True
        player_counter = 0
        last = self.dealer
        while last.next.info != 'Dealer':
            last = last.next
            if last.folded == False:
                player_counter += 1
        if player_counter == 1:
            return True
        else:
            return False
    
    def clear_table(self):#clears the table and prepares it for another round
        self.pot = 0
        self.cards = []
        self.cards_to_write = []
        self.deck = cards()
        self.trash = 0
        self.highest = 0

        start_mini_image = ImageTk.PhotoImage(small_blank)
        self.first_card_label.configure(image = start_mini_image)
        self.first_card_label.image = start_mini_image
        self.second_card_label.configure(image = start_mini_image)
        self.second_card_label.image = start_mini_image
        self.third_card_label.configure(image = start_mini_image)
        self.third_card_label.image = start_mini_image
        self.fourth_card_label.configure(image = start_mini_image)
        self.fourth_card_label.image = start_mini_image
        self.fifthcard_label.configure(image = start_mini_image)
        self.fifthcard_label.image = start_mini_image


        last = self.dealer
        
        player_counter = 0

        while last.next.info != 'Dealer':
            last = last.next
            if last.cash < 10:
                last.folded = True
                last.hand = []
                last.hand_to_write = []
                last.cashin = 0
                last.pairs = {}
                last.suits = {}
                last.values = []
            else:
                last.folded = False
                last.hand = []
                last.hand_to_write = []
                last.cashin = 0
                last.pairs = {}
                last.suits = {}
                last.values = []
        if self.just_one_player():
            pass
        else: 
            last = self.dealer
            last_small_blind = None
            while last.info != 'Dealer':
                last = last.next
                if last.folded == False and last_small_blind == None:
                    last_small_blind = last.position
            
            new_small_blind = None
            while new_small_blind == None or new_small_blind == last_small_blind:
                deall = self.dealer
                first_after = self.dealer.next
                last = self.dealer
                while last.next.info != 'Dealer':
                    last = last.next
                last.next = first_after
                deall.next = first_after.next
                first_after.next = deall       
                last = self.dealer
                while last.next.info != 'Dealer':
                    last = last.next
                    if last.folded == False:
                        new_small_blind = last.position
                        break     
            

    def show_hands(self):#this function hhides the player avatar and reveals the cards in their hands instead
        hands = {}
        people = []
        last = self.dealer
        while last.next.info != 'Dealer':
            last = last.next
            if last.folded == False:
                hands[last.position] = last.hand
        first = placement(1, self.number)
        second = placement(2, self.number)
        third = placement(3, self.number)
        fourth = placement(4, self.number)
        fifth = placement(5, self.number)
        sixth = placement(6, self.number)
        if 1 in hands:
            one_left_card = ImageTk.PhotoImage(show_mini_cards(hands[1][0]))
            one_right_card = ImageTk.PhotoImage(show_mini_cards(hands[1][1]))
            self.one_left.configure(image = one_left_card)
            self.one_left.image = one_left_card
            self.one_right.configure(image = one_right_card)
            self.one_right.image = one_right_card
            self.one_left.place(anchor=CENTER, x = first[0]-30, y = first[1])
            self.one_right.place(anchor=CENTER, x = first[0]+30, y = first[1])
            self.player_one_avatar.place_forget()
            people.append(1)
        if 2 in hands:
            two_left_card = ImageTk.PhotoImage(show_mini_cards(hands[2][0]))
            two_right_card = ImageTk.PhotoImage(show_mini_cards(hands[2][1]))
            self.two_left.configure(image = two_left_card)
            self.two_left.image = two_left_card
            self.two_right.configure(image = two_right_card)
            self.two_right.image = two_right_card
            self.two_left.place(anchor=CENTER, x = second[0]-30, y = second[1])
            self.two_right.place(anchor=CENTER, x = second[0]+30, y = second[1])
            self.player_two_avatar.place_forget()
            people.append(2)
        if 3 in hands:
            three_left_card = ImageTk.PhotoImage(show_mini_cards(hands[3][0]))
            three_right_card = ImageTk.PhotoImage(show_mini_cards(hands[3][1]))
            self.three_left.configure(image = three_left_card)
            self.three_left.image = three_left_card
            self.three_right.configure(image = three_right_card)
            self.three_right.image = three_right_card
            self.three_left.place(anchor=CENTER, x = third[0]-30, y = third[1])
            self.three_right.place(anchor=CENTER, x = third[0]+30, y = third[1])
            self.player_three_avatar.place_forget()
            people.append(3)
        if 4 in hands:
            four_left_card = ImageTk.PhotoImage(show_mini_cards(hands[4][0]))
            four_right_card = ImageTk.PhotoImage(show_mini_cards(hands[4][1]))
            self.four_left.configure(image = four_left_card)
            self.four_left.image = four_left_card
            self.four_right.configure(image = four_right_card)
            self.four_right.image = four_right_card
            self.four_left.place(anchor=CENTER, x = fourth[0]-30, y = fourth[1])
            self.four_right.place(anchor=CENTER, x = fourth[0]+30, y = fourth[1])
            self.player_four_avatar.place_forget()
            people.append(4)
        if 5 in hands:
            five_left_card = ImageTk.PhotoImage(show_mini_cards(hands[5][0]))
            five_right_card = ImageTk.PhotoImage(show_mini_cards(hands[5][1]))
            self.five_left.configure(image = five_left_card)
            self.five_left.image = five_left_card
            self.five_right.configure(image = five_right_card)
            self.five_right.image = five_right_card
            self.five_left.place(anchor=CENTER, x = fifth[0]-30, y = fifth[1])
            self.five_right.place(anchor=CENTER, x = fifth[0]+30, y = fifth[1])
            self.player_five_avatar.place_forget()
            people.append(5)
        if 6 in hands:
            six_left_card = ImageTk.PhotoImage(show_mini_cards(hands[6][0]))
            six_right_card = ImageTk.PhotoImage(show_mini_cards(hands[6][1]))
            self.six_left.configure(image = six_left_card)
            self.six_left.image = six_left_card
            self.six_right.configure(image = six_right_card)
            self.six_right.image = six_right_card
            self.six_left.place(anchor=CENTER, x = sixth[0]-30, y = sixth[1])
            self.six_right.place(anchor=CENTER, x = sixth[0]+30, y = sixth[1])
            self.player_six_avatar.place_forget()
            people.append(6)

    def hide_cards(self): #counter-function to show_hands()
        self.one_left.place_forget()
        self.one_right.place_forget()
        first = placement(1, self.number)
        self.player_one_avatar.place(anchor=CENTER, x = first[0], y = first[1])
        self.two_left.place_forget()
        self.two_right.place_forget()
        second = placement(2, self.number)
        self.player_two_avatar.place(anchor=CENTER, x = second[0], y = second[1])
        if self.number >= 3:
            self.three_left.place_forget()
            self.three_right.place_forget()
            third = placement(3, self.number)
            self.player_three_avatar.place(anchor=CENTER, x = third[0], y = third[1])
        if self.number >= 4:
            self.four_left.place_forget()
            self.four_right.place_forget()
            fourth = placement(4, self.number)
            self.player_four_avatar.place(anchor=CENTER, x = fourth[0], y = fourth[1])
        if self.number >= 5:
            self.five_left.place_forget()
            self.five_right.place_forget()
            fifth = placement(5, self.number)
            self.player_five_avatar.place(anchor=CENTER, x = fifth[0], y = fifth[1])
        if self.number >= 6:
            self.six_left.place_forget()
            self.six_right.place_forget()
            sixth = placement(6, self.number)
            self.player_six_avatar.place(anchor=CENTER, x = sixth[0], y = sixth[1])

            




        

    def close(self):#callback function which kills the program
        self.running = False
        self.next_var.set('quit')
        self.action_var.set('quit')
        self.root.destroy()



    def check_for_winners(self): #this function looks at the table and determines the winner
        last = self.dealer
        while last.next.info != 'Dealer':
            last = last.next
            if last.folded == False:
                for i in self.cards:
                    last.hand.append(i)
                last.hand.sort(key=lambda x: x[0])

        while True:
            if royal(self):
                break
            if straight_flush(self):
                break
            if four(self):
                break
            if full_house(self):
                break
            if flush(self):
                break
            if straight(self):
                break
            if three(self):
                break
            if two_pair(self):
                break
            if pair(self):
                break
            if highcard(self):
                break
        
        payout(self)
        
                        

            

                        
                    


                        
                ####  kdyz trojice a stejna high card tak se deli pot
                    
                    