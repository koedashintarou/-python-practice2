﻿#入力を得てインチをセンチメートルに変換
#変換のもとになる値
per_inch = 2.54
#ユーザーから入力を得る
user =input("何インチですか？")
#浮動小数点型に変換
inch = float(user)
#計算
cm = inch * per_inch
#結果を表示
desc = "{0}inch = {1}センチ",format(inch, cm)
print(desc)