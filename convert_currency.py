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
