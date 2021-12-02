"""
-y
/\
+#-------------------> +x (Forward)
|           #
|  #
|      #        #
\/
+y
(depth)
"""


def read_values():
    file = open("input.txt")
    return [line.split(" ") for line in file]


def execute_instructions(instructions, calc_aim=False):
    position = 0
    depth = 0
    aim = 0
    for instr in instructions:
        value = int(instr[1])
        if instr[0] == "forward":
            if calc_aim:
                position += value
                depth += aim * value
            else:
                position += value
        if instr[0] == "down":
            if calc_aim:
                aim += value
            else:
                depth += value
        if instr[0] == "up":
            if calc_aim:
                aim -= value
            else:
                depth -= value
    return position * depth


def main():
    instructions = read_values()
    result = execute_instructions(instructions)
    print(result)
    result_aim = execute_instructions(instructions, calc_aim=True)
    print(result_aim)


if __name__ == "__main__":
    main()
