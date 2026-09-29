import display_currency
import show_rates
import show_history
import convert_currency
rates = {
    "USD": 1.00,
    "INR": 88.00,
    "EUR": 0.85,
    "GBP": 0.74,
    "JPY": 147.00,
    "AUD": 1.52,
    "CAD": 1.38,
    "CNY": 7.12
}
currency_names = {
    "USD": "US Dollar",
    "INR": "Indian Rupee",
    "EUR": "Euro",
    "GBP": "British Pound",
    "JPY": "Japanese Yen",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "CNY": "Chinese Yuan"
}

history = []
def display_currencies():
    print("\n------------------------------------------")
    print("          AVAILABLE CURRENCIES")
    print("------------------------------------------")

    for code in rates:
        print(code, "-", currency_names[code])

    print("------------------------------------------")
  def convert_currency():

    display_currencies()

    from_currency = input( 
        "Enter source currency code: "
    ).upper()

    to_currency = input(
        "Enter target currency code: "
    ).upper()

    if from_currency not in rates:
        print("\nInvalid source currency!")
        return

    if to_currency not in rates:
        print("\nInvalid target currency!")
        return
    usd_amount = amount / rates[from_currency]
    converted_amount = usd_amount * rates[to_currency]
    print("\n==========================================")
    print("             CONVERSION RESULT")
    print("==========================================")

    print(
        amount,
        from_currency,
        "=",
        round(converted_amount, 2),
        to_currency
    )

    print("==========================================")
    record = (
        str(amount) + " " + from_currency +
        " -> " +
        str(round(converted_amount, 2)) +
        " " + to_currency
    )

    history.append(record)


    amount = float(input("Enter amount: "))

    if amount < 0:
        print("\nAmount cannot be negative!")
        return
def show_rates():

    display_currencies()

    print("\nExchange rates based on 1 USD:")
    print("------------------------------------------")

    for code in rates:
        print("1 USD =", rates[code], code)

    print("------------------------------------------")
def show_history():

    print("\n==========================================")
    print("           CONVERSION HISTORY")
    print("==========================================")

    if len(history) == 0:
        print("No conversions have been performed yet.")

    else:
        count = 1

        for record in history:
            print(count, ".", record)
            count = count + 1

    print("==========================================")
def currency_information():

    display_currencies()

    code = input(
        "Enter currency code for information: "
    ).upper()

    if code in currency_names:

        print("\n------------------------------------------")
        print("Currency Code :", code)
        print("Currency Name :", currency_names[code])
        print("Rate vs USD   :", rates[code])
        print("------------------------------------------")

    else:
        print("\nInvalid currency code!")
while True:

    print("\n")
    print("==========================================")
    print("       CURRENCY CONVERTER SYSTEM")
    print("==========================================")
    print("1. Convert Currency")
    print("2. View Exchange Rates")
    print("3. View Conversion History")
    print("4. Currency Information")
    print("5. View Available Currencies")
    print("6. Exit")
    print("==========================================")

    choice = input("Enter your choice: ")

    if choice == "1":

        convert_currency()

    elif choice == "2":

        show_rates()

    elif choice == "3":

        show_history()

    elif choice == "4":
       currency_information()

    elif choice == "5":

        display_currencies()

    elif choice == "6":

        print("\nThank you for using Currency Converter!")
        print("Program terminated successfully.")
        break

    else:

        print("\nInvalid choice!")
        print("Please enter a number between 1 and 6.")
    
