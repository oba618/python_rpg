from src.utils.event import Event
from src.item import Item
from src.views.field import Field
from src.views.text import Text


class Map:
    """フィールドマップのクラス
    """

    def __init__(self, field_level):
        self.now_h = 1
        self.now_w = 1
        self.field_level = int('1')     # レベル分け作成予定
        self.field_number = 11
        self.map_list = self.create_map()

    def create_map(self) -> list:
        """フィールドマップを作成する

        Returns:
            list: フィールドマップ
        """

        # レベルに応じたマップを選択
        field_map = Field.FIELDS[self.field_level][self.field_number]

        # マップにプレイヤーを配置
        field_map[self.now_h][self.now_w] = Item.PLAYER.value

        return field_map

    def show(self):
        """マップを表示
        """
        Event.clear()
        print(Text.MES_HOW_TO_PLAY)

        # 二次元配列の文字列を、コマンドライン表示用に変換
        for array in self.map_list:
            map = ''
            for string in array:
                map = map + Item(string).map_item
            print(map)

    def move(self, height: int, width: int) -> str:
        """マップを移動

        Args:
            height (int): 座標高
            width (int): 座標幅
        """
        next_height = self.now_h + height
        next_width = self.now_w + width

        # 画面端の場合
        if self.is_out_of_range(next_height, next_width):
            next_field = self.scroll_map(height, width)

        else:
            next_field \
                = self.map_list[next_height][next_width]

            # マップ更新
            if not next_field == Item.BLOCK.value:
                self.change_field(height, width)

            # 壁の場合
            if next_field == Item.BLOCK.value:
                print(Text.MES_CAN_NOT_MOVE)
                Event.input()
                return

            # 空地の場合
            if next_field == Item.EMPTY.value:
                return

        # 移動先が、アイテムの場合
        return next_field

    def change_field(self, height: int, width: int):
        """現在位置を空地へ
        """

        # 元の位置を空へ
        self.map_list[self.now_h][self.now_w] = Item.EMPTY.value

        # 座標更新
        self.now_h += height
        self.now_w += width

        # 次の位置へ移動
        self.map_list[self.now_h][self.now_w] = Item.PLAYER.value

    def is_out_of_range(self, height: int, width: int) -> bool:
        """リストの範囲外か否か（リストの範囲外の場合：True）

        Args:
            height (int): 高
            width (int): 幅

        Returns:
            bool: リストの範囲外か否か
        """
        return not (
            0 <= height < len(self.map_list)
            and 0 <= width < len(self.map_list[0])
        )

    def scroll_map(self, height: int, width: int) -> tuple:

        # スクロール先
        next_field_number = self.field_number + (height * 10 + width)

        # 反転した座標を取得
        height, width = self.get_revers_point(height, width)

        # マップ作成
        next_map_list = Field.FIELDS[self.field_level][next_field_number]

        next_field = next_map_list[height][width]

        # マップ更新
        if not next_field == Item.BLOCK.value:
            self.field_number = next_field_number
            self._scroll_field(height, width, next_map_list)

        # 壁の場合
        if next_field == Item.BLOCK.value:
            print(Text.MES_CAN_NOT_MOVE)
            Event.input()
            return

        # 空地の場合
        if next_field == Item.EMPTY.value:
            return

        return next_field

    def get_revers_point(self, height: int, width: int) -> tuple:

        # 上へ
        if (self.now_h + height) < 0:
            height = len(self.map_list) - 1
            width = self.now_w + width

        # 下へ
        elif (self.now_h + height) > (len(self.map_list) - 1):
            height = 0
            width = self.now_w + width

        # 左へ
        elif (self.now_w + width) < 0:
            height = self.now_h + height
            width = len(self.map_list[0]) - 1

        # 右へ
        elif (self.now_w + width) > (len(self.map_list[0]) - 1):
            height = self.now_h + height
            width = 0

        return height, width

    def _scroll_field(
            self, height: int, width: int, next_map_list):
        """現在位置を空地へ
        """

        # 元の位置を空へ
        self.map_list[self.now_h][self.now_w] = Item.EMPTY.value

        # 座標更新
        self.now_h = height
        self.now_w = width

        self.map_list = next_map_list

        # 次の位置へ移動
        self.map_list[self.now_h][self.now_w] = Item.PLAYER.value
