import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        return random.randint(0, self.attack_strength)

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    
    def block(self):
        return random.randint(0, self.max_block)

class Hero:

    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []

    # Add Ability object
    def add_ability(self, ability):
        # self.ability = ability
        self.abilities.append(ability)


    def attack(self):
        hits = 0
        for hit in self.abilities:
            hits += hit.attack()
        return hits

    # Add Armor object
    def add_armor(self, armor):
        self.armors.append(armor)

    # Why need this damage_amt?
    def defend(self, damage_amt=0):
        blocks = 0
        if not len(self.armors) == 0:
            for block in self.armors:
                blocks += block.block()
        return blocks

    def take_damage(self, damage):
        total_damage = damage - self.defend(damage)
        self.current_health -= total_damage

    def is_alive(self):
        return self.current_health >= 0

    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())

        print(f"{self.name} current health: {self.current_health}. {opponent.name} current health: {opponent.current_health}")

        if self.current_health > opponent.current_health:
            print(f"Hero 1 wins, which is {self.name}")
        else:
            print(f"Hero 2 wins, which is {opponent.name}")

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)

    # for stuff in hero.abilities:
    #     print(stuff.attack())