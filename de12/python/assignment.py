#三択＆採点
#オープニング



print("これから神奈川県電車ゲームを始めます")
print("ルールは簡単！！他の人の答えを見ないこと！")
print("ゲームスタート！")

for i in range(1,4):
    print(i,"人目")

    ok = 0
    ng = 0
   
    score = 0

    print("横浜駅を通っている鉄道会社はいくつ？a,10 b,6 c,5")
    w = input("答えはどれだと思う？")
    if w == "b":
        print("正解")
        ok = ok + 1
        score += 1
    else:
        print("不正解")
        ng = ng + 1
        score += 0

    print("みなとみらい線の駅の数は？a,5 b,6 c,2")
    x = input("答えはどれだと思う？")
    if x == "b":
        print("正解")
        ok = ok + 1
        score += 3
    else:
        print("不正解")
        ng = ng + 1
        score += 0

    print("神奈川県にある駅は全部でいくつ？a,251 b,97 c,371")
    y =input("答えはどれだと思う？")
    if y =="c":
        print("正解")
        ok = ok + 1
        score += 9
    else:
        print("不正解")
        ng = ng + 1
        score += 0

    print("神奈川県で駅がないのはどこ？a,綾瀬市 b,中井町 c,座間市")
    z = input("答えはどれだと思う？")
    if z == "a":
        print("正解")
        ok = ok + 1
        score += 7
    else:
        print("不正解")
        ng = ng + 1
        score += 0
    
    print("終了！！正解数は", ok, "正解率は", ok/(ok+ng)*100, "％です")
    print("そして、得点は", score, "点です")




