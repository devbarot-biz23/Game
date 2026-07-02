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

def spawn_enemy(pos : int, type : str):
    if type == "Goblin":
        Goblin()

def main():
    lane = {1}
    input("Enter a string")
