import random

def roll(num_dice, num_sides):
    total = 0
    for i in range(num_dice):
        roll = random.randint(1, num_sides)
        total += roll
    print(f"You rolled a {total}")
roll(3, 6)
