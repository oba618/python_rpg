class Text():
    PLAYER_NAME_MAX_LENGTH = 10

    #title
    TITLE = [
        '＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃',
        '＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃',
        '',
        '   RPG created by Python',
        '',
        '＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃',
        '＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃',
        '＃＃＃　ゲームスタート　＃＃＃',
    ]

    #text
    INPUT_PLAYER_NAME = '名前を入力してください: '
    MES_PLAYER_NAME_IS_TOO_LONG = '名前が長すぎます。（10文字まで）'
    QUESTION_ANSWER = '"{}" これで良いですか？\n"yes" または "no" で応答してください [y/N]:'
    WELCOME = 'ようこそ '
    INPUT_YES_OR_NO = ''
    ENTER = '\n'

    #map
    MES_CONFIRMATION = \
        '本当に良いですか？\n' \
        + '"yes" または "no" で応答してください [y/N]'
    MES_HOW_TO_PLAY = \
        '＝＝＝＝＝＝＝＝＝　操作方法　＝＝＝＝＝＝＝＝＝\n' \
        + '[終了　　　：q ][上　　　　：w ][アイテム　：e ]\n' \
        + '[左　　　　：a ][下　　　　：s ][右　　　　：d ]\n' \
        + '[ステータス：z ][ヘルプ　　：x ]\n' \
        + '＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\n'
    MES_CAN_NOT_USE_KEY = '!!! 無効なキーです !!!'
    MES_CAN_NOT_MOVE = '!!! 移動できません !!!'
    MES_GET_SIELD = '勇者の盾を手に入れた！'
    MES_GET_WEAPON = '勇者の剣を手に入れた！'
    MES_GET_HERBS = '薬草を手に入れた！'

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

    GAME_OVER = '\n ... ゲーム　オーバー ... \n\n'
    GAME_CLEAR = '\n=== ゲーム　クリア === \n\n'



