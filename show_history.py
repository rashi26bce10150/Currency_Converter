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
