print("Welcome to my RPG game!")

def main_menu():

    print("Choose your hero: ")
    print(" 1.) Warrior 2.) Wizard 3.) Medic")
    hero_select = input("Choose your hero: ")
    
    if hero_select == "1":
        hero = Warrior
    elif hero_select == "2":
        hero = Wizard 
    elif hero_select == "3":
        hero = Medic
    else:
        print("You are not worthy!")

    return hero


class Character():
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        while goblin.alive() and hero.alive():
            print("You have {} health and {} power.".format(hero_health, hero_power))
            print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))



class hero(Character):

    def attack(self):
        enemy.health -= self.power
            print("You did {} damage to the goblin.".format(self.power))
            if enemy.health <= 0:
                print("The goblin is dead.")

    def print_status(self):
        print("You have {} health and {} power.".format(hero_health, hero_power))
        print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
        


class goblin(Character):

    def attack(self, enemy):
        enemy.health -= self.power
            print("You did {} damage to the hero.".format(self.power))
            if enemy.health <= 0:
                print("The hero is dead.")

    def print_status(self):
        print("You have {} health and {} power.".format(hero_health, hero_power))
        print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
        

class zombie(Character):

    def attack(self, enemy):
        enemy.health -= self.power
            print("You did {} damage to the hero.".format(self.power))
            if enemy.health <= 0:
                print("The hero is dead.")

    def print_status(self):
        print("You have {} health and {} power.".format(hero_health, hero_power))
        print("The hero has {} health and {} power.".format(hero_health, hero_power))



hero = Hero(10, 5)
goblin = Goblin(6, 2)

hero.attack(goblin)
goblin.attack(hero)

