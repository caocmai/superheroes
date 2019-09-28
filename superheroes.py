import random

# Class that returns random attack amount for ability name and max strength
class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        return random.randint(0, self.attack_strength)

# Class that returns random attack amount that starts at least 1/2 the minimum
class Weapon(Ability):
    def attack(self):
        return random.randint(self.attack_strength // 2, self.attack_strength)

# Class that return random defense/block with max block input
class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    
    def block(self):
        return random.randint(0, self.max_block)

class Hero:
    # Initializes the hero class, with starting health as 100 by default
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.deaths = 0
        self.kills = 0

    # Setter function to add weapon to abilities; in this case adding object
    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    # def add_armor(self, armor):
    #     self.abilities.append(armor)

    # Setter function to add armor to armors; in this case adding object
    def add_armor(self, armor):
        self.armors.append(armor)

    # Setter add number of kills
    def add_kill(self, num_kills):
        self.kills += num_kills

    # This is a setter add number of deaths
    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

    # Add Ability object from Ability class. This is a setter
    def add_ability(self, ability):
        # self.ability = ability
        self.abilities.append(ability) 

    # Attack method that returns the TOTAL of all the attacks in the ability list
    # Can use .attack() from Weapons class because the object passed in is the Weapons object
    def attack(self):
        hits = 0
        for hit in self.abilities:
            hits += hit.attack()
        return hits

    # Why need the damage_amt? Not added in this method
    # Exactly like the attack method above except this time it's the block method from Armor
    def defend(self):
        blocks = 0
        if not len(self.armors) == 0:
            for block in self.armors:
                blocks += block.block()
        return blocks

    # This is the meat and potatoe of this Hero class. This method updates the amount of 
    # current health by taking the total (attack()) = (damage) and subtracting total defend()
    def take_damage(self, damage):
        absolute_damge = damage - self.defend()
        self.current_health -= absolute_damge

    # Returns True if current_health is greater than 0, and reverse if less than 0
    def is_alive(self):
        return self.current_health > 0

    # Method to determine who wins when fighting each other
    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())

            # print(f"{self.name} current health: {self.current_health}. {opponent.name} current health: {opponent.current_health}")

            if self.is_alive() and not opponent.is_alive():
                opponent.add_deaths(1)
                self.add_kill(1)
                print(f"{self.name} is the winner")
            elif not self.is_alive() and opponent.is_alive():
                self.add_deaths(1)
                opponent.add_kill(1)
                print(f"{opponent.name} is the winner")


class Team():
    # Initizalizes Team class
    def __init__(self, name):
        self.name = name
        # To add objects of Hero class
        self.heroes = []

    # Removes a hero with passed in hero
    # hero.name refers tot he Hero class name not Team class name
    # because objects in heroes list are from Hero class
    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
        return False

    # Can use the .name from the Hero class because passing in Hero object
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)
    
    # To add heros object from Hero class
    def add_hero(self, hero):
        self.heroes.append(hero)

    # Check to make sure at least one alive hero in heroes list
    def is_hero_alive(self):
        # Looping to make sure at least one alive hero-object in heroes list
        for hero in self.heroes:
            # Can use is_alive becuase of again, passing in Hero class objects
            if hero.is_alive():
                return True
        return False

    def attack(self, other_team):
        # If at least one alive hero in self and other team, then fight
        while self.is_hero_alive() and other_team.is_hero_alive():
            one_alive_hero = random.choice(self.heroes)
            one_alive_villian = random.choice(other_team.heroes)
            print(f"Hero {one_alive_hero.name} is fighting hero {one_alive_villian.name}")
            one_alive_hero.fight(one_alive_villian)

            for hero in self.heroes:
              print("hero name: " + str(hero.name))
              print("hero heath: " + str(hero.current_health))
              if hero.current_health < 0:
                self.heroes.remove(hero)

            for hero in other_team.heroes:
              print("other team hero name:  " + str(hero.name))
              print("other team hero healt: " + str(hero.current_health))
              if hero.current_health < 0:
                other_team.heroes.remove(hero)

            print("home alive hero: ")
            self.view_all_heroes()
            print("other alive heroes: ")
            other_team.view_all_heroes()
            print("-----------")

        if len(self.heroes) == 0:
            print(f"{self.name} Team one wins")
        elif len(other_team.heroes) == 0:
            print(f"{other_team.name} Team 2 wins")



    # Printing out the stats of kill/deaths ratio
    def stats(self):
        for hero in self.heroes:
            if hero.deaths > 0:
                kill_ratio = hero.kills // hero.deaths
                print(f"{hero.name} kill ratio is {kill_ratio}")
            else:
                print(f"{hero.name} kill ratio is {hero.kills}")


            # print("Kill/Death:")
            # try:
            #     print(hero.kills/hero.deaths)
            # except ZeroDivisionError:
            #     return 0

    # To revive all heros in the list of heros
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health


class Arena:

    # Initializes Arena class to have two teams
    def __init__(self):
        self.team_one = None
        self.team_two = None

    # To create ability and return the entire Ability class
    # And Ability class returns a random attack value when called
    def create_ability(self):
        ability_name = input("Enter ability name: ")
        ability_attack_strength = input("Enter max strength for ability: ")
        return Ability(ability_name, int(ability_attack_strength))

    # To create weapon and return the Weapon class
    # Not calling it just creating
    def create_weapon(self):
        weapon_name = input("Enter weapon name: ")
        weapon_strength = input("Enter weapon strength: ")
        return Weapon(weapon_name, int(weapon_strength))

    # To create armor and return the Armor class
    def create_armor(self):
        armor_name = input("Enter armor name: ")
        armor_strength = input("Enter armor strength: ")
        return Armor(armor_name, int(armor_strength))

    # Create hero along with armors, abilities, and weapons
    def create_hero(self):
        name = input("Give your hero a name: ")
        health = input("Enter the starting health of your hero: ")
        hero = Hero(name, int(health))

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
        team_name = input("Enter Team One name: ")
        self.team_one = Team(team_name)

        while True:
            try:
                user_choice = int(input("Enter number of heroes to add to Team One: "))
            except ValueError:
                continue
            else:
                break

        for i in range(user_choice, 0, -1):
            placement = user_choice - (i - 1)
            print(f"For Team One named: {self.team_one.name} of hero {placement}, add the hero's name and abilities.")
            new_hero = self.create_hero()
            self.team_one.add_hero(new_hero)
            print("-------------------")

    def build_team_two(self):
        team_name = input("Enter Team Two name: ")
        self.team_two = Team(team_name)

        while True:
            try:
                user_choice = int(input("Enter number of heroes to add to Team Two: "))
            except ValueError:
                continue
            else:
                break

        for i in range(user_choice, 0, -1):
            placement = user_choice - (i - 1) # Just so print out to user that makes sense numerically
            print(f"For Team Two named: {self.team_two.name} of hero {placement}, add the hero's name and abilities.")
            new_hero = self.create_hero()
            self.team_two.add_hero(new_hero)
            print("-----------------")


    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        self.team_one.stats()
        self.team_two.stats()

        # alive_heros_team_one = []
        # alive_heros_team_two = []
        
        # for hero in self.team_one.heroes:
        #     if hero.is_alive():
        #         alive_heros_team_one.append(hero.name)

        # for hero in self.team_two.heroes:
        #     if hero.is_alive():
        #         alive_heros_team_two.append(hero.name)

        # print(f"These are the current alive heros on Team One: {alive_heros_team_one}")
        # print(f"These are the current alive heros on Team Two: {alive_heros_team_two}") 

        # if len(alive_heros_team_one) == 0:
        #     print("Team Two won!")
        # if len(alive_heros_team_two) == 0:
        #     print("Team One won!")

# awesome = Team("awesome")
# awesome.add_hero('hero 1')
# awesome.add_hero('hero 2')
# awesome.attack("you")
# awesome.stats()

if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()

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
