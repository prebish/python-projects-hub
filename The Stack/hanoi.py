import os
from stack import Stack

class TowerOfHanoi():

    

    def __init__(self):
        self.rings = {
            0: "   |   ",
            1: "  =|=  ",
            2: " ==|== ",
            3: "===|==="
        }

        self.left_tower = Stack()
        for i in range(3, 0, -1): self.left_tower.push(self.rings[i])
        self.middle_tower = Stack()
        for _ in range(3, 0, -1): self.middle_tower.push(self.rings[0])
        self.right_tower = Stack()
        for _ in range(3, 0, -1): self.right_tower.push(self.rings[0])

        self.towers = {
            "l": self.left_tower,
            "m": self.middle_tower,
            "r": self.right_tower
        }

        

    def start(self):
        while(not self.game_won()):
            self.update()
            self.read_next_move()

    def game_won(self):
        if self.right_tower.peek(len(self.right_tower)-1) == self.rings[3]:
            return True

    
    def read_next_move(self):
        move = input()
        src = move[0]
        dst = move[-1]
        if(src not in self.towers.keys() or dst not in self.towers.keys()):
            return
        self.towers[dst].push(self.towers[src].pop())
        
        #cmd.split()
        

    def update(self):
        os.system("cls")
        self.update_towers()
        print("Options: l, m, r\nUsage ex: 'l m' or 'r l'")

    def update_towers(self):
        # self.left_tower.reverse()
        # for ring in self.left_tower:
        #     print(ring)

        # Determine the maximum height of the towers
        max_height = max(len(tower) for tower in self.towers.values())

        # Iterate from the bottom of the towers
        for level in range(max_height):
            for tower_name, tower in self.towers.items():
                # Check if the current level exists in the tower
                if level < len(tower):
                    # Access the ring from the bottom of the stack
                    ring = tower.peek(len(tower) - level - 1)
                else:
                    ring = self.rings[0]  # Empty space if no ring at this level

                print(f"{ring}\t", end="")
            print()  # Move to the next line after printing all towers at the current level

        # Print the base of the towers
        for _ in self.towers:
            print(4*"_" + "⊥" + 4*"_" + "\t", end="")
        print("\n")  # Extra newline for spacing after the bases

        # print()
        # # Top rings
        # for tower_name, tower in self.towers.items():
        #     ring = tower.peek(0) 
        #     if(ring is None or ring == self.rings[1]): ring = self.rings[0]
        #     print(" " + ring + "\t", end="")
        # print()
        # # Middle rings
        # for tower_name, tower in self.towers.items():
        #     ring = tower.peek(1) 
        #     if(ring is None): ring = self.rings[0]
        #     print(" " + ring + "\t", end="")
        # print()
        # # Bottom rings
        # for tower_name, tower in self.towers.items():
        #     ring = tower.peek(2) 
        #     if(ring is None): ring = self.rings[0]
        #     print(" " + ring + "\t", end="")
        # print()
        # # Bases
        # for tower_name, tower in self.towers.items():
        #     print(4*"_"+"⊥"+4*"_"+1*"\b"+"\t", end="")
        # print("\n")
        



        







def main():
    game = TowerOfHanoi()
    game.start()


if __name__ == "__main__":
    main()