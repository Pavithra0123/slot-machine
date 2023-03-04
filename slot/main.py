
#generating slot machine
import random

MAX_LINES = 5
MAX_BET = 200
MIN_BET = 1

ROWS = 5
COLS = 5

symbol_count ={
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value ={
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

#6 to check the winning
def check_winings(columns,lines,bet,values):
    winnings = 0
    winning_lines =[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines

#4 slot machine
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[] #this is going to be list
    for symbol,symbol_count in symbols.items():#item gives the both key and value in dictionary
        for _ in range (symbol_count):
            all_symbols.append(symbol)
    columns =[] #nested list is going represent the value
    for col in range(cols):
        column =[]
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

#5 changing to the column way from row
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end="|")#end is giving the default new line.
            else:
                print(column[row],end="")
        print()

#1 function calling to deposit the amount
def deposit():
    while True:
        amount = input(" what would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0")
        else:
            print("please enter a number")

    return amount

#2 bet for how many lines and giving the maximum lines
def get_number_of_lines():
    while True:
        lines = input(" enter the number of lines to bet on(1-" + str(MAX_LINES) + ")? ")#here giving the range with one dash and maximumline
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter the valid number of lines")
        else:
            print("please enter a number")
            
    return lines

#3 betting
def get_bet():
    while True:
        amount = input(" what would you like to bet on each line? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<= amount <=MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("please enter a number")
    return amount

#7    
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet> balance:
            print(f"you dont have enough to bet that amount ,your current balance is :${balance}")
        else:
            break
    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to : ${total_bet}")
     
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winings(slots,lines,bet,symbol_value)
    print(f"you won ${winnings}")
    print(f"you won on lines:", *winning_lines)
    return winnings - total_bet
    

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")
    
main()




