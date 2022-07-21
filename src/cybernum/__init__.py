from beadsvec import BeadsVec
from dicordnum import DicOrdNum


class CyberNum:
    """Cyber Number"""

    @staticmethod
    def be_accurate(value=0):

        element_list = None

        try:
            # 整数かどうか判定
            int_value = int(str(value), 10)

        except ValueError:
            # 整数ではなかった
            #
            # タプル型なら
            if type(value) is tuple:
                # いったんリストに戻して 0 の要素を追加
                element_list = list(value)
                element_list.append(0)
                # タプルに変換して使う
                return CyberNum(tuple(element_list))
            else:
                # TODO 整数ではなかった
                raise ValueError

        else:
            # 整数だ
            # リストに変換し、0 の要素を追加
            element_list = []
            element_list.append(int_value)
            element_list.append(0)

        # タプルに変換して使う
        return CyberNum(tuple(element_list))

    def __init__(self, value=0, order=1):
        self._order = order
        self._beadsvec = BeadsVec(value)

    def __str__(self):
        """辞書順記数法"""
        text = ""
        for token in self.elements:
            # print(
            #    f"token:{token} DicOrdNum(token):{DicOrdNum(token)} text:{text}")
            text = f"{text}o{DicOrdNum(token)}"

        # 先頭だけを大文字の 'O' にする
        # print(f"text:{text}")
        text = f"O{text[1:]}"
        return text

    @property
    def elements(self):
        return self._beadsvec.elements
