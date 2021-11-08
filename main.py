# 素数を判定する関数
# 素数とは? : https://benesse.jp/teikitest/chu/math/math/c00395.html#:~:text=%E6%95%B0%E5%AD%A6%E3%81%AE%E6%B1%BA%E3%81%BE%E3%82%8A%E3%81%A8%E3%81%97%E3%81%A6%EF%BC%8C1,%E3%81%AA%E8%87%AA%E7%84%B6%E6%95%B0%E3%81%8C%E7%B4%A0%E6%95%B0%E3%81%A7%E3%81%99%E3%80%82
# 約数とは? : http://kentiku-kouzou.jp/suugaku-yakusuu.html
def is_prime(n):
    # nが1の時は、素数でないため、Falseを返す。
    if n == 1:
        return False

    # 2~n-1の中に、nの約数が存在するのか検証する。
    for i in range(2, n):
        # 約数が存在する = 素数ではないのでFalseを返す。
        if n % i == 0:
            return False

    # 約数が存在しない = 素数ですのでTrueを返す。
    return True

# 1~500の数字に関して検証する。
for i in range(1, 501):
    # 1~500の数字が素数かどうか判定する。
    if is_prime(i):
        # 素数ならば、その値を出力する。
        print(i)
