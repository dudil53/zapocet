from tkinter import *





def sublist(sublist, list1):
    for i in sublist:
        if i not in list1:
            return False
    return True




#### combination functions

def royal(table):
    last = table.dealer
    while last.next.info != 'Dealer':
        last = last.next
        if last.folded == False:   
            if (10, 'hearts') in last.hand and (11, 'hearts') in last.hand and (12, 'hearts') in last.hand and (13, 'hearts') in last.hand and (14, 'hearts') in last.hand:
                table.winners = [last.position]
                table.situation = 'royal flush'
                return True
    return False

def straight_flush(table):
    last = table.dealer
    winners = {}
    while last.next.info != 'Dealer':
        last = last.next
        if last.folded == False:
            multiples = list(zip(*last.hand))[0]
            values = dict.fromkeys(multiples)
            values = list(values)
            pairs = {} ####tohle pouzivam dal
            for o in values:
                pairs[o] = multiples.count(o)
            last.pairs = pairs
            suits = {
                'hearts' : [],
                'diamonds' : [],
                'clubs' : [],
                'spades' : []
            }
            for k in last.hand:
                if k[1] == 'hearts':
                    if k[0] not in suits['hearts']:
                        suits['hearts'].append(k[0])
                elif k[1] == 'diamonds':    
                    if k[0] not in suits['diamonds']:
                        suits['diamonds'].append(k[0])
                elif k[1] == 'clubs':    
                    if k[0] not in suits['clubs']:
                        suits['clubs'].append(k[0])
                elif k[1] == 'spades':    
                    if k[0] not in suits['spades']:
                        suits['spades'].append(k[0])
            if 14 in values:
                values.append(0)
            last.values = values #### will use later for normal flush
            holder = []
            while len(values) >= 5:
                minimum = min(values)
                straight = list(range(minimum, minimum+6))
                straight_check = False
                for l in suits:
                    if sublist(straight, suits[l]):
                        straight_check = True
                        break
                if straight_check:
                    if len(winners) == 0:
                        winners[last.position] = minimum
                    elif last.position in winners:
                        if winners[last.position] < minimum:
                            winners = {last.position : minimum}
                    else:
                        last_winner = list(winners)[0]
                        if minimum > winners[last_winner]:
                            winners = {last.position : minimum}
                        elif minimum == winners[last_winner]:
                            winners[last.position] = minimum
                values.remove(minimum)
                holder.append(minimum)
            for i in holder:
                values.append(i)
            last.values = values
    if len(winners) != 0:
        table.winners = list(winners)
        table.situation = 'straight flush'
        return True
    else:
        return False

def four(table):
    winners = {}
    last = table.dealer
    while last.next.info != 'Dealer':
        last = last.next
        if last.folded == False:
            for k in last.pairs:
                if last.pairs[k] == 4:
                    if len(winners) == 0:
                        winners[last.position] = k
                    else:
                        last_winner = list(winners)[0]
                        if winners[last_winner] < k:
                            winners = {last.position : k}
                        elif winners[last_winner] == k:
                            winners[last.position] = k
    if len(winners) != 0:
        if len(winners) == 1:
            table.winners = list(winners)
        else:
            highcard = None
            new_winners = []
            last = table.dealer
            while last.next.info != 'Dealer':
                last = last.next
                if last.position in winners:
                    values_copy = last.values.copy()
                    values_copy.remove(winners[last.position])
                    if not highcard:
                        highcard = max(values_copy)
                        new_winners.append(last.position)
                    elif max(values_copy) == highcard:
                        new_winners.append(last.position)
                    elif highcard < max(values_copy):
                        highcard = max(values_copy)
                        new_winners = [last.position]
            table.winners = new_winners
        table.situation = 'four of a kind'
        return True
    else:
        return False
                        
def full_house(table):
    winners = {}
    triplets = {}
    twins = {}
    last = table.dealer
    while last.next.info != 'Dealer':
        last = last.next
        if last.folded == False:
            winners[last.position] = (None, None)
            for k in last.pairs:
                if last.pairs[k] == 2:
                    if last.position not in twins:
                        twins[last.position] = [k]
                    else:
                        twins[last.position].append(k)
                    if winners[last.position][0] == None:
                        winners[last.position] = (k, winners[last.position][1])
                    elif k > winners[last.position][0]:
                        winners[last.position] = (k, winners[last.position][1])
                elif last.pairs[k] == 3:
                    if winners[last.position][1] == None:
                        triplets[last.position] = k
                        winners[last.position] = (winners[last.position][0], k)
                    elif k > winners[last.position][1]:
                        winners[last.position] = (winners[last.position][1], k)
                    elif k < winners[last.position][1]:
                        winners[last.position] = (k, winners[last.position][1])
            if winners[last.position][0] == None or winners[last.position][1] == None:
                winners.pop(last.position)
    table.twins = twins
    if len(winners) != 0:
        maximum3 = None
        maximum2 = None
        winner = None
        for i in winners:
            if not maximum3:
                maximum3 = winners[i][1]
                maximum2 = winners[i][0]
                winner = [i] 
            elif winners[i][1] > maximum3:
                maximum3 = winners[i][1]
                maximum2 = winners[i][0]
                winner = [i]
            elif winners[i][1] == maximum3 and winners[i][0] > maximum2:
                maximum3 = winners[i][1]
                maximum2 = winners[i][0]
                winner = [i]
            elif winners[i][1] == maximum3 and winners[i][0] == maximum2:
                winner.append(i)
        table.winners = winner
        table.situation = 'full house'
        return True
    else:
        return False

def flush(table):
    winners = {}
    last = table.dealer
    while last.next.info != 'Dealer':
        last = last.next
        if last.folded == False:
            flush = 'nothing'
            suits = {
                'hearts' : [],
                'diamonds' : [],
                'clubs' : [],
                'spades' : []
            }
            for k in last.hand:
                if k[1] == 'hearts':
                    suits['hearts'].append(k[0])
                    if len(suits['hearts']) == 5:
                        flush = 'hearts'
                elif k[1] == 'diamonds':
                    suits['diamonds'].append(k[0])
                    if len(suits['diamonds']) == 5:
                        flush = 'diamonds'
                elif k[1] == 'clubs':
                    suits['clubs'].append(k[0])
                    if len(suits['clubs']) == 5:
                        flush = 'clubs'
                elif k[1] == 'spades':
                    suits['spades'].append(k[0])
                    if len(suits['spades']) == 5:
                        flush = 'spades'
            if flush != 'nothing':
                if flush == 'hearts':
                    winners[last.position] = suits['hearts']
                elif flush == 'diamonds':
                    winners[last.position] = suits['diamonds']
                elif flush == 'clubs':
                    winners[last.position] = suits['clubs']
                elif flush == 'spades':
                    winners[last.position] = suits['spades']
    if len(winners) == 0:
        return False
    elif len(winners) == 1:
        table.winners = winners
        table.situation = 'flush'
        return True
    elif len(winners) > 1:
        maximum = None
        winner = None
        for i in winners:
            if not maximum:
                maximum = max(winners[i])
                winner = [i]
            elif max(winners[i]) > maximum:
                maximum = max(winners[i])
                winner = [i]
            elif max(winners[i]) == maximum:
                winner.append(i)
        table.winners = winner
        table.situation = 'flush'
        return True
    
def straight(table):
    winners = {}
    last = table.dealer
    while last.next.info != 'Dealer':
        last = last.next
        if last.folded == False:
            last.values = list(last.pairs)
            if 14 in last.values:
                last.values.append(0)
            while len(last.values) >= 5:
                        minimum = min(last.values)
                        straight = list(range(minimum, minimum+6))
                        straight_check = False
                        if sublist(straight, last.values):
                            straight_check = True
                        if straight_check:
                            if last.position not in winners:
                                winners[last.position] = [minimum]
                            else:
                                winners[last.position].append(minimum)
                        last.values.remove(minimum)

    if len(winners) != 0:
        winner = None
        maximum = None
        for i in winners:
            if not maximum:
                maximum = max(winners[i])
                winner = [i]
            elif maximum < max(winners[i]):
                maximum = max(winners[i])
                winner = [i]
            elif maximum == max(winners[i]):
                winner.append(i)
        table.winners = winners
        table.situation = 'straight'
        return True
    else:
        return False
        
def three(table):
    triplets = {}
    last = table.dealer
    while last.next.info != 'Dealer':
        last = last.next
        if last.folded == False:
            for i in last.pairs:
                if last.pairs[i] == 3:
                    triplets[last.position] = i ##kdyby byly dve trojice vyhodnoti se uz fullhoouse
    if len(triplets) == 0:
        return False
    elif len(triplets) == 1:
        table.winners = list(triplets)
        table.situation = 'three of a kind'
        return True
    elif len(triplets) > 1:
        highcard = None
        winner = []
        last = table.dealer
        while last.next.info != 'Dealer':
            last = last.next
            if last.position in triplets:
                new_values = (list(last.pairs)).copy()
                new_values.remove(triplets[last.position])
                if not highcard:
                    highcard = max(new_values)
                    winner = [last.position]
                elif max(new_values) == highcard:
                    winner.append(last.position)
                elif max(new_values) > highcard:
                    winner = [last.position]
        table.winners = winner
        table.situation = 'three of a kind'
        return True

def two_pair(table):
    winners = []
    if len(table.twins) != 0:
        bigger_pair = None
        smaller_pair = None
        for i in table.twins:
            if len(table.twins[i]) >= 2:
                if not bigger_pair:
                    bigger_pair = max(table.twins[i])
                    table.twins[i].remove(bigger_pair)
                    smaller_pair = max(table.twins[i])
                    table.twins[i].append(bigger_pair)
                    winners = [i]
                elif max(table.twins[i]) > bigger_pair:
                    bigger_pair = max(table.twins[i])
                    table.twins[i].remove(bigger_pair)
                    smaller_pair = max(table.twins[i])
                    table.twins[i].append(bigger_pair)
                    winners = [i]
                elif max(table.twins[i]) == bigger_pair:
                    table.twins[i].remove(bigger_pair)
                    if max(table.twins[i]) > smaller_pair:
                        smaller_pair = max(table.twins[i])
                        winners = [i]
                    elif max(table.twins[i]) == smaller_pair:
                        winners.append(i)
                    table.twins[i].append(bigger_pair)
        if len(winners) == 0:
            return False
        elif len(winners) == 1:
            table.winners = winners
            table.situation = 'two pairs'
            return True
        elif len(winners) > 1:
            highcard = None
            winner = []
            last = table.dealer
            while last.next.info != 'Dealer':
                last = last.next
                if last.position in winners:
                    new_values = (list(last.pairs)).copy()
                    new_values.remove(bigger_pair)
                    new_values.remove(smaller_pair)
                    if not highcard:
                        highcard = max(new_values)
                        winner = [last.position]
                    elif max(new_values) == highcard:
                        winner.append(last.position)
                    elif max(new_values) > highcard:
                        winner = [last.position]
            table.winners = winner
            table.situation = 'two pairs'
            return True
    else:
        return False


def pair(table):
    if len(table.twins) != 0:
        winners = []
        biggest_pair = None
        for i in table.twins:
            if len(table.twins[i]) == 1:
                if not biggest_pair:
                    biggest_pair = table.twins[i][0]
                    winners = [i]
                elif table.twins[i][0] > biggest_pair:
                    biggest_pair = table.twins[i][0]
                    winners = [i]
                elif table.twins[i][0] == biggest_pair:
                    winners.append(i)
        if len(winners) == 0:
            return False
        elif len(winners) == 1:
            table.winners = winners
            table.situation = 'pair'
            return True
        elif len(winners) > 1:
            highcard = None
            winner = []
            last = table.dealer
            while last.next.info != 'Dealer':
                last = last.next
                if last.position in winners:
                    new_values = (list(last.pairs)).copy()
                    new_values.remove(biggest_pair)
                    if not highcard:
                        highcard = max(new_values)
                        winner = [last.position]
                    elif max(new_values) == highcard:
                        winner.append(last.position)
                    elif max(new_values) > highcard:
                        winner = [last.position]
            table.winners = winner
            table.situation = 'pair'
            return True
    else:
        return False

def highcard(table):
    last = table.dealer
    highcard = None
    winners = []
    while last.next.info != 'Dealer':
        last = last.next
        if last.folded == False:
            last.values = list(last.pairs)
            if not highcard:
                highcard = max(last.values)
                winners = [last.position]
            elif max(last.values) > highcard:
                highcard = max(last.values)
                winners = [last.position]
            elif max(last.values) == highcard:
                winners.append(last.position)
    if len(winners) == 0:###this wont happen
        table.winners = [1]
        return True
    else:
        table.winners = winners
        table.situation = 'highcard'
        return True



### this function 
def payout(table):
    total = int(table.pot)
    nr_of_winners = len(table.winners)
    one_winner_payout = total // nr_of_winners
    last = table.dealer
    winner_string = ''
    while last.next.info != 'Dealer':
        last = last.next
        if last.position in table.winners:
            last.cash += one_winner_payout
            winner_string += f'{last.name} won {one_winner_payout},'
    winner_string += f'the winning situation was {table.situation}'
    table.winner_label_var.set(winner_string)
    table.winner_label.place(anchor=W, x = 0, y = 605)
    table.pot = 0
    table.winners = []
    table.situation = 'nothing yet'
    return