# Objectives of this project:

Learn to handle scrubbing dirty input, do currency conversions using abstract units of measurments (pips and lots)

This project mainly relies on the comprehension of loops, conditional statements, and fstrings. \
(There is a use of "eval" which may be innaproriate for this project, if so, lines 166 and 225 need to be re-thought out)

The goal of this readme is to breakdown the project into modules. **The code of this project is 240 lines**\
where the instructor code for old project 3 is about 170. I will leave it upto whom ever has the final say\
to add, remove or reconfigure, modules from to this project in order to craft a more suited project 3 for CSE231. 

## Project breakdown

- ### Setting up the users account

Lines: 73 -> 126, 152 -> 154 \
Total: **55 lines**

![image](assets/initial_currency_input.gif)

On every run of the program, the user will be asked to input a currency, either USD or EUR, and an amount. \
Both the account currency type, and currency amount input have error checking implemented.
This will represent how much money the user is working with and all calculation in the program will rely on it.\
The user also has the option to change their currency and amount on the fly with a menu option (option 3).

When selecting menu 3, we are presented with a prompt to either pick a new currency, or just press enter for\
the default entry. There is error checking implemented here as well.

![image](assets/changing_account_currency.gif)

- ### Menu option 1, calculating position size

Lines: 206 -> 234, (relies on (10) lines 136 -> 146 for calculating pip value)\
Total: **28 lines**

On the left is an [online currency calculator](https://www.myfxbook.com/forex-calculators/position-size/USDJPY), plugged into API's that constantly get updated forex rates.\
On the right is the python program with a set of static values set at the top of the program,\
*which is why there may be a small discrepancy between the two, but the math will always return similar results.*

DEMO
![image](assets/pos_size_demo.gif)

**Explination:**

- **Account Currency** will be what currency our broker is accepting, This currency would appear in our trading account to use as leverage for trading. So if we are in the USA, we will be using USD.
- **Currency Pair** is the pair of currency we are treating as an asset (like one would treat TSLA in the stock market) to execute our trades against.
- **Account size** is the amount of money we have in our trading account to use as leverage for trades.
- **Risk ratio** is simply the percent amount of our account size we are willing to lose on one trade. Typically 2-5%
- **Stop-Loss in pips** every point the market moves in forex is called a pip, if the market moves 50 pips on EUR/USD, An example of the market value of EUR/USD could have moved from 1.0850 to 1.0900 where one pip is one digit in the fourth decimal place, or one ten thousandth of a currency pair value \
*(this is not true for one exception, any pair with the japanese yen, where we measure one pip in the 100th's place, 161.54 to 161.64 is a 10 pip movement)* [further explanation on pips can be found below](#explaining-pips)
- **Trade size** - in the online calculator, trade size is just a reference for how big of lots we are trading in, standard lot sizes are 1.0, so we will keep it as one. [further explanation on lots can be found below](#explaining-lot-sizes)

**Calculation**

The calculation for position size can be found on line 228
```python
position_size = (((account_balance * risk_percent)/pip_stoploss)/pip_value_per_lot)
```
position size relies on four values, three of which the user gives to us (acc balance, risk percent of acc, and pip stoploss) the fourth value requires some calculation which is done on the code block on lines 136 to 146\
```python
    if account_currency == "USD":
        pip_value_per_lot_USD = STANDARD_PIP * STANDARD_LOT_SIZE
        pip_value_per_lot_SGD = (STANDARD_PIP / USDSGD) * STANDARD_LOT_SIZE
        pip_value_per_lot_JPY = (JPY_PIP / USDJPY) * STANDARD_LOT_SIZE
        pip_value_per_lot_CHF = (STANDARD_PIP / USDCHF) * STANDARD_LOT_SIZE
    elif account_currency == "EUR":
        pip_value_per_lot_EUR = STANDARD_PIP * STANDARD_LOT_SIZE
        pip_value_per_lot_SGD = (STANDARD_PIP / EURSGD) * STANDARD_LOT_SIZE
        pip_value_per_lot_JPY = (JPY_PIP / EURJPY) * STANDARD_LOT_SIZE
        pip_value_per_lot_CHF = (STANDARD_PIP / EURCHF) * STANDARD_LOT_SIZE
        pip_value_per_lot_USD = (STANDARD_PIP / EURUSD) * STANDARD_LOT_SIZE
```


[more about position size can be found here](https://learningcenter.fxstreet.com/education/learning-center/unit-3/chapter-3/the-position-size/index.html)


### explaining pips

### explaining lot sizes