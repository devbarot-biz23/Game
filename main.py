from poetry.console.commands import self

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
    def __init__(self):
        Tower.Counter_N += 1
        self.id = "T"+str(Tower.Counter_N)
        self.pos = 0
        self.range = 1

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

def spawn_enemy(type : str):

    if type == "Goblin":
        Goblin()

def main():
    start = True
    print("hello")
    while start:
        command = input()
        if command.startswith("Spawn"):
            enemy = command.split(" ")[2]
            spawn_enemy(enemy)
        if command.startswith("ADD_TOWER"):
            pos = command.split(" ")[2]
            tower = Tower()
        if command.startswith("EXIT"):
            start = False


if __name__ == "__main__":
    main()