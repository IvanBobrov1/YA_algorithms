import sys


def search_substring_in_string(string: str) -> int:
    result_str: str = ''
    length_str: int = 0
    last_index = 0
    next_index = 0
    for s in string:
        if s not in result_str:
            result_str += s
            next_index += 1
        else:
            if length_str < len(result_str):
                length_str = len(result_str)
            last_index = 0
            for item in result_str:
                if s != item:
                    last_index += 1
                else:
                    break
            result_str = result_str[last_index + 1:next_index]
            if s in result_str:
                continue
            else:
                result_str += s
    if length_str < len(result_str):
        length_str = len(result_str)
    return length_str


if __name__ == '__main__':
    long_string: str = sys.stdin.readline().rstrip()
    # long_string = 'qwertyasdfgezxcvapoi'
    # with open('str.txt', mode='r', encoding='UTF-8') as f:
    #     long_string = f.readline()
    print(search_substring_in_string(long_string))
