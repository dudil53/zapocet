import random
from tkinter import *
import time
from table import *
import sys
from PIL import ImageTk, Image


sys.setrecursionlimit(50000)



        





class START():
    def __init__(self, root):
        ### variables
        self.root = root
        self.blinds_var = StringVar()
        self.buy_in = StringVar()
        self.table = None




        ### start and quit buttons
        start_button = Button(self.root, text='Start Game', width=10, height=2, command=self.start_game)
        start_button.place(anchor=CENTER, x=300, y = 200)

        quit_button = Button(self.root, text='Quit Game', width=10, height=2, command=self.root.destroy)
        quit_button.place(anchor=CENTER, x=600, y = 200)



        #### minimum is two players, maximum is 6
        #player one
        self.player_one_name = StringVar()
        self.player_one_name.set('Player 1')
        self.player_one_label = Label(self.root, text='Player 1 name:', background='lightgray')
        self.player_one = Entry(self.root, textvariable=self.player_one_name)
        self.player_one_label.place(anchor=CENTER, x=110, y=300)
        self.player_one.place(anchor=CENTER, x=310, y=300)

        #player two
        self.player_two_name = StringVar()
        self.player_two_name.set('Player 2')
        self.player_two_label = Label(self.root, text='Player 2 name:', background='lightgray')
        self.player_two = Entry(self.root, textvariable=self.player_two_name)
        self.player_two_label.place(anchor=CENTER, x=110, y=335)
        self.player_two.place(anchor=CENTER, x=310, y=335)


        #### other players
        self.nr_of_players = IntVar()
        self.nr_of_players.set(2)

        player_nr_label = Label(self.root, text = 'Choose the number of players: ', background='lightgray')
        player_nr_label.place(anchor=CENTER, x=600,y=300)  

        player_nr = Scale(self.root, from_=2, to=6, orient = HORIZONTAL, variable=self.nr_of_players, background='lightgray', command=self.player_nr_update)
        player_nr.place(anchor=CENTER, x=600, y=350)


        #### other player labels / names
        # player three
        self.player_three_name = StringVar()
        self.player_three_name.set('Player 3')
        self.player_three_label = Label(self.root, text='Player 3 name:', background='lightgray')
        self.player_three = Entry(self.root, textvariable=self.player_three_name)
        

        # player four
        self.player_four_name = StringVar()
        self.player_four_name.set('Player 4')
        self.player_four_label = Label(self.root, text='Player 2 name:', background='lightgray')
        self.player_four = Entry(self.root, textvariable=self.player_four_name)
        

        # player five
        self.player_five_name = StringVar()
        self.player_five_name.set('Player 5')
        self.player_five_label = Label(self.root, text='Player 2 name:', background='lightgray')
        self.player_five = Entry(self.root, textvariable=self.player_five_name)
        #self.player_five_label.place(anchor=CENTER, x=110, y=440)
        #self.player_five.place(anchor=CENTER, x=310, y=440)

        # player six
        self.player_six_name = StringVar()
        self.player_six_name.set('Player 6')
        self.player_six_label = Label(self.root, text='Player 2 name:', background='lightgray')
        self.player_six = Entry(self.root, textvariable=self.player_six_name)
    

        #update player number so the default number isnt only 2
        self.player_nr_update(4)
        self.nr_of_players.set(4)



        #buy in options and things around that
        self.buy_in.set('200')
        buy_options = [
            '200',
            '500',
            '1000',
            '10000'
        ]
        money_label = Label(self.root, text='Choose the buy in:', background='lightgray')
        money_label.place(anchor=CENTER, x=600,y=420)
        money_drop = OptionMenu(self.root, self.buy_in, *buy_options, command = self.buy_in_update)
        money_drop.place(anchor=CENTER, x=600, y=470)

        blinds_label = Label(self.root, text='Small Blind / Big Blind', background='lightgray')
        blinds_label.place(anchor=CENTER, x=600, y=520)
        
        self.blinds_var.set('1 / 2')
        blinds = Label(self.root, textvariable=self.blinds_var, background='lightgray')
        blinds.place(anchor=CENTER, x=600, y=545)
        
        
        ### Title
        title_label = Label(self.root, text = "Poker, Texas Hold'em", font = ('Arial', 70), background='lightgray')
        title_label.place(anchor=CENTER, y=100, x=450)
        return

    def player_nr_update(self, number): ###this function updates the number of players, name boxes etc.
        number = int(number)
        if number == 6:
            self.player_three_label.place(anchor=CENTER, x=110, y=370)
            self.player_three.place(anchor=CENTER, x=310, y=370)
            self.player_four_label.place(anchor=CENTER, x=110, y=405)
            self.player_four.place(anchor=CENTER, x=310, y=405)
            self.player_five_label.place(anchor=CENTER, x=110, y=440)
            self.player_five.place(anchor=CENTER, x=310, y=440)
            self.player_six_label.place(anchor=CENTER, x=110, y=475)
            self.player_six.place(anchor=CENTER, x=310, y=475)
        elif number == 5:
            self.player_three_label.place(anchor=CENTER, x=110, y=370)
            self.player_three.place(anchor=CENTER, x=310, y=370)
            self.player_four_label.place(anchor=CENTER, x=110, y=405)
            self.player_four.place(anchor=CENTER, x=310, y=405)
            self.player_five_label.place(anchor=CENTER, x=110, y=440)
            self.player_five.place(anchor=CENTER, x=310, y=440)
            self.player_six_label.place_forget()
            self.player_six.place_forget()
        elif number == 4:
            self.player_three_label.place(anchor=CENTER, x=110, y=370)
            self.player_three.place(anchor=CENTER, x=310, y=370)
            self.player_four_label.place(anchor=CENTER, x=110, y=405)
            self.player_four.place(anchor=CENTER, x=310, y=405)
            self.player_five_label.place_forget()
            self.player_five.place_forget()
            self.player_six_label.place_forget()
            self.player_six.place_forget()
        elif number == 3:
            self.player_three_label.place(anchor=CENTER, x=110, y=370)
            self.player_three.place(anchor=CENTER, x=310, y=370)
            self.player_four_label.place_forget()
            self.player_four.place_forget()
            self.player_five_label.place_forget()
            self.player_five.place_forget()
            self.player_six_label.place_forget()
            self.player_six.place_forget()
        elif number == 2:
            self.player_three_label.place_forget()
            self.player_three.place_forget()
            self.player_four_label.place_forget()
            self.player_four.place_forget()
            self.player_five_label.place_forget()
            self.player_five.place_forget()
            self.player_six_label.place_forget()
            self.player_six.place_forget()


    def buy_in_update(self, variable): #this function updates the buy in options and small/big blinds
        if variable == '200':
            self.blinds_var.set('1 / 2')
        elif variable == '500':
            self.blinds_var.set('2 / 5')
        elif variable == '1 000':
            self.blinds_var.set('5 / 10')
        else:
            self.blinds_var.set('50 / 100')
        return
    
    def start_game(self): #this function gathers all the information needed and starts the game - it creates the 'table'
        names = [self.player_one_name.get(), self.player_two_name.get()]
        nr_players = self.nr_of_players.get()
        if nr_players >= 3:
            names.append(self.player_three_name.get())
        if nr_players >= 4:
            names.append(self.player_four_name.get())
        if nr_players >= 5:
            names.append(self.player_five_name.get())
        if nr_players == 6:
            names.append(self.player_six_name.get())
        money = self.buy_in.get()
        for widget in self.root.winfo_children():
            widget.destroy()
        self.table = TKTABLE(self.root, nr_players, names, int(money))
        return
    



### window settings
root = Tk()
root.title('Poker Game')
root.iconbitmap('cards/icon.ico')

root.configure(background='lightgray')
root.geometry('900x620')
root.resizable(False, False)

start_of_program = START(root)


root.mainloop()

