#Alex Chen,CSC201
#Program05

#Part1

class Treasure():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

class Gold(Treasure):
    def __init__(self, amount):
        self.amount = amount
        self.name = Gold
        self.description = "Currency used to buy goods."
        self.value = self.amount

class Food(Treasure):
    def __init__(self, name, description, value, nutrition_Val):
        self.name = Food
        self.description = "an object to eat."
        self.value = 3
        self.nutrition_Val = 30

class Weapon(Treasure):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        self.name = name
        self.description = description
        self.value = value
 
 class Sword(Weapon):
    def __init__(self):
        self.damage = 10
        self.name = Sword
        self.description = "A Steel Sword."
        self.value = 5

class Armor(Treasure):
    def __init__(self, name, description, value, defense):
        self.defense = defense
        self.name = name
        self.description = description
        self.value = value
 
class Hauberk(Armor):
    def __init__(self):
        self.defense = 20
        self.name = Hauberk
        self.description = "A Steel mail."
        self.value = 15


#Part2

class Character:
    def __init__(self, name, health, dps, gold):
        self.name = name
        self.health = health
        self.dps = dps
        self.gold = gold

class Player(Character):
  def __init__(self):
    Character.__init__(self)
    self.name = Player
    self.health = 10
    self.dps = 1
    self.gold = 0

  def is_alive(self):
        return self.health > 0

class Enemy:
    def __init__(self, name, health, dps):
        self.name = name
        self.health = health
        self.dps = dps

    def is_alive(self):
        return self.health > 0

class Goblin(Enemy):
    def __init__(self):
        self.name = Goblin
        self.health = 10
        self.dps = 2
 
class Ogre(Enemy):
    def __init__(self):
        self.name = Ogre
        self.health = 30
        self.dps = 15

#Part3

import Treasure, Character ,Enemy
 
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class StartingRoom(MapTile):
    def intro_text(self):
        return "You find yourself in a cave"
 
    def modify_player(self, Player):
        pass

Commands = {
  "h": Player.move_left,
  "j": Player.move_down,
  "k": Player.move_up,
  "l": Player.move_right,
  "^": Player.stairs_up,
  "v": Player.stairs_down,
  "i": Player.inventory,
  "E": Player.equip,
  "a": Player.wear_armor,
  "A": Player.remove_armor,
  "w": Player.wield_weapon,
  "W": Player.unwield,
  "e": Player.eat,
  "d": Player.drop,
  "p": Player.pick_up,
  "?" print(Commands)
  }
