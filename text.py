from item import Color


class Text:
    PLAYER_NAME_MAX_LENGTH = 10

    # title
    STRING_DECORATION = '＝' * 24 + '\n'
    TITLE = \
        STRING_DECORATION \
        + '\n' * 5 \
        + '　　　　　RPG created by Python\n' \
        + '\n' * 5 \
        + STRING_DECORATION \
        + 'Enterを押してゲームスタート'

    # text
    MES_INPUT_PLAYER_NAME = \
        STRING_DECORATION + '\n\nプレイヤー名を入力してください: '
    MES_PLAYER_NAME_IS_TOO_LONG = '名前が長すぎます。（10文字まで）'
    QUESTION_ANSWER = '"{}" これで良いですか？\n"yes" または "no" で応答してください [y/N]:'
    MES_SELECT_GAME_LEVEL = 'プレイするゲームレベルを入力してください。\n' \
        + '1: EASY \n' \
        + '2: NORMAL \n' \
        + '3: HARD \n'
    WELCOME = 'ようこそ '
    INPUT_YES_OR_NO = ''
    ENTER = '\n'
    MES_GAME_MISSION = STRING_DECORATION \
        + '\n\nようこそ{}さん！\n' \
        + 'ゲームクリア条件は、ゴール(G)に到達することです。\n' \
        + '\n道中恐ろしいモンスターと遭遇するかもしれません。\n' \
        + '戦うか逃げるかは、あなた次第です！\n' \
        + '\n・・・恐ろしいドラゴンが接近中と言う\n' \
        + '連絡がありましたので、\n' \
        + '早めにゴールを目指す事をお薦めします！\n' \
        + '\nそれでは、いってらっしゃい！！'

    # map
    MES_CONFIRMATION = \
        '本当に良いですか？\n' \
        + '"yes" または "no" で応答してください [y/N]'
    MES_HOW_TO_PLAY = \
        '＝＝＝＝＝＝＝＝＝　操作方法　＝＝＝＝＝＝＝＝＝\n' \
        + '[終了　　　：q ]['+Color.YELLOW+'上'+Color.END+'　　　　：w ][アイテム　：e ]\n' \
        + '['+Color.YELLOW+'左'+Color.END+'　　　　：a ]['+Color.YELLOW+'下'+Color.END+'　　　　：s ]['+Color.YELLOW+'右'+Color.END+'　　　　：d ]\n' \
        + '[ステータス：z ][決定　　　：x ][ヘルプ　　：c ]\n' \
        + '＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝'
    HOW_TO_USE_ITEM = \
        '＝＝＝＝＝＝＝＝＝　操作方法　＝＝＝＝＝＝＝＝＝\n' \
        + '[　　　　　　　][上　　　　：w ][とじる　　：x ]\n' \
        + '[　　　　　　　][下　　　　：s ][　　　　　　　]\n' \
        + '[　　　　　　　][つかう　　：x ]\n' \
        + '＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\n'
    ITEM_LIST_PREFIX = '＃＃＃＃＃＃＃＃　アイテム一覧　＃＃＃＃＃＃＃＃\n'
    ITEM_LIST_NOTING = 'アイテムがありません。'
    MES_USE_HERB = 'HPが{}回復した！'
    MES_USE_EQUIPMENT = '装備品は持っているだけで効果があります'
    ITEM_LIST_SUFFIX = '\n＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃\n'
    USE_ITEM_CONFIRM = \
        '"{}"を使用します。よろしいですか？\n' \
        + '"yes" または "no" で応答してください [y/N]'
    ICON_SELECTED = '[＊]'
    ICON_NOT_SELECTED = '[　]'
    MES_CAN_NOT_USE_KEY = '!!! 無効なキーです !!!'
    MES_CAN_NOT_MOVE = '!!! 移動できません !!!'
    MES_GET_SIELD = '勇者の盾を手に入れた！'
    MES_GET_WEAPON = '勇者の剣を手に入れた！'
    MES_GET_HERBS = '薬草を手に入れた！'
    MES_GET_ITEM = '{}を手に入れた！'

    # buttle
    MES_HOW_TO_BUTTLE = \
        '＝＝＝＝＝＝＝＝＝　操作方法　＝＝＝＝＝＝＝＝＝\n' \
        + '[終了　　　：q ][　　　　　：w ][アイテム　：e ]\n' \
        + '[こうげき　：a ][まほう　　：s ][にげる　　：d ]\n' \
        + '[ステータス：z ][ヘルプ　　：x ]\n' \
        + '＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\n'
    PLAYER_STATUS = \
        '{}\n' \
        + 'HP[{}/{}] MP[{}/{}]\n'
    PLAYER_STATUS_DETAIL = \
        'LEVEL： {}\n' \
        + '集めた経験値： {}exp\n' \
        + '次の経験値まで後：　{}exp\n' \
        + '攻撃力：　{}\n' \
        + '防御力：　{}\n'
    MONSTER_STATUS = \
        '{}\n' \
        + 'HP[{}]\n'
    MES_APPEAR_MONSTER = '{}が、あらわれた！'
    MES_CHOOSE_ACTION = '何をしますか？'
    MES_MP_IS_EMPTY = 'MPが空だった！'
    KNOCK_OUT_MONSTER = '{}を、たおした！'
    KNOCK_OUT_PLAYER = '{}は、ちからつきた...'
    MES_ATTACK_FROM_PLAYER = '{}は、こうげきした！'
    MES_ATTACK_FROM_MONSTER = '{}のこうげき！'
    MES_DAMAGE = '{}のダメージ！'
    MES_MAGIC = '{}は、まほうをとなえた！'
    MES_GET_EXP = '{}のけいけんちをかくとく！'
    MES_LEVEL_UP = 'レベルアップ！ {}はレベル{}になった！'
    MES_ESCAPE = 'にげた！'
    MES_CAN_NOT_ESCAPE = 'にげることに、しっぱいした！'

    GAME_ESCAPE = STRING_DECORATION + '\n\n ... ゲーム　終了 ... \n\n'
    GAME_OVER = STRING_DECORATION + '\n\n ... ゲーム　オーバー ... \n\n'
    GAME_CLEAR = STRING_DECORATION + '\n\n=== ゲーム　クリア === \n\n'
