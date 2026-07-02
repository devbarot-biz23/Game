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

    def __del__(self):
        pass

    def move(self):
        self.pos += 1
        if self.pos > 5:
            del self
            return
        print(f"{self.id} moved from {self.pos-1} to {self.pos}")

    def damage(self):
        self.health -= 1
        if self.health < 0:
            del self



class Tower:
    Counter_N = 0
    def __init__(self, position : int):
        Tower.Counter_N += 1
        self.id = "T"+str(Tower.Counter_N)
        self.pos = position
        self.range = 1
        print(f"Added { self.id } tower on lane1 at position {self.pos}")


    def place(self, index):
        self.pos = index

class Base:
    def __init__(self):
        self.health = 10

    def __del__(self):
        pass

    def damage(self):
        self.health -= 1
        if self.health < 0:
            print("GAME OVER")
            del self



def spawn_enemy(types : str):

    if types == "Goblin":
        GAME.enemy_track.append(Goblin())


def print_status():
    e_list1 = []
    e_list2 = []
    e_list3 = []
    e_list4 = []
    e_list5 = []
    t_list1 = []
    t_list2 = []
    t_list3 = []
    t_list4 = []
    t_list5 = []
    for e_obj in GAME.enemy_track:
        if e_obj.pos == 0:
            e_list1.append(e_obj.id)
        if e_obj.pos == 1:
            e_list2.append(e_obj.id)
        if e_obj.pos == 2:
            e_list3.append(e_obj.id)
        if e_obj.pos == 3:
            e_list4.append(e_obj.id)
        if e_obj.pos == 4:
            e_list5.append(e_obj.id)
    for t_obj in GAME.tower_track:
        if t_obj.pos == 0:
            t_list1.append(t_obj.id)
        if t_obj.pos == 1:
            t_list2.append(t_obj.id)
        if t_obj.pos == 2:
            t_list3.append(t_obj.id)
        if t_obj.pos == 3:
            t_list4.append(t_obj.id)
        if t_obj.pos == 4:
            t_list5.append(t_obj.id)
    print(e_list1, t_list1, "----", e_list2, t_list2, "----", e_list3, t_list3, "----", e_list4, t_list4, "----",e_list5, t_list5)

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
            print_status()
        if command.startswith("EXIT"):
            start = False
        if command.startswith("RUN_TURN"):
            GAME.turns += 1
            print(f"TURN : {GAME.turns} started")

            for t_obj in GAME.tower_track:
                for e_obj in GAME.enemy_track:
                    if e_obj.pos == t_obj.pos or e_obj.pos == t_obj.pos-1 or e_obj.pos == t_obj.pos+1:
                        e_obj.damage()
                        print(f"{t_obj.id} attacked {e_obj.pos} for 1 damage, {e_obj.id} hp={e_obj.health}")
                        break
            for e_obj in GAME.enemy_track:
                if e_obj.pos == 5:
                    BASE.damage()

            for e_obj in GAME.enemy_track:
                e_obj.move()
        else:
            pass




if __name__ == "__main__":
    main()