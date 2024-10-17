from random import randint

class Character:
    def __init__(self, name, life, level) -> None:
        self.__name = name
        self.__life = life
        self.__level = level
        
    def get_name(self):
        return self.__name
        
    def get_life(self):
        return self.__life
        
    def get_level(self):
        return self.__level
    
    def view_details(self):
        return f'Name: {self.get_name()}\nLife: {self.get_life()}\nLevel: {self.get_level()}'
    
    def receive_attack(self, damage):
        self.__life -= damage
        if self.__life < 0:
            self.__life = 0

    def attack(self, target):
        damage = randint(self.get_level() * 2, self.get_level() * 4)
        target.receive_attack(damage)
        print(f'{self.get_name()} attacked {target.get_name()} and dealt {damage} damage.')
    
class Hero(Character):
    def __init__(self, name, life, level, power):
        super().__init__(name, life, level)
        self.__power = power
        self.__recharges = 2
        
    def get_power(self):
        return self.__power
    
    def view_details(self):
        return f'{super().view_details()}\nPower: {self.get_power()}\n'
    
    def get_special_attack_recharges(self):
        return self.__recharges
    
    def special_attack(self, target):
        damage = randint(self.get_level() * 5, self.get_level() * 8)
        target.receive_attack(damage)
        self.__recharges -= 1
        print(f'{self.get_name()} used the {self.get_power()} on {target.get_name()} and dealt {damage} damage!')
    
        
class Enemy(Character):
    def __init__(self, name, life, level, type):
        super().__init__(name, life, level)
        self.__type = type
        
    def get_type(self):
        return self.__type
    
    def view_details(self):
        return f'{super().view_details()}\nType: {self.get_type()}'
    
class Game:
    def __init__(self):
        self.hero = Hero(name="Ares", life=100, level=5, power="Super Strength")
        self.enemy = Enemy(name="Dragon", life=100, level=5, type="Mythical")

    def start_battle(self):
        print('Starting battle!')
        while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
            print('\nCharacter Details:')
            print(f'{self.hero.view_details()}\n')
            print(f'{self.enemy.view_details()}\n')
            input("Press enter to attack...")
            choice = input(f"Choose (1 - Normal Attack, 2 - Power [{self.hero.get_special_attack_recharges()} charges remaining] ): ")
            if choice == '1':
                self.hero.attack(self.enemy)
            elif choice == '2':
                if self.hero.get_special_attack_recharges() <= 0:
                    print('You have already used all the recharges of your special power.')
                    continue
                else:
                    self.hero.special_attack(self.enemy)
            else:
                print('Invalid choice. Choose again.')
                
            if self.enemy.get_life() > 0:
                self.enemy.attack(self.hero)
                
        if self.hero.get_level() > 0:
            print('\nCongratulations, you won the battle!')
        else:
            print('\nYou have been defeated')
            
game = Game()
game.start_battle()

                