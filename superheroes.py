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

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        ability_name = input("Enter ability name: ")
        ability_attack_strength = input("Enter max strength for ability: ")
        return Ability(ability_name, int(ability_attack_strength))

    def create_weapon(self):
        weapon_name = input("Enter weapon name: ")
        weapon_strength = input("Enter weapon strength: ")
        return Weapon(weapon_name, int(weapon_strength))

    def create_armor(self):
        armor_name = input("Enter armor name: ")
        armor_strength = input("Enter armor strength: ")
        return Armor(armor_name, int(armor_strength))

    def create_hero(self):
        name = input("Give your hero a name: ")
        health = int(input("Enter the starting health of your hero: "))
        hero = Hero(name, health)

        running = True
        while running:
            user_choice = input("To add ability type 'a'. To add armor type 'r'. To add new weapon type 'w'. Once finished type 'q'. ")

            if user_choice == 'a':
                new_ability = self.create_ability()
                hero.add_ability(new_ability)

            if user_choice == 'r':
                new_armor = self.create_armor()
                hero.add_armor(new_armor)

            if user_choice == 'w':
                new_weapon = self.create_weapon()
                hero.add_weapon(new_weapon)

            if user_choice == 'q':
                running = False

        return hero

    def build_team_one(self):
        user_choice = int(input("Enter number of heroes to add to Team One: "))

        for i in range(user_choice, 0, -1):
            placement = user_choice - (i - 1)
            print(f"For hero {placement} add the hero name and abilities.")
            new_hero = self.create_hero()
            self.team_one.add_hero(new_hero)

    def build_team_two(self):
        user_choice = int(input("Enter number of heroes to add to Team Two: "))

        for i in range(user_choice, 0, -1):
            placement = user_choice - (i - 1)
            print(f"For hero {placement} add the hero name and abilities.")
            new_hero = self.create_hero()
            self.team_two.add_hero(new_hero)


    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        self.team_one.stats()
        self.team_two.stats()

        alive_heros_team_one = []
        alive_heros_team_two = []
        
        for hero in self.team_one.heroes:
            if hero.is_alive():
                alive_heros_team_one.append(hero.name)

        for hero in self.team_two.heroes:
            if hero.is_alive():
                alive_heros_team_two.append(hero.name)

        print(f"These are the current alive heros on Team One: {alive_heros_team_one}")
        print(f"These are the current alive heros on Team Two: {alive_heros_team_two}") 

        if alive_heros_team_one == 0:
            print("Team Two won!")
        if alive_heros_team_two == 0:
            print("Team One won!")

class Hero:

    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.deaths = 0
        self.kills = 0

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    # def add_armor(self, armor):
    #     self.abilities.append(armor)

    # Add Armor object
    def add_armor(self, armor):
        self.armors.append(armor)

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
        self.heroes.append(hero)

    def attack(self, other_team):

        # Why does this not work!!!
        # while len(self.heroes) > 0 and len(other_team.heroes) > 0:
        #     for hero in self.heroes:
        #         if not hero.is_alive():
        #             self.heroes.remove(hero)

        #     for villian in other_team.heroes:
        #         if not villian.is_alive():
        #             other_team.heroes.remove(villian)
                
            one_alive_hero = random.choice(self.heroes)
            one_alive_villian = random.choice(other_team.heroes)

            one_alive_hero.fight(one_alive_villian)

        
    def stats(self):
        for hero in self.heroes:
            if hero.deaths > 0:
                kill_ratio = hero.kills // hero.deaths
                print(f"{hero.name} hero kill ratio is {kill_ratio}")
            else:
                print(f"{hero.name} hero kill ratio is {hero.kills}")


            # print("Kill/Death:")
            # try:
            #     print(hero.kills/hero.deaths)
            # except ZeroDivisionError:
            #     return 0

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health


# awesome = Team("awesome")
# awesome.add_hero('hero 1')
# awesome.add_hero('hero 2')
# awesome.attack("you")
# awesome.stats()

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
