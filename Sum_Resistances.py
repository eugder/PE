def series_resistance(lst):
    result = sum(lst)
    if result <= 1:
        endfix = " ohm"
    else:
        endfix = " ohms"

    return str(result) + endfix

print(series_resistance([16, 3.5, 6]))