import sys

from src.controllers.inputKey import InputKey
from src.controllers.inputKeyServer import InputKeyServer
from src.models.monster import Monster
from src.models.player import Player
from src.utils.const import (
    ButtleAction,
    ItemListAction,
    Mode,
)
from src.utils.event import Event
from src.views.text import Text


class Buttle:
    """バトル画面に遷移するイメージのクラス

    Args:
        player (Player): プレイヤー
        monster (Monster): モンスター
    """

    def __init__(self, player: Player, monster: Monster):
        self.player = player
        self.monster = monster
        self.appear_flg = True
        self.monster_action_flg = False
        self.select_index = 0
        self.mode = Mode.BUTTLE
        self.buttle_flg = True

    def mode_buttle(self):
        """バトルモード
        """

        while self.mode == Mode.BUTTLE:

            # 画面表示
            self.show_display()

            if self.monster.appear_flg:
                self.monster.appear_flg = False
                continue

            # アクションリスト表示
            self.player.output_action_list(self.select_index)

            # キー入力に対応したアクション
            self.action_in_buttle(
                InputKeyServer.get_input_key_obj(Event.input_character()))

            # モンスター死亡判定
            if self.is_dead(self.monster):

                # プレイヤー勝利
                self.player.output_win_buttle(self.monster)

                # フィールドモードへ
                self.mode = Mode.FIELD
                self.buttle_flg = False
                return

            # モンスターの攻撃
            if self.monster.action_flg:
                self.monster.attack(self.player)

            # プレイヤー死亡判定
            if self.is_dead(self.player):

                # ゲームオーバーモードへ
                self.mode = Mode.GAME_OVER
                self.buttle_flg = False
                return

    def action_in_buttle(self, key_obj: InputKey):
        """バトルモードでのアクション

        Args:
            key_obj (InputKey): キーオブジェクト
        """

        # カーソル動く
        if key_obj.buttle_action == ButtleAction.MOVE:
            self.select_index = key_obj.move_cursor(
                len(self.player.action_list),
                self.select_index,
            )

        # 決定
        if key_obj.buttle_action == ButtleAction.DECISION:
            self.mode = self.player.action_in_buttle(
                self.select_index,
                self.monster,
            )

        # 画面遷移
        if key_obj.buttle_action == ButtleAction.CHANGE:
            self.mode = key_obj.change_display()

    def is_dead(self, target) -> bool:
        """死亡判定

        Args:
            target (Player or Monster): ターゲット

        Returns:
            bool: 死亡判定
        """
        return target.hp <= 0

    def show_display(self):
        """ディスプレイ表示
        """

        # 上部表示
        Event.clear()
        self.show_display_top()

        # モンスター登場
        if self.monster.appear_flg:
            self.monster.appear()

    def show_display_top(self):
        """ディスプレイ上部表示
        """

        # 遊び方
        print(Text.MES_HOW_TO_PLAY)

        # プレイヤーステータス
        print(Text.PLAYER_STATUS.format(
            self.player.name,
            self.player.hp,
            self.player.max_hp,
            self.player.mp,
            self.player.max_mp
        ))

        # モンスターステータス
        print(Text.MONSTER_STATUS.format(
            self.monster.name,
            self.monster.hp,
        ))

    def show_items(self, item_list: list):
        """アイテム表示

        Args:
            item_list (list): アイテム一覧
        """

        print(Text.ITEM_LIST_PREFIX)

        # アイテムがある場合
        if item_list:
            for index, item in enumerate(item_list):

                # 選択中のアイテムの場合は'[※]'を表示する
                if index == self.select_index:
                    print(Text.ICON_SELECTED + item.title)
                else:
                    print(Text.ICON_NOT_SELECTED + item.title)

        # アイテムがない場合
        else:
            print(Text.ITEM_LIST_NOTING)
            print(Text.ITEM_LIST_SUFFIX)
            Event.input()
            return

        print(Text.ITEM_LIST_SUFFIX)

    def mode_item_list(self):
        """アイテム一覧を表示するループ
        """

        # インデックス初期化
        self.select_index = 0

        while self.mode == Mode.ITEM_LIST:

            Event.clear()
            print(Text.MES_HOW_TO_PLAY)

            # アイテム一覧表示
            self.player.output_status()
            self.player.output_item_list(self.select_index)

            # アイテムなしの場合
            if not self.player.item_list:
                self.mode = Mode.BUTTLE
                return

            # キー入力に応じた処理
            self.action_in_item_list(
                InputKeyServer.get_input_key_obj(Event.input_character()))

    def action_in_item_list(self, key_obj: InputKey):
        """アイテム一覧でのアクション

        Args:
            key_obj (InputKey): キーオブジェクト
        """

        # カーソル移動
        if key_obj.item_list_action == ItemListAction.MOVE:
            self.select_index = key_obj.move_cursor(
                len(self.player.item_list),
                self.select_index,
            )

        # アイテム使用
        if key_obj.item_list_action == ItemListAction.DECISION:
            self.player.use_item(self.select_index)
            self.select_index = 0

        # バトルに戻る
        if key_obj.item_list_action == ItemListAction.ESCAPE:
            self.mode = Mode.BUTTLE
            self.select_index = 0

    def mode_status(self):
        """プレイヤーのステータス詳細を表示
        """

        Event.clear()
        print(Text.MES_HOW_TO_PLAY)

        # 概要ステータスを表示
        self.player.output_status()
        self.player.output_status_detail()
        Event.input()

        # バトルに戻る
        self.mode = Mode.BUTTLE

    def mode_help(self):
        """ヘルプモード
        """

        # ヘルプ表示
        Event.clear()
        print('show help')
        Event.input()

        self.mode = Mode.BUTTLE

    def mode_game_escape(self):
        """エスケープモード
        """

        self.show_display()
        print(Text.STRING_DECORATION)

        # 確認
        if Event.confirm():

            # ゲーム終了
            Event.clear()
            print(Text.GAME_ESCAPE)
            sys.exit()

        else:
            self.mode = Mode.BUTTLE

    def mode_field(self):
        """フィールドモードへ
        """
        self.buttle_flg = False

    def start(self) -> Mode:
        """バトルスタート

        Returns:
            Mode: モード
        """

        while self.buttle_flg:

            # モード定義
            define = {
                Mode.FIELD: self.mode_field,
                Mode.BUTTLE: self.mode_buttle,
                Mode.ITEM_LIST: self.mode_item_list,
                Mode.ESCAPE: self.mode_game_escape,
                Mode.STATUS: self.mode_status,
                Mode.HELP: self.mode_help,
            }

            # モード選択
            method = define.get(self.mode)

            # モード実行
            method()

        return self.mode
