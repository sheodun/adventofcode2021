
class Position:

    def __init__(self):
        self.horizontal = 0
        self.depth = 0

    def command(self, string):
        cmd = string.lower()
        instruction, value = cmd.strip().split(" ")
        instruction = instruction.strip()
        value = int(value)
        
        if instruction == "forward":
            self.horizontal += int(value)

        elif instruction == "up":
            self.depth -= int(value)

        elif instruction == "down":
            self.depth += int(value)

        else:
            raise Exception("Instruction not recognised")

    def product(self):
        return self.horizontal * self.depth

