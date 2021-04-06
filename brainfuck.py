import sys

alphabet = "+-<>,.[]"

def get_matching(code, index):
    if code[index] == "[":
        x = index
        opened = 0
        while True:
            x += 1
            if opened == 0 and code[x] == "]":
                break
            if code[x] == "[":
                opened += 1
            elif code[x] == "]":
                opened -= 1
        return x

    if code[index] == "]":
        x = index
        closed = 0
        while True:
            x -= 1
            if closed == 0 and code[x] == "[":
                break
            if code[x] == "]":
                closed += 1
            elif code[x] == "[":
                closed -= 1
            
        return x

            
        #[[]]



if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        code = [x for x in f.read() if x in alphabet]
    data_pointer = 0
    instruction_pointer = 0
    memory = dict()
    while instruction_pointer < len(code):
        current_instruction = code[instruction_pointer]
        if current_instruction == ">":
            data_pointer += 1
            instruction_pointer += 1
        elif current_instruction == "<":
            data_pointer -= 1
            instruction_pointer += 1
        elif current_instruction == "+":
            memory[data_pointer] = memory.get(data_pointer, 0) + 1
            instruction_pointer += 1
        elif current_instruction == "-":
            memory[data_pointer] = memory.get(data_pointer, 0) - 1
            instruction_pointer += 1
        elif current_instruction == ".":
            print(chr(memory[data_pointer]), end="")
            instruction_pointer += 1
        elif current_instruction == ",":
            memory[data_pointer] = ord(sys.stdin.read(1))   
            instruction_pointer += 1 
        elif current_instruction == "[":
            if memory.get(data_pointer, 0) == 0:
                instruction_pointer = get_matching(code, instruction_pointer) + 1
            else:
                instruction_pointer += 1       
        elif current_instruction == "]":
            instruction_pointer = get_matching(code, instruction_pointer)


