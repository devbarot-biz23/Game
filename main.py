from poetry.console.commands import self

class Goblin:
    def __init__(self):
        self.pos = 0
        self.health = 3
        self.speed = 1

    def move(self):
        self.pos += self.pos
        if self.pos > 5:
            del self

    def health(self):
        self.health -= 1
        if self.health < 0:
            del self

    def __del__(self):
        pass

class Tower:
    def __init__(self):
        self.pos = 0
        self.range = 1


class Base:
    def __init__(self):
        self.health = 10

    def damage(self):
        self.health -= 1
        if self.health < 0:
            print("GAME OVER")
            del self

    def __del__(self):
        pass

def spawn_enemy(pos : int, type : str):
    if type == "Goblin":
        Goblin()

def main():
    str = 0
    while(str):
        input("Enter a string")
