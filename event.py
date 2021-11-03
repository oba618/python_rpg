import os
import sys
from random import random
from key import Key

from text import Text


class Event:

    YES_LIST = [
        'y', 'ye', 'yes', 'Y', 'YE', 'YES',
        'ｙ', 'いぇ', 'いぇｓ', 'Ｙ', 'ＹＥ', 'ＹＥＳ',
    ]

    @staticmethod
    def clear():
        """コンソール画面をクリアする
        """
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')

    @classmethod
    def is_yes(cls, answer: str) -> bool:
        """"応答がYesであるか否か
        """
        return True if answer in cls.YES_LIST else False

    @staticmethod
    def is_encount(counter):
        """モンスターと戦闘するか否か
        """
        return True \
            if int(random() * 10) % 9 == 0 or counter % 20 == 0 \
            else False

    @classmethod
    def confirmation(cls) -> bool:
        """確認
        """
        answer = input(Text.MES_CONFIRMATION)
        return True if answer in cls.YES_LIST else False

    @staticmethod
    def input():
        """標準入力
        """
        return sys.stdin.readline().rstrip('\n')

    @classmethod
    def input_player_key(cls) -> str:
        """標準入力の受付

        Returns:
            str: バリデーションされた文字列
        """
        while True:
            input_key = Event.input()
            for key, value in Key.KEY_LIST.items():
                if input_key in value:
                    return key

            # 不正な入力の場合
            else:
                print(Text.MES_CAN_NOT_USE_KEY)

    @staticmethod
    def check_player_key() -> str:
        """メインループでの入力チェック

        Returns:
            str: フィールドマップ
        """
        player_key = Event.input_player_key()

        if not player_key:
            return ''

        if len(player_key) >= 2:
            return ''

        return player_key

    @classmethod
    def show_title(cls):
        """タイトルを表示
        """
        cls.clear()
        print(Text.TITLE)
        cls.input()

    @classmethod
    def show_prologue(cls, player_name):
        """プロローグを表示

        Args:
            player_name (str): プレイヤー名
        """
        cls.clear()
        print(Text.MES_GAME_MISSION.format(player_name))
        cls.input()

    @classmethod
    def input_player_name(cls) -> str:
        """プレイヤーの名前を入力

        Returns:
            str: プレイヤー名
        """
        player_name = ''
        while not player_name:

            Event.clear()
            print(Text.MES_INPUT_PLAYER_NAME)
            player_name = Event.input()

            # プレイヤー名が長い場合
            if len(player_name) >= Text.PLAYER_NAME_MAX_LENGTH:
                print(Text.MES_PLAYER_NAME_IS_TOO_LONG)
                Event.input()
                player_name = ''
                continue

            # プレイヤー名が未入力の場合
            if len(player_name) == 0:
                continue

            # 決定の確認
            player_name = cls.confirm_input(player_name)

        return player_name

    @classmethod
    def select_game_level(cls) -> str:
        """ゲームレベル選択

        Returns:
            str: ゲームレベル
        """
        game_level = ''
        while not game_level:
            Event.clear()
            print(Text.MES_SELECT_GAME_LEVEL)
            game_level = cls.input()

            if game_level in ['1', '2', '3']:
                game_level = cls.confirm_input(game_level)

            else:
                game_level = ''

        return game_level

    @classmethod
    def confirm_input(cls, item: str) -> str:
        """応答がYesかNoを確認

        Args:
            item (str): 文字列

        Returns:
            str: 文字列
        """
        print(Text.QUESTION_ANSWER.format(item))
        answer = cls.input()
        if cls.is_yes(answer):
            return item
        else:
            return ''
