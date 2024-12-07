import sys

sys.path.append("../../")
from lib import get_input

EVENT = 2024
DAY = 7

def part_1():
    chall_input = get_input(EVENT, DAY)
    res = 0 

    operators_list = ['+', '*']
    len_operators = len(operators_list)
    for line in chall_input.split('\n'):
        target, operands = line.split(':')
        target = int(target)
        operands = list(map(int, operands.split()))
        len_operands = len(operands)
        operators_id = 0
        found = False
        while not found and operators_id < len_operators**(len_operands - 1):
            operators = [operators_list[operators_id % len_operators**(i+1) // len_operators**i] for i in range(len_operands - 1)]
            op_res = operands[0]
            for operand, operator in zip(operands[1:], operators):
                op_res = eval(f"{op_res}{operator}{operand}")
            if target == op_res:
                found = True
                res += target
            operators_id += 1


    print(f"{res = }")
    return res

def part_2():
    chall_input = get_input(EVENT, DAY)
    res = 0 

    operators_list = ['+', '*', '']
    len_operators = len(operators_list)
    for line in chall_input.split('\n'):
        target, operands = line.split(':')
        target = int(target)
        operands = list(map(int, operands.split()))
        len_operands = len(operands)
        operators_id = 0
        found = False
        while not found and operators_id < len_operators**(len_operands - 1):
            operators = [operators_list[operators_id % len_operators**(i+1) // len_operators**i] for i in range(len_operands - 1)]
            op_res = operands[0]
            for operand, operator in zip(operands[1:], operators):
                op_res = eval(f"{op_res}{operator}{operand}")
            if target == op_res:
                found = True
                res += target
            operators_id += 1

    print(f"{res = }")
    return res 

if __name__ == "__main__":
    part_1()
    part_2()
