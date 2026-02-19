import random
import time

class Character:
    def __init__(self, name, health, attack, defense, special_power):
        self.name = name
        self.__health = health
        self.max_health = health
        self.attack_power = attack
        self.defense = defense
        self.special_power = special_power
    def get_health(self):
        return self.__health
    def health_bar(self):
        total = 20
        filled = int((self.__health / self.max_health) * total)
        bar = "|" * filled + " " * (total - filled)
        return f"{self.name}: [{bar}] {self.__health}/{self.max_health}"

    def take_damage(self, damage):
        damage_taken = max(0, damage - self.defense)
        self.__health -= damage_taken
        if self.__health < 0:
            self.__health = 0
        print(f"{self.name} took {damage_taken} damage")
        print(self.health_bar())
        if self.__health <= 0:
            print(f"{self.name} is defeated")

    def attack(self, target):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        print(f"{self.name} attacks {target.name} with {damage} damage")
        target.take_damage(damage)

    def special_attack(self, target):
        damage = random.randint(self.special_power - 5, self.special_power + 5)
        print(f"{self.name} uses special attack on {target.name} with {damage} damage")
        target.take_damage(damage)
    def is_alive(self):
        return self.__health > 0

class Player(Character):
    def choose_action(self, target):
        print("\nChoose action")
        print("1 Attack")
        print("2 Special Attack")
        print("3 Defend")
        choice = input("> ")
        if choice == "1":
            self.attack(target)
        elif choice == "2":
            self.special_attack(target)
        elif choice == "3":
            print(f"{self.name} is defending")
            self.defense += 5
        else:
            print("Invalid choice. Default attack used")
            self.attack(target)
class Enemy(Character):
    def choose_action(self, target):
        action = random.choice(["attack", "special", "defend"])
        if action == "attack":
            self.attack(target)
        elif action == "special":
            self.special_attack(target)
        else:
            print(f"{self.name} is defending")
            self.defense += 3

def battle_game():
    print("Battle Game")
    player_name = input("Enter player name: ")
    player = Player(player_name, 100, 20, 5, 30)
    enemies = [
        Enemy("Bunty", 80, 15, 3, 25),
        Enemy("Babli", 120, 18, 5, 28),
        Enemy("Milo", 90, 12, 4, 35)
    ]
    enemy = random.choice(enemies)
    print("\nBattle started")
    print(player.name, "vs", enemy.name)
    turn = 1
    while player.is_alive() and enemy.is_alive():
        print("\nTurn", turn)
        print(player.health_bar())
        print(enemy.health_bar())
        player.choose_action(enemy)

        if enemy.is_alive():
            enemy.choose_action(player)
        player.defense = 5
        enemy.defense = enemy.defense - 3 if enemy.defense > 3 else enemy.defense
        turn += 1
        time.sleep(1)
    if player.is_alive():
        print("\nYou win")
    else:
        print("\nYou lost")
if __name__ == "__main__":
    battle_game()
