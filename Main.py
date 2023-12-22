import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)


def deposit():
    ph = 0
    # ph means PlaceHolder, it can be ph, ph2, ph3...
    while ph == 0:
        print("Must be a valid INT")
        amount = input("Money deposited: R$")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print(f"Good! R${amount}.00 deposited sucessfully")
                ph = 1
            else:
                print("Amount must be greater than 0 (ZERO)\n\n")
        else:
            print("Please enter a valid number\n\n")
    return amount


def get_number_of_lines():
    ph = 0
    while ph == 0:
        print(f"Must be a valid INT between 0 to {MAX_LINES}")
        lines = input("Enter the number of lines: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                print(f"Good! {lines} lines set!")
                ph = 1
            else:
                print(f"Amount must be between 0 and {MAX_LINES}\n\n")
        else:
            print(f"Please enter a valid number between 0 and {MAX_LINES}\n\n")
    return lines


def get_bet():
    ph = 0
    while ph == 0:
        print("Must be a valid INT")
        amount = input("Money you like to bet on each line: R$")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                print(f"Good! R${amount}.00 in each line! Lets goo")
                ph = 1
            else:
                print(f"Please enter a valid number between R${MIN_BET} and R${MAX_BET}\n\n")
        else:
            print("Please enter a valid number\n\n")
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough to bet, your balance is R${balance}")
        else:
            break


main()