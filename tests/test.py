"""
python -m tests.test
"""
from src.cybernum import CyberNum

test_data = [
    # 種をまく
    ['CyberNum.seed(1)', CyberNum.seed(1), 'O1o0', (1, 0)],
    # ----------------   ----------------   ----   ------
    # 1                  2                  3      3
    # 1. Test case title
    # 2. Actual
    # 3. Expected

    ['CyberNum.seed(2)', CyberNum.seed(2), 'O2o0', (2, 0)],

    # 正の整数
    ['1', CyberNum(1), 'O1', (1,)],

    # 正の整数の文字列
    ['"1"', CyberNum('1'), 'O1', (1,)],

    # 辞書順記数法
    ['"_9"', CyberNum('_9'), 'O_9', (-1,)],
    ['"A10"', CyberNum('A10'), 'OA10', (10,)],

    # 数珠玉記数法
    ['"O_9"', CyberNum('O_9'), 'O_9', (-1,)],
    ['"OA10"', CyberNum('OA10'), 'OA10', (10,)],
    ['"O_9o1oA10"', CyberNum('O_9o1oA10'), 'O_9o1oA10', (-1, 1, 10)],
]

for datum in test_data:
    if f'{datum[1]}' == datum[2] and datum[1].elements == datum[3]:
        print(f'{datum[0]} --> "{datum[1]}" {datum[1].elements}')
    else:
        print(
            f'[Error] {datum[0]} --> "{datum[1]}" {datum[1].elements} Expected: "{datum[2]}" {datum[3]}')

# "2oo1" は使えない
try:
    print(f'[Error] "2oo1" --> {CyberNum("2oo1")}')
except:
    print(f'"2oo1" is not CyberNum')
