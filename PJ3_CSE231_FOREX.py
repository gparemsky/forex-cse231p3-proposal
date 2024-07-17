########################################
# Computer project #3
#
# Desc
#
# Algorithm
#
#
#
#
########################################


#Constants
program_loops = 0
change_account_balance_flag = False
account_currency = ''
account_balance = 0.0
valid_account_currencies_abbreviation = 'USD/EUR'
valid_currency_pairs = 'EURUSD/GBPUSD/USDSGD/USDJPY/EURCHF'


#PIP SIZE AND LOT SIZE TO NUMERICAL DEFINITIONS
JPY_PIP = 0.01             #ONLY THE JAPANESE YEN IS SPECIAL AND USES 2 DECIMAL PLACES
STANDARD_PIP = 0.0001      #PIP IS 1/10,000TH OF A CURRENCY, 4 DECIMAL PLACES, A PIPETTE IS 5 DECIMAL PLACES BUT WE WONT USE THOSE HERE
STANDARD_LOT_SIZE = 100000 #100,000 OR 1.0
MINI_LOT_SIZE = 10000      #10,000 OR 0.1
MICRO_LOT_SIZE = 1000      #1,000 OR 0.01

#prices taken July 10, 2024, 14:31 GMT
EURUSD = 1.0826 #EUR/USD - every 1 Euro is worth 1.0826 USD
GBPUSD = 1.2839 #GBP/USD - every 1 British pound is worth 1.2839 USD
USDSGD = 1.3488 #USD/SGD - every 1 USD dollar is 1.3488 Singapore dollar
USDJPY = 161.57 #USD/JPY - every 1 USD is worth 161.57 Japanese yen
EURCHF = 0.9735 #EUR/CHF - every 1 Euro is worth 0.9735 swiss franc's

EURJPY = 172.62 #EUR/JPY - every 1 Euro is worth 172.62 Japanese yen
EURSGD = 1.4611 #EUR/SGD - every 1 Euro is worth 1.4611 Singapore dollar

#conversion for usd to swiss franc
#price taken July 10, 2024, 23:11 GMT
USDCHF = 0.8992


#Prompt Texts
WELCOME_TEXT = '*** forex trading multi-calculator and tracker ***'
MAIN_PROMPT = ''
CURRENCY_PAIR_TEXT = 'Enter currency pair (EURUSD, GBPUSD, USDSGD, USDJPY, EURCHF): '
ACCOUNT_CURRENCY_TEXT = 'Enter the account currency (USD, EUR): '
ACCOUNT_BALANCE_TEXT = 'Enter the current balance of your account: '
ACCOUNT_BALANCE_INVALID_TEXT = 'Please input either an int or a float without comma separators'
TRADE_SIZE_TEXT = 'Input trade size in lots (1.0, 0.1, 0.01): (user input)'
OPEN_PRICE_TEXT = 'Enter open price: '
CLOSE_PRICE_TEXT = 'Enter close price: '


MAIN_MENU = '''
[1] Position Size Calculator
[2] Profit calculator
[3] Change account currency and balance

enter "e" to exit program

'''

print(WELCOME_TEXT)
print(MAIN_PROMPT)


keep_going = ''

while keep_going.upper() != 'E':

    if program_loops == 0 or change_account_balance_flag == True:
        #set the currency of the account (valid are USD, EUR, and GBP)

        # if we already had a currency set from the previous loop, then show the user the last one, and re-use it if the user entered a blank one.
        if account_currency:
            ac_old = account_currency

            while True:
                account_currency = input(ACCOUNT_CURRENCY_TEXT+f'(default: {account_currency}): ').upper()
                if not account_currency:
                    account_currency = ac_old
                if account_currency not in valid_account_currencies_abbreviation:
                    print('typo or currency not valid')
                    continue
                break

        #if this is the first loop around, then our account_currency variable is empty, and needs to be set here
        else:
            while True:
                account_currency = input(ACCOUNT_CURRENCY_TEXT).upper()
                if account_currency not in valid_account_currencies_abbreviation:
                    print('typo or currency not valid')
                    continue
                break


        ## Block of code to practice error checking
        while True:
            dot_count = 0 #how many dots are in the input amount, 1.54 is valid, 1.54.23 is invalid
            valid = False #valid flag
            account_balance = input(ACCOUNT_BALANCE_TEXT)

            for i in account_balance:  # For every charecter in the text the user gave
                if i not in '1234567890.':  # check if the charecter is in the string(list) of approved charecters, numbers or a period
                    #fun todo - if a user appends a + or - to the front of an account balance, it would take the previous balance and add or subtract what they enter after the + or -
                    valid = False
                    print(ACCOUNT_BALANCE_INVALID_TEXT)  # if its not, such as 'a' or '(' then set valid to false, break from the for loop, and continue
                    break
                if i == '.':  # if the charecter is a dot, thats okay, but we cant have more than one dot in an account balance. so keep track of it
                    dot_count += 1
                if dot_count > 1:  # if our dot count ever exceeds one, then we set the valid flag to false, and break the for loop.
                    valid = False
                    print(ACCOUNT_BALANCE_INVALID_TEXT)
                    break
                valid = True

            if not valid:  # if the valid flag is false, restart the loop.
                continue
            else:  # if it's not false, continue to the main menu of the program.
                break
        change_account_balance_flag = False

    print("======================================")
    print(f"Account: {account_currency} {float(account_balance):,.2f}")
    print(MAIN_MENU)

    account_balance = float(account_balance)

    keep_going_user_input = input() #this is the users menu choice

    if keep_going_user_input == '3': #change the calculators account currency and balance. ------------------------------------------------------------------------------------------------
        change_account_balance_flag = True
    elif keep_going_user_input == '2': #calculate profit from pip increase or decrease, with position direction stake ---------------------------------------------------------------------

        while True:
            currency_pair = input(CURRENCY_PAIR_TEXT).upper()
            if currency_pair not in valid_currency_pairs:
                print("Invalid Pair - Please enter an approved currency pair")
                continue
            break

        if account_currency == "USD":
            if currency_pair[3:6] == 'USD':
                pip_value_per_lot = STANDARD_PIP * STANDARD_LOT_SIZE
            elif currency_pair[3:6] == 'SGD':
                pip_value_per_lot = (STANDARD_PIP / USDSGD) * STANDARD_LOT_SIZE
            elif currency_pair[3:6] == 'JPY':
                pip_value_per_lot = (JPY_PIP / USDJPY) * STANDARD_LOT_SIZE
            elif currency_pair[3:6] == 'CHF':
                pip_value_per_lot = (STANDARD_PIP / USDCHF) * STANDARD_LOT_SIZE
        elif account_currency == "EUR":
            if currency_pair[3:6] == 'EUR':
                pip_value_per_lot = STANDARD_PIP * STANDARD_LOT_SIZE
            elif currency_pair[3:6] == 'SGD':
                pip_value_per_lot = (STANDARD_PIP / EURSGD) * STANDARD_LOT_SIZE
            elif currency_pair[3:6] == 'JPY':
                pip_value_per_lot = (JPY_PIP / EURJPY) * STANDARD_LOT_SIZE
            elif currency_pair[3:6] == 'CHF':
                pip_value_per_lot = (STANDARD_PIP / EURCHF) * STANDARD_LOT_SIZE
            elif currency_pair[3:6] == 'USD':
                pip_value_per_lot = (STANDARD_PIP / EURUSD) * STANDARD_LOT_SIZE

        trade_size_in_lots = float(input("Please enter trade size in lots: "))
        print(f"--- Entered {trade_size_in_lots} lots ---")

        open_price = float(input(OPEN_PRICE_TEXT))
        print(f"--- Entered {open_price} open price ---")

        close_price = float(input(CLOSE_PRICE_TEXT))
        print(f"--- Entered {close_price} close price ---")

        if "JPY" in currency_pair:
            pip_delta = (close_price - open_price) * 100
        else:
            pip_delta = (close_price - open_price) * 10000

        print(f"--- Market change {pip_delta} pips ---")

        trade_direction = input("Please enter trade direction ((b)uy or (s)ell): ").lower()
        if trade_direction == "b" or trade_direction == "buy":
            print(f"--- Entered long position ---")
            trade_direction = "b"

        if trade_direction == "s" or trade_direction == "sell":
            print(f"--- Entered short position ---")
            trade_direction = "s"


        profit = trade_size_in_lots * pip_value_per_lot * pip_delta

        if trade_direction == "s":
            profit = profit * -1

        print(f"Profit = {account_currency} {profit:,.2f}")

        print()
        input("press enter to continue...")
        print()
        print()

    elif keep_going_user_input == '1': #calculate position size to take in pips from risk percent -----------------------------------------------------------------------------------------
        risk_percent = (float(input(f"How much of your account ({account_currency} {account_balance:,.2f}) are you willing to risk? (%): "))/100)
        print(f"--- Entered {risk_percent}% - {((risk_percent)*account_balance)} ---") #for debug, make dynamic sentence structure down below later.
        pip_stoploss = int(input("how many pips are you willing to gamble? (stoploss in integer): "))
        print(f"--- Entered {pip_stoploss} pips ---")

        while True:
            currency_pair = input(CURRENCY_PAIR_TEXT).upper()
            if currency_pair not in valid_currency_pairs:
                print("Invalid Pair - Please enter an approved currency pair")
                continue
            break

        print(f"--- Entered currency pair {currency_pair} ---")

        # calculate pip_value_per_lot for each trade currency

        if account_currency == "USD":
            if currency_pair[3:6] == 'USD':
                pip_value_per_lot = STANDARD_PIP * STANDARD_LOT_SIZE
            elif currency_pair[3:6] == 'SGD':
                pip_value_per_lot = (STANDARD_PIP / USDSGD) * STANDARD_LOT_SIZE
            elif currency_pair[3:6] == 'JPY':
                pip_value_per_lot = (JPY_PIP / USDJPY) * STANDARD_LOT_SIZE
            elif currency_pair[3:6] == 'CHF':
                pip_value_per_lot = (STANDARD_PIP / USDCHF) * STANDARD_LOT_SIZE
        elif account_currency == "EUR":
            if currency_pair[3:6] == 'EUR':
                pip_value_per_lot = STANDARD_PIP * STANDARD_LOT_SIZE
            elif currency_pair[3:6] == 'SGD':
                pip_value_per_lot = (STANDARD_PIP / EURSGD) * STANDARD_LOT_SIZE
            elif currency_pair[3:6] == 'JPY':
                pip_value_per_lot = (JPY_PIP / EURJPY) * STANDARD_LOT_SIZE
            elif currency_pair[3:6] == 'CHF':
                pip_value_per_lot = (STANDARD_PIP / EURCHF) * STANDARD_LOT_SIZE
            elif currency_pair[3:6] == 'USD':
                pip_value_per_lot = (STANDARD_PIP / EURUSD) * STANDARD_LOT_SIZE


        # calculate position size
        position_size = (((account_balance * risk_percent)/pip_stoploss)/pip_value_per_lot)

        print()
        print(f"With an account balance of {account_currency} {account_balance:,.2f}, taking a {risk_percent}% risk with a {pip_stoploss} pip stoploss.\n\
A position of {position_size:,.2f} lots should be staked in {currency_pair[0:3]+'/'+currency_pair[3:6]}")
        print()
        input("press enter to continue...")

    else:
        keep_going = keep_going_user_input
    program_loops += 1


