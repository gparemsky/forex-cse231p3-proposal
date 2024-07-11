flow_rate_downhill = 100 #gallons per minute
flow_rate_pump = 430 #gallons per minute
mixture_percent_dilution_start = 100
dot_111_tank_car_capacity = 30000
#tanker car can really only carry a max of 198,000 lbs of load, or 30,000 gallons, whichever comes first. 30,000 gallons of methylamine is
#roughly 184,680 lbs

pound_of_water_per_gal = 8.34

pounds_of_methylamine_solution_per_gal = 6.156
#1 gallon is 3785.41 cm^3, assume 40% methylamine in a 60% solution of methanol.
#40% of methylamine of 1 gallon is 1,514.164 cm^3
#60% of methanol of 1 gallon is 2,271.246 cm^3

#methylamine is 0.6562 g/cm^3, or 993.59 grams
#methanol is 0.792 g/cm^3, or 1,798.83 grams

#total weight per gallon is 2792.42 grams, or 6.156 lbs


MENU = "====================================================================================\n" \
       "A: For a given time, how much methylamine could you siphon\n" \
       "B: For a needed amount of methylamine, how much time would it take to siphon\n" \
       "C: What is the percent dilution of methylamine left in the tanker car?\n" \
       "D: Profit calculator\n"


def calculate_time_to_methylamine():
    ''' If your flow gauge is broken, and you only had a stop watch (which measures in seconds) timing the exchange, given the downhill flowrate of methylamine
    how many gallons of methylamine did you collect only given a time start and finish

    returns an amount of gallons which was transfered'''

    gal_per_sec = flow_rate_downhill/60
    #flow rate down hill(gal per min) divided by time(seconds in a minute), is how many gal per seconds we get.

    # TODO ERROR CHECKING
    time = float(input("How much time(seconds) did you have to transfer an amount of methylamine?: "))

    print("in {} seconds, {} gallons amount of methylamine was transfered".format(time,gal_per_sec * time))

    return gal_per_sec*time

def calculate_methylamine_to_time():
    '''given a required amount of methylamine, how much time would it take to exchange that amount?'''

    methylamine_needed = float(input("how much methylamine (gallons) do we need?: "))

    seconds_for_methylamine = methylamine_needed / 1.666 #100 gals per min, or 1.666 gal per second


    gal_water_needed = calculate_water_needed_to_replace_methylamine_weight(methylamine_needed)


    print("to exchange {} gallons of methylamine and pump back {} gallons of water you would need {} minutes and {:.2f} seconds".format(methylamine_needed, gal_water_needed,seconds_for_methylamine//60, seconds_for_methylamine%60))

    return methylamine_needed, seconds_for_methylamine #1, return how much methylmine we want, 2, return the amount of time (seconds) needed for this amount of methylamine

def calculate_water_needed_to_replace_methylamine_weight(gallons_of_methylamine):
    weight_of_methylamine = gallons_of_methylamine * pounds_of_methylamine_solution_per_gal
    gallons_of_water_needed = round(weight_of_methylamine / pound_of_water_per_gal, 2)

    return gallons_of_water_needed

def percent_dilution(gallons_of_methylamine = 0.0):
    '''given an amount of methylamine which was exchanged, an amount of water was put in its place to replace the weight
    calculate how much percent more dilute the tanker car of methylamine has become'''
    gallons_of_methylamine = float(input("\nEnter an amount of methylamine (gallons) obtained: "))

    percent_dilute = round(gallons_of_methylamine/dot_111_tank_car_capacity,2)

    print("The dot-111 tanker car, originally carrying 184,680 lbs (30,000 gallons) of methylamine is now dilute by {:.2f}%".format(percent_dilute))

    return percent_dilute

def calc_profit(amount_of_methylamine = 0.0):
    '''passed in a float for an amount of methylamine, or asked for an amount of methylamine from a text prompt...
    What is the rough profit you could obtain from robbing the train
    For every gallon of methylamine, you could produce $300,000 worth of product
    '''
    while True:
        if amount_of_methylamine <= 0.0:
            amount_of_methylamine = float(input("\nEnter an amount of methylamine obtained: "))
            if amount_of_methylamine <= 0.0:
                print("Amount given:", amount_of_methylamine)
                print("Cannot be zero or less than zero")
                continue
        break

    print("Profits by yeilded product from {} gallons of methylamine: $ {:,.2f}".format(round(amount_of_methylamine,2), amount_of_methylamine * 300000))


def print_results():
    pass

while True:
    #print welcome
    #print main prompt
    #if not run:

    print(MENU)

    user_input = input("Please enter an option: ").lower()
    print()

    if user_input == "a":
        calculate_time_to_methylamine()
    elif user_input == "b":
        calculate_methylamine_to_time()
    elif user_input == "c":
        percent_dilution()
    elif user_input == "d":
        calc_profit()


