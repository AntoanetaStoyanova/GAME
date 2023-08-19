import random  #generate the slot machine values kind of randomly

#global constant 
MAX_LINES = 3   # in capital letter because it's a constant value that is not going to change
MAX_BET = 100
MIN_BET = 1

#values that specify the numbers of rows and colums we are going to have in the slot machine
ROWS = 3
COLS = 3

#specify how many symbols are in each of our reals
#dictionary - in every column we will have 2 A, 4 B, 6 C and 8 D . A is going to be the most valiable cause it's not so present in the column
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): # we are loopping in every row 
        symbol = columns[0][line] #check the first symbol so we can see if all symbols in one row are the same
        for column in columns: # loop though all the columns and check for that symbol
            symbol_to_check = column[line] # the symbol to check is eauql to the column at the current row that we are looking at
            if symbol != symbol_to_check:
                break  #if we found one of the symbols is not equal to the previous symbol or equal to all of the symbols that should be in this row, then we just break out the fault
        else: 
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)
    
    return winnings, winning_lines

#what outcome of the slot machine was using the previous values 
def get_slot_machine_spin(rows, cols, symbols):
    # generate what symboles is going to be in each column based on the frequency of symbols that we have 
    # randpmly select symbols for each columns, by list that contains al of the different values we possibly could select from, and randomly choose three of those values 
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []  #define the columns list
    for _ in range(cols):  #generate colimn for every single column that we have, so if we have 3 columns we will generate 3 times the rest of the instructions 
       #picking random values for each row in our column , 
        column = []  # colum, equal to empty list
        current_symbols = all_symbols[:]   #[:] operator referred to as the slice operator , copy of the list that isnt changed 
        for _ in range(rows):  # loops through the number of values that we need to generate, which is equal of the rows that we have in our slot machine
            value = random.choice(current_symbols) # certain number of values of the symbols list
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print() # empty , by default at the end of the empty print statement is gonna continue on the next line 
        

#collect user imput : the deposit that the user's entering as well as their bet 
def deposit():  #collect user imput that gets the deposit from the user
    while True: #using while loop cause i'm going to continully ask the user to enter a deposit amount until they give me a valid amount
        amount = input("What would you like to deposit? $")
        #i need to check if that amount is actually a number
        if amount.isdigit():  #check if the characters are digits, negative number ( -9 ) wont be true
            amount = int(amount)  #if it's a digit , will be converted into amount
            if amount > 0:
                break # will break if amount is greater than zero 
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

#call the deposit function 
#deposit()

#collect the bet from the users , i need to determine how much i want to bet and how many lines the users going to bet on, i will multyply their bet amount by the number of lines
#1 ask the number of lines
def get_number_of_lines():
    #will ask the user to pick a number between one and three
    while True: 
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")   # (1-" + str(MAX_LINES) + ") -> using concatenation and turning the MAX_LINES into a string
        if lines.isdigit():  
            lines = int(lines)  
            if 1 <= lines <= MAX_LINES:  #check if the value is in between two values
                break 
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


#ask how many they want to bet on each line
def get_bet():
    while True: 
        amount = input("What would your like to bet on each line? $")
        if amount.isdigit():  
            amount = int(amount)  
            if MIN_BET <= amount <= MAX_BET:
                break 
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    #CHECK if the amount the user is betting is whithin their balance 
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enought to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is esquel to : ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winning_lines)  # * splat or unpack operator, will pass every single line from the winning_lines list to the print function 
    return winnings - total_bet

#programe
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