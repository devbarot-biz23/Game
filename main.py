from poetry.console.commands import self


class Game:
    def __init__(self):
        self.enemy_track = []
        self.tower_track = []
        self.status = "RUNNING"
        self.turns = 0
        
class Goblin:
    Counter_N = 0
    def __init__(self):
        Goblin.Counter_N += 1
        self.id = "E"+str(Goblin.Counter_N)
        self.pos = 0
        self.health = 3
        self.speed = 1
        print(f"Spawned { self.id } goblin on lane1 at position {self.pos}")


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
    Counter_N = 0
    def __init__(self, position : int):
        Tower.Counter_N += 1
        self.id = "T"+str(Tower.Counter_N)
        self.pos = position
        self.range = 1
        print(f"Spawned { self.id } tower on lane1 at position {self.pos}")


    def place(self, index):
        self.pos = index

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

def spawn_enemy(types : str):

    if types == "Goblin":
        GAME.enemy_track.append(Goblin())



GAME = Game()
BASE = Base()
def main():
    start = True
    while start:
        command = input()
        if command.startswith("Spawn"):
            enemy = command.split(" ")[2]
            spawn_enemy(enemy)
        if command.startswith("ADD_TOWER"):
            pos = command.split(" ")[2]
            Tower(int(pos))
        if command.startswith("STATUS"):
            print(f"Status : {GAME.status}")
            print(f"Turn : {GAME.turns}")
            print(f"Base Health: {BASE.health}")
            count_space = len(GAME.enemy_track) + len(GAME.tower_track)
            print("lane1")
            print(" 0 " + " " * count_space + " 1 " + " " * count_space + " 2 "+ " " * count_space + " 3 "+ " " * count_space + " 4 "+ " " * count_space + " BASE ")
        if command.startswith("EXIT"):
            start = False




if __name__ == "__main__":
    main()