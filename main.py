import random
class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20  # Default attack power for darts

    def attack(self, other, weapon):
        if weapon == "лук":
            damage = 40
        else:
            damage = 20

        other.health -= damage
        print(f"{self.name} атакует {other.name} с помощью {weapon} и наносит {damage} урона.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self):
        self.player = Hero(input("Введите имя вашего героя: "))
        self.computer = Hero("Монстр")

    def start(self):
        weapons = ["лук", "дротики"]

        while self.player.is_alive() and self.computer.is_alive():
            print(f"\n{self.player.name} здоровье: {self.player.health}")
            print(f"{self.computer.name} здоровье: {self.computer.health}")

            # Игрок делает ход
            weapon = input(f"Выберите оружие ({'/'.join(weapons)}): ").strip().lower()
            if weapon not in weapons:
                print("Неверный выбор оружия. Попробуйте снова.")
                continue
            self.player.attack(self.computer, weapon)
            if not self.computer.is_alive():
                print(f"\n{self.computer.name} пал. {self.player.name} победил!")
                break

            # Монстр делает ход
            computer_weapon = random.choice(weapons)
            self.computer.attack(self.player, computer_weapon)
            if not self.player.is_alive():
                print(f"\n{self.player.name} пал. {self.computer.name} победил!")
                break


if __name__ == "__main__":
    game = Game()
    game.start()