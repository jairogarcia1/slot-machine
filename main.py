# Global Variables
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on(1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")

    return lines

def get_bet():


def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)

main()