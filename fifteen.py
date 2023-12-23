# author: Kaushik Rajarathinam
# date: March 17, 2023
# file: fifteen.py the code behind the game
# output: the game in which user can input their options


import numpy as np
from random import choice, randint


class Fifteen:

    def __init__(self, size=4): #4 gives 15 board
        self.size = size
        self.tiles = np.array([i for i in range(1, size ** 2)] + [0])
        self.adj = {}
        for i in range(size**2):
            self.adj[i] = []
            if i-size >=0:
                self.adj[i].append(i-size)
            if i+size < size**2:
                self.adj[i].append(i+size)
            if i%size != 0:
                self.adj[i].append(i-1)
            if (i+1)%size != 0:
                self.adj[i].append(i+1)

    def update(self, move):
        index = np.where(self.tiles == 0)[0][0]
        if self.is_valid_move(move):
            for i in self.adj[index]:
                if self.tiles[i] == move:
                    self.tiles[index], self.tiles[i] = self.tiles[i], self.tiles[index]
                    return True

    def transpose(self, i, j):
        if i==j:
            return i

    def shuffle(self, steps=100):
        index = np.where(self.tiles == 0)[0][0]
        for i in range(steps):
            move_index = choice(self.adj[index])
            self.tiles[index], self.tiles[move_index] = self.tiles[move_index], self.tiles[index]
            index = move_index

    def is_valid_move(self, move):
        index = np.where(self.tiles == 0)[0][0]
        for i in self.adj[index]:
            if self.tiles[i] == move:
                return True
        return False

    def is_solved(self):
        for i in range(len(self.tiles)-1):
            if self.tiles[i] != i+1:
                return False
        return True

    def draw(self):
        print()
        print('', "+---" * self.size, '+', sep='')
        for x in range(self.size):
            for y in range(self.size):
                print("|", end='')
                if self.tiles[x * self.size + y] == 0:
                    print(f'   ', end='')
                elif self.tiles[x* self.size +y] >= self.size+6:
                    print(f'{self.tiles[x * self.size + y]} ', end='')
                else:
                    print(f'{self.tiles[x * self.size + y]:2} ', end='')
            print('|')
            print("", '+---' * self.size, '+', sep='')
        print()

    def __str__(self):
        s = ''
        for x in range(self.size):
            for y in range(self.size):
                if self.tiles[x*self.size+y] == 0:
                    s += '   '
                else:
                    s += f'{self.tiles[x*self.size+y]:2} '
            s += '\n'
        return str(s)

if __name__ == '__main__':
    game = Fifteen(4)
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
