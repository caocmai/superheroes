import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        return random.randint(0, self.attack_strength)


class Weapon(Ability):
    def attack(self):
        return random.randint(self.attack // 2, self.attack_strength)


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
        self.deaths = 0
        self.kills = 0

    def add_kill(self, num_kills):
        self.kills = num_kills

    def add_deaths(self, num_deaths):
        self.deaths = num_deaths

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

    # Why need the damage_amt? Not added in this method
    def defend(self):
        blocks = 0
        if not len(self.armors) == 0:
            for block in self.armors:
                blocks += block.block()
        return blocks

    def take_damage(self, damage):
        total_damage = damage - self.defend()
        self.current_health -= total_damage

    def is_alive(self):
        return self.current_health >= 0

    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())

        print(f"{self.name} current health: {self.current_health}. {opponent.name} current health: {opponent.current_health}")

        if self.current_health > opponent.current_health:
            opponent.add_deaths(1)
            self.add_kill(1)
            print(f"{self.name} is the winner")
        else:
            self.add_deaths(1)
            opponent.add_kill(1)
            print(f"{opponent.name} is the winner")


class Team():

    def __init__(self, name):
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(Hero(hero))

    def attack(self, other_team):
        for hero in self.heroes:
            if not hero.is_alive():
                self.heroes.pop(hero)
        
        for villian in other_team.heroes:
            if not villian.is_alive():
                other_team.heroes.pop(hero)

        while len(self.heroes) or len(other_team.heroes) > 0:
            one_alive_hero = random.choice(self.heroes)
            one_alive_villian = random.choice(other_team.heroes)

            one_alive_hero.fight(one_alive_villian)

        
    def stats(self):
        for hero in self.heroes:
            print("Kill/Death:")
            try:
                print(hero.kills/hero.deaths)
            except ZeroDivisionError:
                return 0

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health


awesome = Team("awesome")
awesome.add_hero('hero 1')
awesome.add_hero('hero 2')
awesome.attack("you")
awesome.stats()

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.

#     hero1 = Hero("Wonder Woman")
#     hero2 = Hero("Dumbledore")

#     ability1 = Ability("Super Speed", 300)
#     ability2 = Ability("Super Eyes", 130)
#     ability3 = Ability("Wizard Wand", 80)
#     ability4 = Ability("Wizard Beard", 20)

#     hero1.add_ability(ability1)
#     hero1.add_ability(ability2)

#     hero2.add_ability(ability3)
#     hero2.add_ability(ability4)


#     hero1.fight(hero2)

#     print(hero1.kills)
#     print(hero1.deaths)
#     print(hero2.kills)
#     print(hero2.deaths)
