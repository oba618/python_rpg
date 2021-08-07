from buttle import Buttle
from event import Event
from map import Map
from monster import Monster
from player import Player
from text import Text


class Process():
    def start(self):
        """スタート
        """
        # タイトル画面
        Event.clear()
        for string in Text.TITLE:
            print(string)
        input()

        # プレイヤーの名前を入力
        player_name = ''
        while not player_name:
            Event.clear()

            player_name = input(Text.INPUT_PLAYER_NAME)

            # プレイヤー名が長い場合
            if len(player_name) >= Text.PLAYER_NAME_MAX_LENGTH:
                input(Text.MES_PLAYER_NAME_IS_TOO_LONG)
                player_name = ''
                continue

            # プレイヤー名が未入力の場合
            if len(player_name) == 0:
                continue

            # プレイヤーの応答がYesか否か
            player_name_answer = \
                input(Text.QUESTION_ANSWER.format(player_name))
            if Event.is_yes(player_name_answer):
                break
            else:
                player_name = ''
                Event.clear()
                continue

        # プレイヤー作成
        player = Player(player_name)

        # マップ作成
        map = Map()

        # マップ移動
        while True:
            map.show()
            map.move()

            # ESCキーを押した場合
            if map.game_over_flg:
                if Event.confirmation():
                    Event.clear()
                    print(Text.GAME_OVER)
                    break
                else:
                    continue

            # アイテム一覧
            if map.show_item_flg:
                player.show_item_list()
                map.show_item_flg = False
                continue

            # ゴール判定
            if map.goal_flg is True:
                Event.clear()
                print(Text.GAME_CLEAR)
                break

            # アイテム獲得
            if map.field:
                player.get_item(map.field)

            # エンカウント判定
            if Event.is_encount(map.counter):
                monster = Monster(map.counter)
                Buttle().buttle(player, monster)

            # プレイヤーのHPが0以下になった場合
            if player.hp < 0:
                Event.clear()
                print(Text.GAME_OVER)
                break
