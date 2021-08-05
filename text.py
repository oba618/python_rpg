import event
from map import Map
from player import Player
from monster import Monster
from buttle import Buttle

PLAYER_MAX_HP = 200



#text
GAME_START = '=== ゲーム　スタート === \n'
INPUT_PLAYER_NAME = '名前を入力してください: '
QUESTION_ANSWER = ' これで良いですか？ \n'
WELCOME = 'ようこそ '
INPUT_YES_OR_NO = ' "yes" または "no" で応答してください [y/N]: '
ENTER = '\n'

GAME_OVER = ' ... ゲーム　オーバー ... \n'
GAME_CLEAR = '=== ゲーム　クリア === \n'

#map
MES_HOW_TO_PLAY = "=== 操作方法 [上：w][下：s][左：a][右：d][終了：q] ===\n"
MES_CAN_NOT_USE_KEY = "!!! 無効なキーです !!!"
MES_CAN_NOT_MOVE = "!!! 移動できません !!!"

# buttle
MES_HOW_TO_BUTTLE = "=== 操作方法 [こうげき：1][まほう：2][にげる：3] ==="
PLAYER_STATUS = '{}: HP[{}/{}]'
MONSTER_STATUS = '{}: HP[{}]'
MES_APPEAR_MONSTER = '{}が、あらわれた！'
KNOCK_OUT_MONSTER = '{}を、たおした！_▽'
KNOCK_OUT_PLAYER = '{}は、ちからつきた...'
MES_ATTACK = '{}は、こうげきした！'
MES_MAGIC = '{}は、まほうをとなえた！'
MES_ESCAPE = 'にげた！_▽'
WAITE_ENTER = '▽'

def start():
    """スタート
    """
    event.clear()
    print(GAME_START)

    # プレイヤーの名前を入力
    player_name = ''
    while not player_name:
        player_name = input(INPUT_PLAYER_NAME)
        player_name_answer = input(player_name + QUESTION_ANSWER + INPUT_YES_OR_NO)

        # プレイヤーの応答がYesか否か
        if event.is_yes(player_name_answer):
            break
        else:
            player_name = ''
            event.clear()

    print(WELCOME + player_name + ENTER)

    player = Player(player_name, PLAYER_MAX_HP)
    map = Map()

    while True:
        map.show()
        map.move()

        # ESCキーを押した場合
        if map.game_over_flg:
            event.clear()
            print(GAME_OVER)
            break

        # ゴール判定
        if map.goal_flg is True:
            event.clear()
            print(GAME_CLEAR)
            break

        # エンカウント判定
        if event.is_encount(map.counter):
            monster = Monster(map.counter)
            Buttle.buttle(player, monster)

        # プレイヤーのHPが0以下になった場合
        if player.hp < 0:
            event.clear()
            print(GAME_OVER)
            break

