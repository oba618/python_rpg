def main():
    elapsed_time = measure_time(calculate_something)

    # 計測時間を小数点第三位で四捨五入する
    print(f'処理時間は、{elapsed_time:.2f}秒です')


def measure_time(func):
    """処理時間を計測する関数
    """
    from time import time

    # 開始時間を保持
    start = time()

    # 何かを処理する
    func()

    # 終了時間を終了時間で引く
    elapsed_time = time() - start

    return elapsed_time


def calculate_something():
    """何かを処理する関数
    """
    print('=============== 処理開始 ===============')

    result = 0
    end_point = 100000001
    for i in range(end_point):
        result += i
    print(f'0から{end_point}未満までを足すと、{result}')

    print('=============== 処理完了 ===============')


if __name__ == '__main__':
    main()
