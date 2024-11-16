import random

class Coinflips:
    def __init__(self):
        self.__results = []
        self.__choice = []


    def play(self, choice):
        if choice not in ["heads", "tails"]:
            raise Warning
        list1 = ["heads", "tails"]
        winner = random.choice(list1)
        self.__results.append(winner)
        self.__choice.append(choice)

        return winner

    def winner(self):
        wins = sum([1 for h, c in zip(self.__results, self.__choices) if h == c])
        losses = len(self.__results) - wins
        return wins > losses

    def __str__(self):
        return ", ".join(self.__results)


t = Coinflips()
try:
    t.play("arms")
except Warning:
    print("invalid choice")
# Your play results may be different from this example due to randomness
print(t.play("heads"))
print(t.play("tails"))
print(t.play("heads"))
print(t)
print(t.winner())