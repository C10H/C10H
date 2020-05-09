from typing import List
#   hill是仿射变换密码，本脚本以hill密码为例，尝试PEP484中的新语法


def hill(para1: int, para2: int) -> list:
    a_digit = list(range(0, 26))
    a_alphabet: list = []
    for i in a_digit:
        a_alphabet.append(chr(i + 65))
    # print(a_digit)
    # print(a_alphabet)
    b_digit: list = []
    for i in a_digit:
        b_digit.append((para1 * i + para2) % 26)
    b_alphabet: List[str] = []
    for i in b_digit:
        b_alphabet.append(chr(i + 65))
    # print(b_digit)
    # print(b_alphabet)
    output = [a_alphabet, b_alphabet]
    return output


# print(hill(3,11)[0][0])
# print(hill(3,11)[0][0] == 'A')
# print(hill(3,11)[1][2])
# print(hill(3,11)[1][4] == 'B')

for a in range(0, 26):
    for b in range(0, 26):
        if hill(a, b)[1][2] == 'R':
            if hill(a, b)[1][4] == 'B':
                print(a, b)
                print(hill(a, b)[0])
                print(hill(a, b)[1])
