'''
1-Dimension Cellular Automata using Pyxel Game Engine

This algorithm is based in the Chapter 7 of the book
The Nature of Code
https://natureofcode.com/book/chapter-7-cellular-automata/

- Carmelo Milano
https://github.com/milanocr
'''

import pyxel

class CellularAutomata1D:

    def __init__(self, width: int):
        self.width = width
        self.default()

    def default(self, with_new_rule: bool = False):
        self.cells = [0 for x in range(self.width)] # reset the list
        self.ruleset = self.ruleset if with_new_rule else [0, 1, 1, 1, 0, 1, 1, 0]# rule 110
        self.cells[int(self.width/2)] = 1
        self.generation = 0

    def rules(self, a: int, b: int, c: int):
        index = int(f"{a}{b}{c}",2)
        return self.ruleset[index]

    def new_ruleset(self, rules: list = []):

        self.ruleset = rules if rules != [] else [pyxel.rndi(0,1) for x in range(8)]

    def generate(self):
        nextgen = [0 for x in range(self.width)]
        for i in range(0, len(self.cells), 1 ):
            # The left neighbor of the first cell is the last
            left_index = len(self.cells) - 1 if i == 0 else i-1

            # The right neighbor of the last cell is the first
            next = i+1
            right_index = 0 if next == len(self.cells) else next

            left = self.cells[left_index]
            middle = self.cells[i]
            right = self.cells[right_index]
            nextgen[i] = self.rules(left, middle, right)

        self.cells = nextgen
        self.generation += 1
        if self.generation == self.width:
            self.generation = 0
    
    def draw_ruleset(self):
        rule = int("".join(str(x) for x in reversed(self.ruleset)),2)
        pyxel.rect(0, 0, 13, 7, 7)
        pyxel.text(1, 1, str(rule), 0)
    
    def draw(self):
        for i in range(len(self.cells)):
            if (self.cells[i] == 1):
                pyxel.pset(i,self.generation,2)
            else:
                pyxel.pset(i,self.generation,7)
        self.draw_ruleset()
        self.generate()


class App:
    def __init__(self):
        pyxel.init(64, 64)
        global cells
        cells = CellularAutomata1D(width=64)

        pyxel.run(self.update, self.draw)

    def update(self):
        if (pyxel.btnr(pyxel.KEY_SPACE) or pyxel.btnr(pyxel.GAMEPAD1_BUTTON_A)):
            pyxel.cls(0)
            cells.new_ruleset()
            cells.default(with_new_rule=True)
        elif (pyxel.btnr(pyxel.KEY_N) or pyxel.btnr(pyxel.GAMEPAD1_BUTTON_B)):
            pyxel.cls(0)
            cells.default()

            

    def draw(self):
        time = pyxel.frame_count % 1 #Drawing speed of new generations.
        if time == 0:
            cells.draw()

App()
