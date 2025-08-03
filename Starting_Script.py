import random as rand
import typing

# Rarities chance
rarities = {'common': [i for i in range(1,301)], # 30% (1-300)
            'uncommon': [i for i in range(301,551)], # 25% (301-550)
            'rare': [i for i in range(551, 751)], # 20% (551-750)
            'epic': [i for i in range(751, 901)], # 15% (751-900)
            'legendary': [i for i in range(901, 976)], # 7.5% (901-975)
            'mythic': [i for i in range(976, 1001)] # 2.5% (976-1000)
            }

# Generate Rarities
def assign_rarity(rarities) -> list:
    number = rand.randint(1, 1000)
    for rarity in rarities:
        if number in rarities[rarity]:
            return [rarity, number]

# Item
class Item():
    def __init__(self, name: str):
        self.name = name
        self.rarity, self.value = assign_rarity(rarities)

    def calculate_value(self) -> float:
        if self.rarity == 'mythic':
            return self.value * 3
        elif self.rarity == 'legendary':
            return self.value * 2.5
        elif self.rarity == 'epic':
            return self.value * 2
        elif self.rarity == 'rare':
            return self.value * 1.5
        elif self.rarity == 'uncommon':
            return self.value * 1
        else:
            return self.value * 0.5