
def change(pennies):
    dollars = pennies // 100
    pennies = pennies % 100
    quarters = pennies // 25
    pennies = pennies % 25
    dimes = pennies // 10
    pennies = pennies % 10
    nickels = pennies // 5
    pennies = pennies % 5
    return (dollars, quarters, dimes, nickels, pennies)

