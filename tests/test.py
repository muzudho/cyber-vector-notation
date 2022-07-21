"""
python -m tests.test
"""
from src.cybernum import CyberVec

cn = CyberVec.trail_zero((1, 2))
print(f"{cn.elements}")                # (1, 2, 0)

cn = CyberVec.trail_zero(3)
print(f"{cn.elements}")                # (3, 0)

cn = CyberVec((1, 2, 0))
print(f"{cn.elements}")                # (1, 2, 0)

cn = CyberVec((3, 0))
print(f"{cn.elements}")                # (3, 0)

test_data = [
    # 種をまく
    ['CyberVec.trail_zero(1)', CyberVec.trail_zero(1), 'O1o0', (1, 0)],
    # ----------------------   -----------------------  ----   ------
    # 1                        2                        3      3
    # 1. Test case title
    # 2. Actual
    # 3. Expected

    ['CyberVec.trail_zero(2)', CyberVec.trail_zero(2), 'O2o0', (2, 0)],

    # 正の整数
    ['1', CyberVec(1), 'O1', (1,)],

    # 正の整数の文字列
    ['"1"', CyberVec('1'), 'O1', (1,)],

    # 辞書順記数法
    ['"_9"', CyberVec('_9'), 'O_9', (-1,)],
    ['"A10"', CyberVec('A10'), 'OA10', (10,)],

    # 数珠玉記数法
    ['"O_9"', CyberVec('O_9'), 'O_9', (-1,)],
    ['"OA10"', CyberVec('OA10'), 'OA10', (10,)],
    ['"O_9o1oA10"', CyberVec('O_9o1oA10'), 'O_9o1oA10', (-1, 1, 10)],

    # 正の零
    ['0', CyberVec(0), 'O0', (0,)],
    # -   -----------   --   ----
    # 1   2             3    3
    # 1. Test case text
    # 2. Actual
    # 3. Expected

    # 正の整数
    ['1', CyberVec(1), 'O1', (1,)],
    ['10', CyberVec(10), 'OA10', (10,)],

    # 正の整数の文字列
    ['"0"', CyberVec('0'), 'O0', (0,)],
    ['"1"', CyberVec('1'), 'O1', (1,)],
    ['"10"', CyberVec('10'), 'OA10', (10,)],

    # O1o2 の形
    ['"O1o2o_9"', CyberVec('O1o2o_9'), 'O1o2o_9', (1, 2, -1)],
    ['"O1o2"', CyberVec('O1o2'), 'O1o2', (1, 2)],
    ['"O1o2oA10o4"', CyberVec('O1o2oA10o4'), 'O1o2oA10o4', (1, 2, 10, 4)],

    # o1o2 の形, snake_case への寛容
    ['"o1o2o_9"', CyberVec('o1o2o_9'), 'O1o2o_9', (1, 2, -1)],
    ['"o1o2"', CyberVec('o1o2'), 'O1o2', (1, 2)],
    ['"o1o2oA10o4"', CyberVec('o1o2oA10o4'), 'O1o2oA10o4', (1, 2, 10, 4)],

    # O1O2 の形
    ['"O1O2O_9"', CyberVec('O1O2O_9'), 'O1o2o_9', (1, 2, -1)],
    ['"O1O2"', CyberVec('O1O2'), 'O1o2', (1, 2)],
    ['"O1O2OA10O4"', CyberVec('O1O2OA10O4'), 'O1o2oA10o4', (1, 2, 10, 4)],

    # 混在
    ['"o_9O1oA10"', CyberVec('o_9O1oA10'), 'O_9o1oA10', (-1, 1, 10)],

    # 拡張: 辞書順記数法への寛容
    ['"A77"', CyberVec('A77'), 'OA77', (77,)],
    ['"AA777"', CyberVec('AA777'), 'OAA777', (777,)],
    ['"O7oA77oAA777oAAA7777"', CyberVec(
        'O7oA77oAA777oAAA7777'), 'O7oA77oAA777oAAA7777', (7, 77, 777, 7777)],

    ['"a77"', CyberVec('a77'), 'OA77', (77,)],
    ['"aa777"', CyberVec('aa777'), 'OAA777', (777,)],
    ['"o7oa77oaa777oaaa7777"', CyberVec(
        'O7oa77oaa777oaaa7777'), 'O7oA77oAA777oAAA7777', (7, 77, 777, 7777)],

    # タプル
    ['(1,2)', CyberVec((1, 2)), 'O1o2', (1, 2)],
    ['(1,2,-3)', CyberVec((1, 2, -3)), 'O1o2o_7', (1, 2, -3)],
    ['(1,2,10,4)', CyberVec((1, 2, 10, 4)), 'O1o2oA10o4', (1, 2, 10, 4)],
]

for datum in test_data:
    if f'{datum[1]}' == datum[2] and datum[1].elements == datum[3]:
        print(f'{datum[0]} --> "{datum[1]}" {datum[1].elements}')
    else:
        print(
            f'[Error] {datum[0]} --> "{datum[1]}" {datum[1].elements} Expected: "{datum[2]}" {datum[3]}')

# "2oo1" は使えない
try:
    print(f'[Error] "2oo1" --> {CyberVec("2oo1")}')
except:
    print(f'"2oo1" is not CyberVec')
