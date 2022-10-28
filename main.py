#!/usr/bin/env python3
""" Author: Jgarcia | Title: Slot Machine |
Purpose: accepts deposit from the user and takes bets from 1 - MAX_LINES"""
import random

# Global Variables
MAX_BET = 100
MIN_BET = 1
MAX_LINES = 3
ROWS = 3
COLS = 3


symbol_quantity = {
    "A": 4,
    "K": 6,
    "Q": 8,
    "J": 10
}

symbol_multiplier = {
    "A": 6,
    "K": 5,
    "Q": 4,
    "J": 3
}

# takes user input for the amount deposit checks for digits and
# returns the amount of deposit
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

# takes input from the user on how many lines to place bets on,
# checks for digits and line range then returns # of lines
def get_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")

    return lines

# takes the amount for bet per line, checks for int and MAX/MIN bet limit,
# and returns that amount
def take_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

def get_columns(rows, cols, symbols):
    all_symbols = []
    #loops through both key and values
    for symbol, symbol_quantity in symbols.items():
        #appends the symbols+quanities to the list
        for _ in range(symbol_quantity):
            all_symbols.append(symbol)

    columns = []

    for _ in range(cols):
        column = []
        # : used to make a "copy" (not reference) of all_symbols
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

# prints transpose of rows and columns to look like slots in a machine
# uses enumerate to
def print_slots(columns):
    for row in range(len(columns[0])):
        # enumerate gives the index + column
        for i, column in enumerate(columns):
            # if its not equal to last index print pipe
            if i != len(columns) - 1:
                print(column[row], end=" | ") # end with pipe
            else:
                print(column[row], end="")
        print()

# returns a count for winnings and the list of winning lines
def all_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        #transpose we have columns not all rows
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += multiplier[symbol] * bet # per line
            winning_lines.append(line + 1)

    return winnings, winning_lines

# verifies the balance is greater than bet, prints the slots
# and winnings if there are any
def spin(balance):
    lines = get_lines()
    while True:
        bet = take_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}.")

    slots = get_columns(ROWS, COLS, symbol_quantity)
    print_slots(slots)
    winnings, winning_lines = all_winnings(slots, lines, bet, symbol_multiplier)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet

# main runs a while loop to continue the game until there is no more balance
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play or (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

if __name__ == "__main__":
    main()
