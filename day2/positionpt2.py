
class Position:

    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def command(self, string):
        cmd = string.lower()
        instruction, value = cmd.strip().split(" ")
        instruction = instruction.strip()
        value = int(value)
        
        if instruction == "forward":
            self.horizontal += int(value)
            self.depth += self.aim * value

        elif instruction == "up":
            self.aim -= int(value)

        elif instruction == "down":
            self.aim += int(value)

        else:
            raise Exception("Instruction not recognised")

    def product(self):
        return self.horizontal * self.depth

