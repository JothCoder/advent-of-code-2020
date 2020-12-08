import re
import aoc


class BootCode:
    def __init__(self, instructions):
        self.code = instructions
        self.ptr = 0
        self.acc = 0
        self.jmp_ptrs = []
        self.nop_ptrs = []

    def parse(input_):
        instructions = []
        jmp_ptrs = []
        nop_ptrs = []
        for (i, line) in enumerate(input_.splitlines()):
            x, y = line.split()
            instructions.append([x, int(y)])
            if x == 'jmp':
                jmp_ptrs.append(i)
            elif x == 'nop':
                nop_ptrs.append(i)
        boot_code = BootCode(instructions)
        boot_code.jmp_ptrs = jmp_ptrs
        boot_code.nop_ptrs = nop_ptrs
        return boot_code
    
    def _reset(self):
        self.acc = 0
        self.ptr = 0

    def _execute(self, instruction):
        i, n = instruction

        if i == 'acc':
            self.acc += n
            self.ptr += 1
        elif i == 'jmp':
            self.ptr += n
        elif i == 'nop':
            self.ptr += 1
        else:
            exit('error')

        return self.ptr >= len(self.code)

    def execute_till_repeat(self):
        self._reset()
        ptr_history = set()
        acc = self.acc
        while self.ptr not in ptr_history:
            ptr_history.add(self.ptr)
            self._execute(self.code[self.ptr])
            acc = self.acc
        return acc
    
    def try_execute(self):
        self._reset()
        ptr_history = set()
        while self.ptr not in ptr_history:
            ptr_history.add(self.ptr)
            if self._execute(self.code[self.ptr]):
                return True
        return False
    
    def repair_and_execute(self):
        # First try to replace `jmp` by `nop`
        for jmp_ptr in reversed(self.jmp_ptrs):
            self.code[jmp_ptr][0] = 'nop'
            if self.try_execute():
                return self.acc
            self.code[jmp_ptr][0] = 'jmp'
        # Now try replacing `nop` by `jmp`
        for nop_ptr in reversed(self.nop_ptrs):
            self.code[nop_ptr][0] = 'jmp'
            if self.try_execute():
                return self.acc
            self.code[nop_ptr][0] = 'nop'


def main():
    raw_input = aoc.get_input(8)
    boot_code = BootCode.parse(raw_input)

    print('Part 1:', part1(boot_code))
    print('Part 2:', part2(boot_code))


def part1(boot_code):
    return boot_code.execute_till_repeat()


def part2(boot_code):
    return boot_code.repair_and_execute()


main()
