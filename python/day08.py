import aoc


class BootCode:
    def __init__(self, instructions):
        self.code = instructions
        self.ptr = 0
        self.acc = 0
        self.jmp_ptrs = []
        self.nop_ptrs = []

        for (i, (opcode, _)) in enumerate(self.code):
            if opcode == 'jmp':
                self.jmp_ptrs.append(i)
            elif opcode == 'nop':
                self.nop_ptrs.append(i)

    @staticmethod
    def parse(input_):
        instructions = []
        for line in input_.splitlines():
            opcode, data = line.split()
            instructions.append([opcode, int(data)])
        return BootCode(instructions)

    def execute_till_repeat(self):
        self._reset()
        ptr_history = set()
        acc = self.acc
        while self.ptr not in ptr_history:
            ptr_history.add(self.ptr)
            self._exec_instruction()
            acc = self.acc
        return acc
    
    def repair_and_execute(self):
        if (self._try_opcode_replace_and_exec(reversed(self.jmp_ptrs), 'nop')
                or self._try_opcode_replace_and_exec(reversed(self.nop_ptrs), 'jmp')):
            return self.acc
        return None
    
    def _try_opcode_replace_and_exec(self, ptrs, opcode_replacement):
        """
            Try to to execute properly (i.e. not infinitly) by replacing the
            opcode of one pointer from `ptrs` to the given `opcode_replacement`.
        """
        for ptr in ptrs:
            old_opcode = self.code[ptr][0]
            self.code[ptr][0] = opcode_replacement
            if self._try_exec():
                return True
            self.code[ptr][0] = old_opcode
        return False
    
    def _try_exec(self):
        self._reset()
        ptr_history = set()
        while self.ptr not in ptr_history:
            ptr_history.add(self.ptr)
            if self._exec_instruction():
                return True
        return False
    
    def _reset(self):
        self.acc = 0
        self.ptr = 0

    def _exec_instruction(self):
        opcode, data = self.code[self.ptr]

        if opcode == 'acc':
            self.acc += data
            self.ptr += 1
        elif opcode == 'jmp':
            self.ptr += data
        elif opcode == 'nop':
            self.ptr += 1

        return self.ptr >= len(self.code)


def main():
    raw_input = aoc.get_input(8)
    boot_code = BootCode.parse(raw_input)

    print('Part 1:', boot_code.execute_till_repeat())
    print('Part 2:', boot_code.repair_and_execute())


main()
