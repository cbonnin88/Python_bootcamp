convert_from = input("Enter currency you wish to convert (EURO,USD,GBP,YEN): ")
convert_to = input("Enter currency you wish to receive (EURO,USD,GBP,YEN): ")

# EURO:
if convert_from in ["EURO", "EUR", "euro", "eur", "euros"]:
    amount = float(input("Enter currency amount: "))
    if convert_to in ["EURO", "EUR", "euro", "eur", "euros"]:
        print(amount, 'EUR is equal to', amount * 1, 'EUR')
    elif convert_to in ["USD", "usd", "dollars"]:
        print(round(amount, 2), 'EUR is equal to', round(amount * 1.08, 2), 'USD')
    elif convert_to in ["GBP", "gbp", "pounds"]:
        print(round(amount, 2), 'EUR is equal to', round(amount * 0.85, 2), 'GBP')
    elif convert_to in ["YEN", "yen"]:
        print(round(amount, 2), 'EUR is equal to', round(amount * 163.0, 2), 'JPK')
    else:
        print("Please enter a valid currency")

    # USD:
elif convert_from in ["USD", "usd", "dollars"]:
    amount = float(input("Enter currency amount: "))
    if convert_to in ["USD", "usd", "dollars"]:
        print(amount, 'USD is equal to', amount * 1, 'USD')
    elif convert_to in ["EURO", "EUR", "euro", "eur", "euros"]:
        print(round(amount, 2), 'USD is equal to', round(amount * 0.92, 2), 'EUR')
    elif convert_to in ["GBP", "gbp", "pounds"]:
        print(round(amount, 2), 'USD is equal to', round(amount * 0.78, 2), 'GBP')
    elif convert_to in ["YEN", "yen"]:
        print(round(amount, 2), 'USD is equal to', round(amount * 150.1, 2), 'JPY')
    else:
        print("Please enter a valid currency")

# GBP
elif convert_from in ["GBP", "gbp", "pounds"]:
    amount = float(input("Enter currency amount: "))
    if convert_to in ["GBP", "gbp", "pounds"]:
        print(amount, 'GBP is equal to', amount * 1, 'GBP')
    elif convert_to in ["USD", "usd", "dollars"]:
        print(round(amount, 2), 'GBP is equal to', round(amount * 1.26, 2), 'USD')
    elif convert_to in ["EURO", "EUR", "euro", "eur", "euros"]:
        print(round(amount, 2), 'GBP is equal to', round(amount * 1.16, 2), 'EUR')
    elif convert_to in ["YEN", "yen"]:
        print(round(amount, 2), 'GBP is equal to', round(amount * 190.3, 2), 'JPK')
    else:
        print("Please enter a valid currency")

    # YEN
elif convert_from in ["YEN", "yen"]:
    amount = float(input("Enter currency amount: "))
    if convert_to in ["YEN", "yen"]:
        print(amount, 'JPY is equal to', amount * 1, 'JYN')
    elif convert_to in ["EURO", "EUR", "euro", "eur", "euros"]:
        print(round(amount, 2), 'JPY is equal to', round(amount * 0.006, 2), 'EUR')
    elif convert_to in ["GBP", "gbp", "pounds"]:
        print(round(amount, 2), 'JPY is equal to', round(amount * 0.005, 2), 'GBP')
    elif convert_to in ["USD", "usd", "dollars"]:
        print(round(amount, 2), 'JPY is equal to', round(amount * 0.006, 2), 'USD')
    else:
        print("Please enter a valid currency")
else:
    print("Please enter a valid currency")
