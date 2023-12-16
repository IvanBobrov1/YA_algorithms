# import sys


def is_correct_bracket_seq(sequence: str) -> bool:
    stack: list[str] = []
    open_brackets: list[str] = ['(', '[', '{']
    close_brackets: list[str] = [')', ']', '}']
    if len(sequence) == 0:
        return True
    if sequence[0] in close_brackets:
        return False
    for seq in sequence:
        if seq in open_brackets:
            stack.append(open_brackets.index(seq))
        elif seq in close_brackets:
            if len(stack) != 0 and stack[-1] == close_brackets.index(seq):
                stack.pop()
            else:
                return False
    return len(stack) == 0


# if __name__ == '__main__':
#     bracket_sequence: str = sys.stdin.readline().rstrip()
#     print(is_correct_bracket_seq(bracket_sequence))

with open('bracket_seq.txt', mode='r', encoding='UTF-8') as f:
    seq = f.readline()
    print(seq)
    is_correct_bracket_seq(seq)
