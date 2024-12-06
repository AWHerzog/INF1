
def currency_converter(src, dst, rate):
    def converter(amount):
        converted = amount * rate
        return f"{amount} {src} is {round(converted, 2)} {dst}"
    return converter



print(currency_converter("EUR", "CHF", 1.1)(5))
