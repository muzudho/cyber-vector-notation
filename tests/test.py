"""
python -m tests.test
"""
from src.cybernum import CyberNum

test_data = [
    # 数値
    ['1', CyberNum(1)],

    # 文字列
    ['"1"', CyberNum('1')],

    # 辞書順記数法
    ['"A1"', CyberNum('A1')],

    # 数珠玉記数法
    ['"32o1"', CyberNum('32o1')],
    ['"654o32o1"', CyberNum('654o32o1')],
    ['"9987o654o32o1"', CyberNum('9987o654o32o1')],

    # 辞書順記数法, 数珠玉記数法
    ['"A77o1"', CyberNum('A77o1')],
    ['"A77oAA777o1"', CyberNum('A77oAA777o1')],
    ['"A77oAA777oAAA7777o1"', CyberNum('A77oAA777oAAA7777o1')],
]

for datum in test_data:
    print(f"{datum[0]} --> {datum[1]} {datum[1].columns}")

# 2 は使えない数だ
try:
    print(f"[Error] 2 --> {CyberNum(2)}")
except:
    print(f"2 is not CyberNum")

# "1o2" は使えない
try:
    print(f'[Error] "1o2" --> {CyberNum("1o2")}')
except:
    print(f'"1o2" is not CyberNum')

# "1o1" は使えない
try:
    print(f'[Error] "1o1" --> {CyberNum("1o1")}')
except:
    print(f'"1o1" is not CyberNum')

# "2oo1" は使えない
try:
    print(f'[Error] "2oo1" --> {CyberNum("2oo1")}')
except:
    print(f'"2oo1" is not CyberNum')
