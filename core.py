from toolchain import *
from time import time


class TM:
    """
    @:param commands: command list
    @:param max_len: default = 100
    """
    def __init__(self, commands, max_len=100, initial_str="", verbose=False, current_state='0'):
        self.arr = ['_'] * 2*max_len
        self.current = max_len
        self.arr_len = max_len
        self.current_state = current_state
        for i in range(len(initial_str)):
            self.arr[self.current+i] = initial_str[i]
        self.verbose = verbose
        self.control = Control(commands)

    def run(self) -> Result:
        a = None
        counter = 0
        res = ""
        t1 = time()
        if self.verbose:
            while a is None:
                a = self.step()
                counter += 1
                line = ""
                for i in self.arr:
                    if i != '_':
                        line += i
                line+="\n"
                res += line
        else:
            while a is None:
                a = self.step()
                counter += 1
            line = ""
            for i in self.arr:
                if i != '_':
                    line += i
            line += "\n"
            res += line
        t2 = time()
        return Result(counter, t2-t1, res)

    @property
    def pointer(self):
        try:
            return self.arr[self.current]
        except IndexError:
            f = ['_']*self.arr_len
            s = ['_']*self.arr_len
            f.extend(self.arr)
            f.extend(s)
            self.arr = f
            self.current += self.arr_len
            self.arr_len *= 3
        return self.arr[self.current]

    def step(self):
        step = self.control.execute(self.current_state, self.pointer)
        if step != -1:
            self.current_state = step.get_state()
            self.arr[self.current] = step.get_char(self.pointer)
            self.current += step.get_move()
        else:
            return "Break!"


class Step:
    def __init__(self, new_char, move: Moves, new_state):
        self._new_char = new_char
        self._move = move
        self._new_state = new_state

    def get_char(self, prev_char):
        if self._new_char == '*':
            return prev_char
        else:
            return self._new_char

    def get_move(self):
        return self._move.value

    def get_state(self):
        return self._new_state


class Command:
    def __init__(self, initial_state):
        self._initial_state = initial_state
        self._vars = dict()

    def get_state(self):
        return self._initial_state

    def __getitem__(self, char):
        try:
            return self._vars[char]
        except KeyError:
            try:
                return self._vars['*']
            except KeyError:
                return -1

    def put_command(self, char, replace, move: Moves, state):
        self._vars[char] = Step(replace, move, state)


class Control:
    def __init__(self, commands):
        self._coms = dict()
        for line in commands.split("\n"):
            if not self.init_command(line) and line.strip():
                print("Line", line, "is invalid")

    def execute(self, state, char):
        try:
            return self._coms[state][char]
        except KeyError:
            return -1

    def init_command(self, line):
        try:
            words = line.split(" ")
            q0 = words[0]
            c0 = words[1]
            c1 = words[2]
            move = Moves.parse(words[3].lower())
            q1 = words[4]
        except Exception:
            return False

        try:
            com = self._coms[q0]
        except KeyError:
            self._coms[q0] = Command(q0)
            com = self._coms[q0]

        com.put_command(c0, c1, move, q1)
        return True
