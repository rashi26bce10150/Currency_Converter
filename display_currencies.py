def display_currencies():
    print("\n------------------------------------------")
    print("          AVAILABLE CURRENCIES")
    print("------------------------------------------")

    for code in rates:
        print(code, "-", currency_names[code])

    print("------------------------------------------")
