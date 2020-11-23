import random as rnd
import json

def roll(diceNumber, diceFaces, bonus=0, dicestart=1):
    rolls = []
    for _ in range(diceNumber):
        rolls.append(rnd.randint(dicestart,diceFaces))
    total = 0
    if bonus>0:
        total += bonus
    for i in range(diceNumber):
        total += rolls[i]
    return total

char = {
    "name" : "NPC",
    "POD" : roll(3,6),
    "CAR" : roll(3,6),
    "FUE" : roll(3,6),
    "CON" : roll(3,6),
    "DEX" : roll(3,6),
    "INT" : roll(2,6,bonus=6),
    "TAM" : roll(2,6,bonus=6)
}

charjs = json.dumps(char, indent=1)
print(charjs)