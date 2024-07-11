###########################################################
#  Computer Project #3

# Description: This program calculates mortgage-related information
#  based on user input.

# Algorithm
# Input and Calculation Loop
#    prompt for user inputs
#    Determine which information is provided
#    Handle down payment and APR inputs
#    Determine location-specific information
#    Calculate mortgage-related information based on input

#       if has a square footage only, calculate the monthly payment
#       if has a maximum monthly payment only, find the maximum square footage that they can afford
#       if has both, calculate the monthly payment based on the square footage and check if they can afford it
#       if neither, display not enough information

#       Display results
###########################################################


# Constants
NUMBER_OF_PAYMENTS = 360  # 30-year fixed-rate mortgage, 30 years * 12 monthly payments
SEATTLE_PROPERTY_TAX_RATE = 0.0092
SAN_FRANCISCO_PROPERTY_TAX_RATE = 0.0074
AUSTIN_PROPERTY_TAX_RATE = 0.0181
EAST_LANSING_PROPERTY_TAX_RATE = 0.0162
AVERAGE_NATIONAL_PROPERTY_TAX_RATE = 0.011
SEATTLE_PRICE_PER_SQ_FOOT = 499.0
SAN_FRANCISCO_PRICE_PER_SQ_FOOT = 1000.0
AUSTIN_PRICE_PER_SQ_FOOT = 349.0
EAST_LANSING_PRICE_PER_SQ_FOOT = 170.0
AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT = 244.0
APR_2023 = 0.0668

# Welcome Text
WELCOME_TEXT = '''\nMORTGAGE PLANNING CALCULATOR\n============================ '''
MAIN_PROMPT = '''\nEnter a value for each of the following items or type 'NA' if unknown '''
LOCATIONS_TEXT = '''\nWhere is the house you are considering (Seattle, San Francisco, Austin, East Lansing)? '''
SQUARE_FOOTAGE_TEXT = '''\nWhat is the maximum square footage you are considering? '''
MAX_MONTHLY_PAYMENT_TEXT = '''\nWhat is the maximum monthly payment you can afford? '''
DOWN_PAYMENT_TEXT = '''\nHow much money can you put down as a down payment? '''
APR_TEXT = '''\nWhat is the current annual percentage rate? '''
AMORTIZATION_TEXT = '''\nWould you like to print the monthly payment schedule (Y or N)? '''
LOCATION_NOT_KNOWN_TEXT = '''\nUnknown location. Using national averages for price per square foot and tax rate.'''
NOT_ENOUGH_INFORMATION_TEXT = '''\nYou must either supply a desired square footage or a maximum monthly payment. Please try again.'''
KEEP_GOING_TEXT = '''\nWould you like to make another attempt (Y or N)? '''

# Input and Calculation Loop
keep_going = 'Y'
while keep_going.upper() == 'Y':
    print(WELCOME_TEXT)
    print(MAIN_PROMPT)
    location = input(LOCATIONS_TEXT)
    sq_footage = input(SQUARE_FOOTAGE_TEXT)
    max_monthly_payment = input(MAX_MONTHLY_PAYMENT_TEXT)
    down_payment = input(DOWN_PAYMENT_TEXT)
    apr = input(APR_TEXT)

    # Determine which information is provided
    has_sq_footage = sq_footage.upper() != 'NA'
    has_max_monthly_payment = max_monthly_payment.upper() != 'NA'
    has_down_payment = down_payment.upper() != 'NA'
    has_apr = apr.upper() != 'NA'

    # Handle down payment and APR inputs
    if has_down_payment:
        down_payment = float(down_payment)
    else:
        down_payment = 0.0

    if has_apr:
        apr = float(apr) / 100
    else:
        apr = APR_2023

    monthly_interest_rate = apr / 12

    # Determine location-specific information
    if location.upper() == 'SEATTLE':
        ppsf = SEATTLE_PRICE_PER_SQ_FOOT
        property_tax_rate = SEATTLE_PROPERTY_TAX_RATE
    elif location.upper() == 'SAN FRANCISCO':
        ppsf = SAN_FRANCISCO_PRICE_PER_SQ_FOOT
        property_tax_rate = SAN_FRANCISCO_PROPERTY_TAX_RATE
    elif location.upper() == 'AUSTIN':
        ppsf = AUSTIN_PRICE_PER_SQ_FOOT
        property_tax_rate = AUSTIN_PROPERTY_TAX_RATE
    elif location.upper() == 'EAST LANSING':
        ppsf = EAST_LANSING_PRICE_PER_SQ_FOOT
        property_tax_rate = EAST_LANSING_PROPERTY_TAX_RATE
    else:
        print(LOCATION_NOT_KNOWN_TEXT)
        location = "the average U.S. housing market"
        ppsf = AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT
        property_tax_rate = AVERAGE_NATIONAL_PROPERTY_TAX_RATE

    # Calculate mortgage-related information based on input
    if has_sq_footage:
        sq_footage = float(sq_footage)
        estimated_home_cost = ppsf * sq_footage
        principal = estimated_home_cost - down_payment
        monthly_taxes = (estimated_home_cost * property_tax_rate) / 12
        monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** NUMBER_OF_PAYMENTS) / (
                (1 + monthly_interest_rate) ** NUMBER_OF_PAYMENTS - 1)

        # Display results
        print(f'\n\nIn {location}, an average {sq_footage:,.0f} sq. foot house would cost ${estimated_home_cost:,.0f}.')
        print(f'A 30-year fixed rate mortgage with a down payment of ${down_payment:,.0f} at {apr * 100:.1f}% APR results')
        print(
            f'\tin an expected monthly payment of ${monthly_taxes:,.2f} (taxes) + ${monthly_payment:,.2f} (mortgage payment) = ${monthly_payment + monthly_taxes:,.2f}')

        # if has maximum monthly, check if they can afford it
        if has_max_monthly_payment:
            max_monthly_payment = float(max_monthly_payment)
            print(
                f'Based on your maximum monthly payment of ${max_monthly_payment:,.2f} you can' + (
                    'not' if max_monthly_payment < (monthly_payment + monthly_taxes) else '') + ' afford this house.')

        # print the amortization table
        print_amortization = input(AMORTIZATION_TEXT)
        if print_amortization.upper() == "Y":
            print(f'\n{"Month":^7s}|{"Interest":^12s}|{"Payment":^13s}|{"Balance":^14s}')
            print('=' * 48)
            m = 1
            while principal > 0:
                interest = principal * monthly_interest_rate
                print(f'{m:^7d}| ${interest:>9,.2f} | ${monthly_payment - interest:>10,.2f} | ${principal:>11,.2f}')
                principal -= (monthly_payment - interest)
                m += 1

    elif has_max_monthly_payment:
        max_monthly_payment = float(max_monthly_payment)
        max_square_footage = 100.0
        over_max = False

        # Calculate the maximum square footage based on the maximum monthly payment
        while not over_max:
            estimated_home_cost = max_square_footage * ppsf
            principal = estimated_home_cost - down_payment
            monthly_taxes = (estimated_home_cost * property_tax_rate) / 12
            monthly_payment = principal * (
                    monthly_interest_rate * (1 + monthly_interest_rate) ** NUMBER_OF_PAYMENTS) / (
                                      (1 + monthly_interest_rate) ** NUMBER_OF_PAYMENTS - 1)
            over_max = monthly_payment + monthly_taxes > max_monthly_payment

            if not over_max:
                max_square_footage += 1.0
            else:
                max_square_footage -= 1.0

        estimated_home_cost = max_square_footage * ppsf
        # Display results
        print(
            f'\n\nIn {location}, a maximum monthly payment of ${max_monthly_payment:,.2f} allows the purchase of a house of {max_square_footage:,.0f} sq. feet for ${estimated_home_cost:,.0f}')
        print(
            f'\t assuming a 30-year fixed rate mortgage with a ${down_payment:,.0f} down payment at {apr * 100:.1f}% APR.')
    else:
        print(NOT_ENOUGH_INFORMATION_TEXT)

    keep_going = input(KEEP_GOING_TEXT)
