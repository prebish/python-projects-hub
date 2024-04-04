# Author: Joel W. Prebish
# Creation Date: 04/04/2024
'''
This file contains solutions for The Stack project.
Please only take a look after you gave it your best shot.
'''
import os
from stack import Stack

game_size = 3

class TowersOfHanoi():

    def __init__(self):
        # fill left tower
        self.left_tower = Stack()
        self.full_tower(self.left_tower)
        # set middle and right towers as empty stacks
        self.middle_tower = Stack()
        self.right_tower = Stack()
        # dictionary of towers for moves
        self.towers_dict = {
            "l": self.left_tower,
            "m": self.middle_tower,
            "r": self.right_tower
        }

    def start(self):
        '''Starts the TowersOfHanoi game loop.'''
        while(not self.game_won()):
            self.update()
            self.read_next_move()
        print("YOU WON!")

    def update(self):
        '''Updates display in game.'''
        os.system("cls")
        print("\t\tTowers of Hanoi (Simplified)\n")
        print("Options: l, m, r\nUsage: 'l m' or 'r l'\n")

        tower: Stack # defines type of 'tower'
        for tower in [self.left_tower, self.middle_tower, self.right_tower]:
            print('|\t'+str(tower)+'\t|',end="")
        print(2*"\n")

    def read_next_move(self):
        '''Reads input for game (in-loop).'''
        # reads user input(), make lower and strip white spaces
        move = input("Entry: ").strip().lower()
        # assign the source tower
        if move[0] in self.towers_dict.keys(): src = self.towers_dict[move[0]]
        else: return
        # assign destination tower
        if move[-1] in self.towers_dict.keys(): dst = self.towers_dict[move[-1]]
        else: return

        self.move_ring(src, dst)
  
    def full_tower(self, tower: Stack):
        '''Fills a specified tower with all rings.'''
        for i in range(game_size, 0, -1): tower.push(i)
    
    def game_won(self):
        '''Checks if game is won (in-loop).'''
        if len(self.right_tower) == game_size:
            return True
        return False
    
    def move_ring(self, src: Stack, dst: Stack):
        '''Moves a ring from src tower to dst tower.'''
        # assign rings for the top of each corresponding stack (tower) 
        src_ring: int = src.peek()
        dst_ring: int = dst.peek()
        # check top of each stack mentioned in move
        if(src_ring is None): return
        if(dst_ring is None): dst_ring = 999
        # check and move ring accordingly
        if(dst_ring > src_ring):
            dst.push(src.pop())
        else: 
            print("Top of src is bigger than top of dst.")
            input("CONTINUE ...  ")
        

def main():
    game = TowersOfHanoi()
    game.start()

if __name__ == "__main__":
    main()