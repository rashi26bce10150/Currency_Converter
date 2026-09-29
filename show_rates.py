def show_rates():

    display_currencies()

    print("\nExchange rates based on 1 USD:")
    print("------------------------------------------")

    for code in rates:
        print("1 USD =", rates[code], code)

    print("------------------------------------------")
