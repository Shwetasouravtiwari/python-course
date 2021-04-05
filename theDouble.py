def doubleChar(doubleit):
    doubled = []
    for letter in doubleit:
        doubled.append(letter * 2)
    print("".join(doubled))

doubleChar('the')