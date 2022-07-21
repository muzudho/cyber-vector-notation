from beadsvec import BeadsVec


class CyberNum:
    """Cyber Number"""

    @staticmethod
    def seed(value=0):
        try:
            # 整数かどうか判定
            int_value = int(str(value), 10)
        except ValueError:
            # TODO 整数ではなかった
            raise ValueError
        else:
            # 整数だ
            # タプルに変換、0 が入っている列を加える
            v = value, 0
            return CyberNum(v)

    @staticmethod
    def reap(value=0):
        pass

    def __init__(self, value=0, order=1):
        self._order = order
        self._beadsvec = BeadsVec(value)

        # 最後の列が 1 でなければいけない
        #element_list = self._beadsvec.elements
        #last = len(element_list) - 1
        # if element_list[last] != 1:
        #    raise ValueError(f"not cyber number: {self._beadsvec.dicordnum}")
        #
        # 1 が連続する列があってはいけない
        #pre_element = 0
        # for element in element_list:
        #    if element == 1 and pre_element == element:
        #        raise ValueError(
        #            f"not cyber number: {self._beadsvec.dicordnum}")
        #    pre_element = element

    def __str__(self):
        # 頭に "O" を付ける
        text = f"{self._beadsvec}"

        for i in range(1, self._order):
            text = f"O{text}"

        return text

    @property
    def elements(self):
        return self._beadsvec.elements
