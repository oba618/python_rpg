from buttle import Buttle
from const import (
    FieldAction,
    ItemListAction,
    Mode,
)
from event import Event
from item import Item
import key
from key import InputKey
from map import Map
from monster import Monster
from player import Player
from random import random
from text import Text


class Process:
    """ゲーム全体の流れを管理するクラス
    """

    def __init__(self):
        self.player = None
        self.map = None
        self.game_flg = True
        self.counter = 0
        self.select_index = 0
        self.show_item_list_flg = False
        self.mode = Mode.START
        self.start()

    def mode_start(self):
        """スタートモード
        """

        # タイトルの表示
        Event.show_title()

        # プレイヤー作成
        self.player = Player(Event.input_player_name())

        # マップの作成
        self.map = Map(Event.select_game_level())

        # プロローグ
        Event.show_prologue(self.player.name)

        # フィールドモードへ
        self.mode = Mode.FIELD

    def mode_field(self):
        """モードフィールド
        """

        # マップ表示
        self.map.show()

        # キー入力に対応した処理
        self.action_in_field(key.get_input_key_obj(Event.input_player_key()))

    def action_in_field(self, key_obj: InputKey):
        """フィールドでのアクション

        Args:
            key_obj (InputKey): キーオブジェクト
        """

        # 動く
        if key_obj.field_action == FieldAction.MOVE:
            self.move_map(key_obj.move_map())

        # 画面遷移
        if key_obj.field_action == FieldAction.CHANGE:
            self.mode = key_obj.change_display()

    def mode_item_list(self):
        """アイテム一覧モード
        """
        self.select_index = 0

        while self.mode == Mode.ITEM_LIST:

            Event.clear()
            print(Text.MES_HOW_TO_PLAY)

            # アイテム一覧表示
            self.player.show_status()
            self.player.show_item_list(self.select_index)

            # アイテムなし
            if not self.player.item_list:
                self.mode = Mode.FIELD
                return

            # キー入力に応じた処理
            self.action_in_item_list(
                key.get_input_key_obj(Event.input_player_key()))

    def action_in_item_list(self, key_obj: InputKey):
        """アイテム一覧でのアクション

        Args:
            key_obj (InputKey): アクションキー
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

        # フィールドモードへ
        if key_obj.item_list_action == ItemListAction.ESCAPE:
            self.mode = Mode.FIELD

    def _show_item_list(self):
        """アイテム一覧を表示
        """

        print(Text.ITEM_LIST_PREFIX)

        # アイテム一覧を表示
        if self.player.item_list:
            self.player.show_item_list(self.select_index)

        # アイテムがない場合
        else:
            print(Text.ITEM_LIST_NOTING)
            print(Text.ITEM_LIST_SUFFIX)
            Event.input()

            # フィールドモードへ
            self.mode = Mode.FIELD

        print(Text.ITEM_LIST_SUFFIX)

    def move_map(self, point: list):
        """フィールドマップを移動する

        Args:
            point (list): 座標(0: height, 1: width)
        """

        # マップを移動
        item = self.map.move(point[0], point[1])

        # ゴール
        if item == Item.GOAL.value:
            self.mode = Mode.GAME_CLEAR
            return

        # アイテム取得
        if item:
            self.player.get_item(item)

        # エンカウント判定
        self.check_encount()

    def check_encount(self):
        """モンスターと戦闘するか否か
        """
        self.counter += 1

        # バトルモードへ
        if int(random() * 10) % 9 == 0 or self.counter % 20 == 0:
            self.mode = Mode.BUTTLE

    def mode_buttle(self):
        """バトルモード
        """

        # モンスター作成
        monster = Monster(self.counter)

        # バトルクラスへ
        buttle = Buttle(self.player, monster)

        # バトル
        self.mode = buttle.start()

    def use_item(self):
        """アイテム使用
        """

        # アイテム一覧からアイテムを取り出す
        item_object = self.player.item_list[self.select_index]

        # アイテムの説明を表示、使用確認
        print(Text.USE_ITEM_CONFIRM.format(item_object.description))

        # アイテム使用
        self.use_item(item_object, Event.input())

    def mode_status(self):
        """プレイヤーのステータス詳細を表示
        """
        Event.clear()
        print(Text.MES_HOW_TO_PLAY)

        # ステータスを表示
        self.player.show_status()
        self.player.show_status_detail()
        Event.input()

        # フィールドモードへ
        self.mode = Mode.FIELD

    def mode_help(self):
        """ヘルプモード
        """

        # ヘルプ表示
        Event.clear()
        print('show help')
        Event.input()

        # フィールドモードへ
        self.mode = Mode.FIELD

    def mode_game_escape(self):
        """エスケープモード
        """

        Event.clear()
        print(Text.STRING_DECORATION)

        # 終了
        if Event.confirmation():
            Event.clear()
            print(Text.GAME_ESCAPE)
            self.game_flg = False

        # 戻る
        else:
            self.mode = Mode.FIELD

    def mode_game_over(self):
        """ゲームオーバーモード
        """

        # ゲームオーバー
        Event.clear()
        print(Text.GAME_OVER)

        self.game_flg = False

    def mode_game_clear(self):
        """ゲームクリアモード
        """

        # ゲームクリア
        Event.clear()
        print(Text.GAME_CLEAR)
        
        self.game_flg = False

    def start(self):
        """メインループ
        """

        while self.game_flg:

            # モード定義
            define = {
                Mode.START: self.mode_start,
                Mode.FIELD: self.mode_field,
                Mode.ITEM_LIST: self.mode_item_list,
                Mode.STATUS: self.mode_status,
                Mode.HELP: self.mode_help,
                Mode.BUTTLE: self.mode_buttle,
                Mode.ESCAPE: self.mode_game_escape,
                Mode.GAME_CLEAR: self.mode_game_clear,
                Mode.GAME_OVER: self.mode_game_over,
            }

            # モード設定
            method = define.get(self.mode)

            # モード実行
            method()
