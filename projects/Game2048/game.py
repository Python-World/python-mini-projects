#!/usr/bin/env python3
#
# Copyright(C) 2021 wuyaoping
#

import random
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD, Font

PADDING = 5


# Block class, a rectangle in the chess board
class Block:
    # Color plate
    PLATE = {
        0: {'fg': '#c8c2b7', 'bg': '#c8c2b7'},
        2: {'fg': '#5b524b', 'bg': '#ebe3dc'},
        4: {'fg': '#574c44', 'bg': '#e7dfcb'},
        8: {'fg': '#fefef0', 'bg': '#e2b287'},
        16: {'fg': '#fdf4e1', 'bg': '#dc9b74'},
        32: {'fg': '#fefff7', 'bg': '#dc876e'},
        64: {'fg': '#fefbe8', 'bg': '#d26e50'},
        128: {'fg': '#fdf8e7', 'bg': '#e3cf88'},
        256: {'fg': '#fdfefc', 'bg': '#e2b287'},
        512: {'fg': '#feffff', 'bg': '#da9d74'},
        1024: {'fg': '#fdffff', 'bg': '#db886e'},
        2048: {'fg': '#fcfffd', 'bg': '#d36f4f'}
    }

    def __init__(self, root, width=96, height=96, ft_size=32):
        font = Font(root, weight=BOLD, size=ft_size)
        self.frame = Frame(root, background='#c8c2b7',
                           width=width, height=height)
        # Set a fixed size frame
        self.frame.propagate(False)
        self.label = Label(self.frame, background='#c8c2b7', font=font)
        self.label.pack(expand=True)

    # Change the the value which above the board
    def value(self, val):
        if val == 0:
            self.label['text'] = ''
            self.label['background'] = self.PLATE[val]['bg']
            self.frame['background'] = self.PLATE[val]['bg']
        else:
            self.label['text'] = '{}'.format(val)
            self.frame['background'] = self.PLATE[val]['bg']
            self.label['background'] = self.PLATE[val]['bg']
            self.label['foreground'] = self.PLATE[val]['fg']

    # Grid layout setting of the block frame
    def grid(self, **kwargs):
        self.frame.grid(kwargs)


class Game2048:
    def __init__(self):
        self.root = Tk()
        self.root.title('2048')
        self.root.resizable(0, 0)
        self.main_frame = Frame(self.root)

        # New a chess board
        self.board = Frame(
            self.main_frame, background='#b7afa4', padx=PADDING, pady=PADDING)
        # New a display board
        self.display = Frame(
            self.main_frame, background='#f9f8ee', padx=PADDING, pady=PADDING)

        # A label which dislpay total socre
        self.ts_label = Label(
            self.display, text='SCORE\n0', font=Font(size=28), foreground='#b9aa9e', background='#f9f8ee', justify=CENTER)
        # A label  which  display highest score
        self.hs_label = Label(
            self.display, text='BEST\n0', font=Font(size=28), foreground='#b9aa9e', background='#f9f8ee', justify=CENTER)
        # A label which display the number of the 2048
        self.num_label = Label(self.display, text='2048\n0', font=Font(
            size=28), foreground='#b9aa9e', background='#f9f8ee', justify=CENTER)
        # Align to the left
        self.ts_label.pack(side=LEFT, expand=True)
        self.hs_label.pack(side=LEFT, expand=True)
        self.num_label.pack(side=LEFT, expand=True)

        self.board.pack(side=TOP)
        self.display.pack(side=TOP, fill=BOTH, expand=True)
        self.main_frame.pack()

        self.total_score = 0
        self.highest_score = 0
        self.num_2048 = 0
        self.blocks = []
        self.data = []
        self.container = []

        # Bind the keyboard event to the `self.keyboard` method
        self.root.bind('<Key>', self.keyboard)

        self.init_board()
        self.next_state()
        self.update()

    def init_board(self, size=4):
        row = size
        column = size
        for r in range(row):
            row = []
            blocks = []
            self.container.append(0)
            for c in range(column):
                row.append(0)
                block = Block(self.board)
                block.grid(row=r, column=c, padx=PADDING, pady=PADDING)
                blocks.append(block)
            self.data.append(row)
            self.blocks.append(blocks)

    def start(self):
        self.root.mainloop()

    # Update the display
    def update(self):
        for r in range(len(self.data)):
            for c in range(len(self.data[0])):
                self.blocks[r][c].value(self.data[r][c])
        self.ts_label['text'] = 'SCORE\n{}'.format(self.total_score)
        self.hs_label['text'] = 'BEST\n{}'.format(self.highest_score)
        self.num_label['text'] = '2048\n{}'.format(self.num_2048)

    # Moving to the next state
    def next_state(self):
        available_block = []
        for r in range(len(self.data)):
            for c in range(len(self.data[0])):
                if self.data[r][c] == 0:
                    available_block.append((r, c))
        insert_pos = []
        block_num = len(available_block)
        if block_num > 1:
            a = random.randrange(0, len(available_block))
            insert_pos.append(available_block.pop(a))
            b = random.randrange(0, len(available_block))
            insert_pos.append(available_block.pop(b))
            if block_num <= 10:
                insert_pos.pop()
        else:
            insert_pos += available_block

        for pos in insert_pos:
            if random.random() < 0.75:
                self.data[pos[0]][pos[1]] = 2
                self.add_score(2)
            else:
                self.data[pos[0]][pos[1]] = 4
                self.add_score(4)

    # Keyboard reaction
    def keyboard(self, event: Event):
        moved = False
        if not self.check():
            self.update()
            # if it can't move, will ask to start a new game
            opt = messagebox.askyesno("GAME OVER", "Start a new game?")
            if opt:
                self.total_score = 0
                self.num_2048 = 0
                for r in range(len(self.data)):
                    for c in range(len(self.data[0])):
                        self.data[r][c] = 0
                self.next_state()
                self.update()
        else:
            if event.keysym == 'Up' or event.keysym.lower() == 'w':
                moved = self.up()
            elif event.keysym == 'Down' or event.keysym.lower() == 's':
                moved = self.down()
            elif event.keysym == 'Left' or event.keysym.lower() == 'a':
                moved = self.left()
            elif event.keysym == 'Right' or event.keysym.lower() == 'd':
                moved = self.right()
            else:
                return

        if moved:
            self.next_state()
            self.update()

    # Checking can move or not
    def check(self):
        for r in range(len(self.data)):
            for c in range(len(self.data[0])):
                if self.data[r][c] == 0:
                    return True

        for r in range(len(self.data)-1):
            for c in range(len(self.data[0])-1):
                if self.data[r][c] == self.data[r][c+1] \
                        or self.data[r][c] == self.data[r+1][c]:
                    return True

        c = len(self.data[0]) - 1
        for r in range(1, len(self.data)):
            if self.data[r][c] == self.data[r-1][c] \
                    or self.data[r][c] == self.data[r][c-1]:
                return True

        r = len(self.data) - 1
        for c in range(len(self.data[0])-1):
            if self.data[r][c] == self.data[r-1][c] \
                    or self.data[r][c] == self.data[r][c+1]:
                return True

        return False

    def down(self):
        moved = False
        val = [0] * len(self.data)
        for c in range(len(self.data[0])):
            for r in range(len(self.data)):
                val[r] = self.data[r][c]
            res = self.move(val[::-1])[::-1]
            for r in range(len(self.data)):
                if not moved and self.data[r][c] != res[r]:
                    moved = True
                self.data[r][c] = res[r]
        return moved

    def up(self):
        moved = False
        val = [0] * len(self.data)
        for c in range(len(self.data[0])):
            for r in range(len(self.data)):
                val[r] = self.data[r][c]
            res = self.move(val)
            for r in range(len(self.data)):
                if not moved and self.data[r][c] != res[r]:
                    moved = True
                self.data[r][c] = res[r]
        return moved

    def left(self):
        moved = False
        for r in range(len(self.data)):
            res = self.move(self.data[r])
            if not moved and self.data[r] != res:
                moved = True
            self.data[r][:] = res[:]
        return moved

    def right(self):
        moved = False
        for r in range(len(self.data)):
            res = self.move(self.data[r][::-1])[::-1]
            if not moved and self.data[r] != res:
                moved = True
            self.data[r][:] = res
        return moved

    # Move the block to aside, and fuse the same block
    def move(self, val):
        idx = 0
        for item in val:
            if item != 0:
                if idx == 0:
                    self.container[idx] = item
                    idx += 1
                else:
                    if self.container[idx-1] == item:
                        self.container[idx-1] = 2 * item
                        self.add_score(2 * item)
                        if self.container[idx-1] == 2048:
                            self.num_2048 += 1
                            self.container[idx-1] = 0
                            idx -= 1
                    else:
                        self.container[idx] = item
                        idx += 1
        while idx < len(val):
            self.container[idx] = 0
            idx += 1
        return self.container

    def add_score(self, val):
        self.total_score += val
        self.highest_score = max(self.total_score, self.highest_score)


if __name__ == '__main__':
    game = Game2048()
    game.start()
