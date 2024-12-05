import random


class Coinflips:
    def __init__(self):
        
        self.choice = []
        self.result = []
    
    def play(self, guess):
        if guess not in ["heads", "tails"]:
            raise Warning
        res = random.choice(["heads", "tails"])
        self.choice.append(guess)
        self.result.append(res)

        return res
    
    def __str__(self):
        return ", ".join(self.result)

    def winner(self):
        correct_guesses = 0

        for guess, result in zip(self.choice, self.result):
            if guess == result:
                correct_guesses += 1  
        return correct_guesses > len(self.result) / 2

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