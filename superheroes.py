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
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = 1

    def add_ability(self, ability):
        self.ability = ability
        return self.abilities.append(ability)


    def attack(self):
        for hit in self.abilities:
            hits += hit
        return hits
            
#     def defend(self, incoming_damage):
#         print("defend")

#     def take_damage(self, damage):

#     def is_alive(self):
#         print("is alive")

#     def fight(opponent):



if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())