from beadsnum import BeadsNum


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
        self._beadsnum = BeadsNum(value)

        # 最後の列が 1 でなければいけない
        #columns = self._beadsnum.columns
        #last = len(columns) - 1
        # if columns[last] != 1:
        #    raise ValueError(f"not cyber number: {self._beadsnum.dicordnum}")
        #
        # 1 が連続する列があってはいけない
        #pre_column = 0
        # for column in columns:
        #    if column == 1 and pre_column == column:
        #        raise ValueError(
        #            f"not cyber number: {self._beadsnum.dicordnum}")
        #    pre_column = column

    def __str__(self):
        # 頭に "O" を付ける
        text = f"{self._beadsnum.dicordnum}"

        for i in range(1, self._order):
            text = f"O{text}"

        return text

    @property
    def columns(self):
        return self._beadsnum.columns
