from event import Event
from item import Item
from text import Text


class Map:
    """フィールドマップのクラス
    """

    # マップ一覧
    MAPS = [

        # level_easy
        [
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'H', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'H', 'B'],
            ['B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'H', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'H', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'H', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'H', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'E', 'S', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'E', 'E', 'E', 'E', 'H', 'B', 'W', 'E', 'E', 'E', 'E', 'B', 'E', 'H', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'G', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
        ],

        # level_normal
        [
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'H', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'H', 'B'],
            ['B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'H', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'E', 'S', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'E', 'E', 'E', 'E', 'H', 'B', 'W', 'E', 'E', 'E', 'E', 'B', 'E', 'H', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'G', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
        ],

        # level_hard
        [
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'H', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'H', 'B'],
            ['B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'H', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'B'],
            ['B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'E', 'E', 'E', 'E', 'B', 'E', 'H', 'E', 'E', 'E', 'B', 'E', 'E', 'E', 'G', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
        ],
    ]

    @property
    def counter(self):
        return self._counter

    @counter.setter
    def counter(self, value):
        self._counter = value

    @property
    def now_h(self):
        return self._now_h

    @now_h.setter
    def now_h(self, value):
        self._now_h = value

    @property
    def now_w(self):
        return self._now_w

    @now_w.setter
    def now_w(self, value):
        self._now_w = value

    @property
    def goal_flg(self):
        return self._goal_flg

    @goal_flg.setter
    def goal_flg(self, value):
        self._goal_flg = value

    @property
    def game_over_flg(self):
        return self._game_over_flg

    @game_over_flg.setter
    def game_over_flg(self, value):
        self._game_over_flg = value

    @property
    def show_item_flg(self):
        return self._show_item_flg

    @show_item_flg.setter
    def show_item_flg(self, value):
        self._show_item_flg = value

    @property
    def field(self):
        return self._field

    @field.setter
    def field(self, value):
        self._field = value

    def __init__(self, game_level):
        self._now_h = 1
        self._now_w = 1
        self._counter = 0
        self._goal_flg = False
        self._game_over_flg = False
        self._show_item_flg = False
        self._field = ''
        self._map_lists = self.create_map(game_level)

    def create_map(self, game_level: str) -> list:
        """フィールドマップを作成する

        Args:
            game_level (str): ゲームレベル

        Returns:
            list: フィールドマップ
        """

        # レベルに応じたマップを選択
        field_map = self.MAPS[int(game_level) - 1]

        # マップにプレイヤーを配置
        field_map[self._now_h][self._now_w] = Item.PLAYER.value

        return field_map

    def show(self):
        """マップを表示
        """
        Event.clear()
        print(Text.MES_HOW_TO_PLAY)

        # 二次元配列の文字列を、コマンドライン表示用に変換
        for array in self._map_lists:
            map = ''
            for string in array:
                map = map + Item(string).map_item
            print(map)

    def move(self, height: int, width: int) -> str:
        """マップを移動
        """

        # 次の移動先
        next_field = self._map_lists[self.now_h + height][self._now_w + width]

        # マップ更新
        if not next_field == Item.BLOCK.value:
            self._change_field(height, width)

        # 壁の場合
        if next_field == Item.BLOCK.value:
            print(Text.MES_CAN_NOT_MOVE)
            Event.input()
            return

        # 空地の場合
        if next_field == Item.EMPTY.value:
            return

        # ゴールの場合
        if next_field == Item.GOAL.value:
            self.goal_flg = True

        # 移動先が、アイテムの場合
        if next_field in [Item.WEAPON.value, Item.SIELD.value, Item.HERBS.value]:
            return next_field

    def _change_field(self, height, width):
        """現在位置を空地へ
        """
        self._map_lists[self.now_h][self.now_w] = Item.EMPTY.value

        self._now_h += height
        self._now_w += width

        self._map_lists[self.now_h][self.now_w] = Item.PLAYER.value
