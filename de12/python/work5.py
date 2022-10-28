for i in range(1,3): #1以上3未満
    print(i,"人目")  #繰り返したいことはすべてタブでくくる！！

#　出力結果
# 1 人目
# 2 人目
    name=input("名前を教えてください")
    waist=float(input("腹囲は?")) #floatは少数点以下も含む、intは整数のみ
    weight=float(input("体重は？"))
    age=int(input("年齢は？"))

    print(name, "さんは腹囲", waist, "cmで、体重は", weight, "kgで年齢は",age, "才ですね。")


    if waist>=85 and age>=40:
        print(name,"さん、内臓脂肪蓄積注意です")
    else:
        print(name,"さん、腹囲は問題ありません")