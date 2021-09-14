import os
import sys
from random import random

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
