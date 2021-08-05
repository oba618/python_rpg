import os
from random import random


def clear():
    """コンソール画面をクリアする
    """
    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clearConsole()


def is_yes(answer: str) -> bool:
    """"応答がYesであるか否か
    """
    yes_list = [
        'y', 'ye', 'yes', 'Y', 'YE', 'YES',
        'ｙ', 'いぇ', 'いぇｓ', 'Ｙ', 'ＹＥ', 'ＹＥＳ',
    ]

    return True if answer in yes_list else False 


def is_encount(counter):
    return True if int(random() * 10) % 5 == 0 or counter % 10 == 0 else False