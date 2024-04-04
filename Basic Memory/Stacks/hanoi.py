# Author: Joel W. Prebish
# Creation Date: 04/04/2024
import os
from stack import Stack
'''
Methods are already in recommended order they should be implemented.
'TODO' marks the methods you should modify. Above them are the ones you should not.
'''

game_size = 3

class TowersOfHanoi():
    #NOTE DO NOT MODIFY
    def __init__(self):

        # fill left tower
        self.left_tower = Stack()
        
        # set middle and right towers as empty stacks
        self.middle_tower = Stack()
        self.right_tower = Stack()
        # dictionary of towers for moves
        self.towers_dict = {
            "l": self.left_tower,
            "m": self.middle_tower,
            "r": self.right_tower
        }
    
    #NOTE DO NOT MODIFY
    def start(self):
        '''Starts the TowersOfHanoi game loop.'''
        while(not self.game_won()):
            self.update()
            self.read_next_move()
        print("YOU WON!")
    
    #NOTE DO NOT MODIFY
    def update(self):
        '''Updates display in game.'''
        os.system("cls")
        print("\t\tTowers of Hanoi (Simplified)\n")
        print("Options: l, m, r\nUsage: 'l m' or 'r l'\n")

        tower: Stack # defines type of 'tower'
        for tower in [self.left_tower, self.middle_tower, self.right_tower]:
            print('|\t'+str(tower)+'\t|',end="")
        print(2*"\n")
    
    #NOTE DO NOT MODIFY
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
    
    #TODO complete implementation
    def full_tower(self, tower: Stack):
        '''Fills a specified tower with all rings.'''
        #NOTE add 1, 2, 3 to tower

        return

    #TODO complete implementation
    def game_won(self) -> bool:
        '''Checks if game is won (in-loop). '''
        raise NotImplementedError("game_won not implemented.")
    
        return

    #TODO complete implementation
    def move_ring(self, src: Stack, dst: Stack):
        '''Moves a ring from src tower to dst tower.'''
        #NOTE additional logic here
        
        # check if we can move the ring and then move ring accordingly  
        if(True):
            #NOTE complete this condition, remove pass
            pass
        else: 
            print("Top of src is bigger than top of dst.")
            input("CONTINUE ...  ")
        

def main():
    game = TowersOfHanoi()
    game.start()

if __name__ == "__main__":
    main()