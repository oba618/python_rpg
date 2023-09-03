from random import randint

from src.item import Item
from src.utils.const import Mode
from src.views.text import Text
from src.utils.event import Event


class Player:

    # アクション名
    ATTACK = 'こうげき'
    MAGIC = 'まほう'
    ITEM = 'アイテム'
    ESCAPE = 'にげる'
    ACTION_LIST = [
        ATTACK,
        MAGIC,
        ITEM,
        ESCAPE,
    ]

    # 初期ステータス
    DEFAULT_INITIAL_HP = 200
    DEFAULT_INITIAL_MP = 5
    DEFAULT_INITIAL_POWER = 10
    DEFAULT_INITIAL_DEFENSE = 0
    DEFAULT_INITIAL_EXP = 0
    DEFAULT_INITIAL_LEVEL = 1
    DEFAULT_INITIAL_ITEM_LIST = []

    # レベルアップ時の値
    ADD_MAX_HP = 20
    ADD_POWER = 5
    ADD_DEFENCE = 1
    ADD_LEVEL = 1

    def __init__(self, name: str):
        self.name = name
        self.max_hp = self.DEFAULT_INITIAL_HP
        self.hp = self.DEFAULT_INITIAL_HP
        self.max_mp = self.DEFAULT_INITIAL_MP
        self.mp = self.DEFAULT_INITIAL_MP
        self.power = self.DEFAULT_INITIAL_POWER
        self.defense = self.DEFAULT_INITIAL_DEFENSE
        self.exp = self.DEFAULT_INITIAL_EXP
        self.level = self.DEFAULT_INITIAL_LEVEL
        self.item_list = self.DEFAULT_INITIAL_ITEM_LIST
        self.action_list = self.ACTION_LIST

    def get_item(self, item: str):
        """アイテム一覧にフィールドのアイテム(Itemインスタンス)を詰める

        Args:
            item (str): フィールドのアイテム
        """

        # 剣の場合
        if item == Item.WEAPON.value:
            self.power += 30

        # 盾の場合
        if item == Item.SIELD.value:
            self.defense += 10

        item = Item(item)

        # アイテムを手に入れた！
        print(Text.MES_GET_ITEM.format(item.title))
        Event.input()

        # アイテム一覧に詰める
        self.item_list.append(item)

    def output_item_list(self, select_index: int):
        """アイテム一覧を出力

        Args:
            select_index (int): 選択中インデックス
        """
        Event.output_item_list(select_index, self.item_list)

        print(Text.ITEM_LIST_PREFIX)

        # アイテム一覧表示
        if self.item_list:

            # ソート
            self.item_list.sort()

            for index, item in enumerate(self.item_list):
                if select_index == index:
                    print(Text.ICON_SELECTED + item.title)
                else:
                    print(Text.ICON_NOT_SELECTED + item.title)

        # アイテムがない場合
        else:
            Event.output_nothing_item()

        print(Text.ITEM_LIST_SUFFIX)

    def output_action_list(self, select_index: int):
        """アクションリストを出力

        Args:
            select_index (int): 選択中インデックス
        """
        print(Text.MES_CHOOSE_ACTION)

        # アクションリスト表示
        for index, action in enumerate(self.ACTION_LIST):

            # 選択中のアクションに’※’を表示
            if select_index == index:
                print(Text.ICON_SELECTED + action)
            else:
                print(Text.ICON_NOT_SELECTED + action)

    def output_status(self):
        """プレイヤーステータス表示
        """
        print(Text.PLAYER_STATUS.format(
            self.name,
            self.hp,
            self.max_hp,
            self.mp,
            self.max_mp
        ))

    def output_status_detail(self):
        """プレイヤー詳細ステータス表示
        """

        # 次レベルまでの必要経験値
        required_exp = self.level**2 - self.exp

        # 詳細ステータスを表示
        print(Text.PLAYER_STATUS_DETAIL.format(
            self.level,
            self.exp,
            required_exp,
            self.power,
            self.defense,
        ))

    def use_item(self, select_index):
        """アイテム使用
        """

        # アイテム一覧からアイテムを取り出す
        item_object = self.item_list[select_index]

        # アイテムの説明を表示、使用確認
        print(Text.USE_ITEM_CONFIRM.format(item_object.description))

        self._use_item(item_object, input(), select_index)

    def _use_item(self, item_object, answer, select_index):
        """アイテム使用

        Args:
            item_object (Item): 使用するアイテム
            answer (str): 入力された文字列
            select_index (int): 選択中インデックス
        """

        # アイテム使用
        if Event.is_yes(answer):

            # ハーブの場合、HP回復
            if item_object[:1] == Item.HERBS[:1]:
                self.hp += item_object.recovery

                # 最大値補正
                if self.hp > self.max_hp:
                    self.hp = self.max_hp

                # リストからアイテムを削除
                del self.item_list[select_index]

                print(Text.MES_USE_HERB.format(item_object.recovery))
                Event.input()

            # 使用不可
            else:
                print(Text.MES_USE_EQUIPMENT)
                Event.input()

    def action_in_buttle(self, select_index, monster) -> Mode:
        """バトルでのアクション
        """

        # こうげきの場合
        if select_index == self.action_list.index(self.ATTACK):

            # プレイヤーの攻撃
            input(Text.MES_ATTACK_FROM_PLAYER.format(self.name))
            damage = self.power + randint(0, self.level)

            # モンスターへダメージ
            input(Text.MES_DAMAGE.format(damage))
            monster.hp -= damage

        # まほうの場合
        if select_index == self.action_list.index(self.MAGIC):
            input(Text.MES_MAGIC.format(self.name))

            # MP確認
            if self.mp > 0:
                self.mp -= 1
                damage = 100 + self.level * 10

                # モンスターへダメージ
                monster.hp -= damage
                input(Text.MES_DAMAGE.format(damage))

            else:
                input(Text.MES_MP_IS_EMPTY)

        # アイテムの場合
        if select_index == self.action_list.index(self.ITEM):
            return Mode.ITEM_LIST

        # にげるの場合
        if select_index == self.action_list.index(self.ESCAPE):

            # にげる判定
            escape = randint(1, 100)
            if escape >= 30:
                input(Text.MES_ESCAPE)
                return Mode.FIELD

            # 失敗
            else:
                input(Text.MES_CAN_NOT_ESCAPE)

        # モンスターのターンへ
        monster.action_flg = True
        return Mode.BUTTLE

    def output_win_buttle(self, monster):
        """バトル勝利を出力

        Args:
            monster (Monster): モンスター
        """

        # モンスター撃破
        print(Text.KNOCK_OUT_MONSTER.format(monster.name))

        # 経験値獲得
        self.exp += monster.level
        print(Text.MES_GET_EXP.format(monster.level))
        Event.input()

        # レベルアップ判定
        if self.level**2 <= self.exp:

            # レベルアップ
            self.update_level()

            print(Text.MES_LEVEL_UP.format(self.name, self.level))
            Event.input()

    def update_level(self):
        """レベルアップ
        """
        self.max_hp += self.ADD_MAX_HP
        self.power += self.ADD_POWER
        self.defense += self.ADD_DEFENCE
        self.level += self.ADD_LEVEL
