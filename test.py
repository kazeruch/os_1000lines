ストーンチョコ
sutonchoko
オンライン

ストーンチョコ — 2024/05/18 18:10
Ja
kuta — 2024/05/25 16:27
"""
総合演習: 数独の実装

数独とは，9×9のマス目に1から9までの数字を入れるパズルである．
ただし，以下のルールを満たすように数字を配置する．
- 各行・列には1から9までの数字を1回ずつ配置する．
展開
ex7-1-1.py
12 KB
気持ちは完成してるんやけど、main関数の
sudoku, blank_map = initialize_sudoku(3)
がpackできてないってエラーで進めません
助けてください泣
ストーンチョコ — 2024/05/28 17:07
def initialize_sudoku(n: int) -> (list[list[int]], list[list[bool]]):
    """9x9の数独を初期化する

    引数nの数だけマスを空欄にした数独を生成する．生成方法はどんなものでも構わないが例えば以下のような方法が考えられる．
    1. 9x9のlist[list[int]]を全て0で初期化
    2. 数独の盤面は1~9の数字でできたグラフ構造とみなし，深さ優先探索で解を求める．以下のような手順となる
        2.1: 1~9の数字を9*9=81個並べる組み合わせを全て列挙する
        2.2: その組み合わせを数独とみなし，組み合わせをcheck_sudoku関数でチェックし，問題ない一覧を作成する
        2.3: その中からランダムに1つ選び，それを数独の盤面とする
    3. n回だけマスを空欄にする．空欄にするマスもランダムに選ぶ．
      - 9x9のマスの中で(x, y)の座標をn個ランダムに選ぶという方法が考えられる．この場合重複した座標がないように注意すること
      - 返り値は初期化した数独の盤面9x9のlist[list[int]]と，空欄にしたマスの座標を示す9x9のlist[list[bool]]の2つを返す

    Args:
        n (int): 空欄にするマスの数．0 < n < 81 とする
    Returns:
        list[list[int]]: 9x9の数独．各数字は0から9までの整数．0は空欄を表すものとする．形式はcheck_sudoku関数の説明を参照
        list[list[bool]]: どこが空欄で初期化されたかを示す9x9のlist．空欄の場合はTrue，空欄でない場合はFalseとする
    """
    sudoku = [[0 for _ in range(0,9)] for _ in range(0,9)]
    num = [range(1,10)]
    for i in range(0,9):
        for j in range(0,9):
            if sudoku[i][j] == 0:
                for k in num:
                    random.shuffle(num)
                    sudoku[i][j] = k
                    if check_sudoku(sudoku):
                        return True
                    sudoku[i][j] = 0
                return False
    return sudoku
    blank_map = [[False for _ in range(0,9)] for _ in range(0,9)]
    indices = random.sample(range(81), n)
    for idx in indices:
        row, col = idx // 9, idx % 9
        sudoku[row][col] = 0
        blank_map[row][col] = True
    
    return sudoku, blank_map


return sudoku, blank_map の前に return sudoku があって、そこで返しちゃってる感じする
ストーンチョコ — 2024/05/28 21:23
あとこの方法だと数独の生成に一生時間かかるから、数独は固定にしちゃってもいいと思う
sudoku = [[0 for _ in range(0,9)] for _ in range(0,9)]
    num = [range(1,10)]
    for i in range(0,9):
        for j in range(0,9):
            if sudoku[i][j] == 0:
                for k in num:
                    random.shuffle(num)
                    sudoku[i][j] = k
                    if check_sudoku(sudoku):
                        return True
                    sudoku[i][j] = 0
                return False
    return sudoku

この部分消して sudoku を条件満たす 9 * 9 の数独にしちゃうみたいな
kuta — 2024/05/28 21:41
すまん
まだ動作確認してない
それは問題の趣旨から離れる？
kuta — 2024/05/28 21:42
それは問題の趣旨から離れる？
ストーンチョコ — 2024/05/28 21:43
深さ優先探索を実装するのはかなり難易度高めだから固定しちゃってもいいよって先生が言ってた
kuta — 2024/05/28 21:43
そうなんや
後でやってみる
kuta — 2024/05/30 03:08
画像
らしい
ストーンチョコ — 2024/05/30 09:25
高級魚だったのか笑
kuta — 2024/05/30 10:34
画像
壊れてる！？
kuta — 2024/05/30 10:35
らしい笑笑
ストーンチョコ — 2024/05/30 10:51
sdカード焼き直しましょうｗ
kuta — 2024/05/30 10:54
焼き直してもダメだったんよ
読み込み機側がもうダメかもしれん
まだなんもしてないけどなー
ストーンチョコ — 2024/05/30 11:25
マジか
交換してもらった方がいいかもね
ストーンチョコ — 2024/05/30 11:34
カードとラズパイ本体のどっちが悪いんだろう
kuta — 2024/05/30 12:22
今度聞いてみる
kuta — 今日 00:20
総会はバイトで行けんくてすまん
ちなみに、ラズパイ
めっちゃ押し込んだら行けた
やっぱ、力が全てやったわ
ストーンチョコ — 今日 00:21
了解です
ストーンチョコ — 今日 00:21
マジか！ｗｗ
kuta — 今日 00:22
結局、接続やったんか、リーダーを変えてやり直したのが良かったのかは正直分からんけど 
ストーンチョコ — 今日 00:23
SDカードの挿しが緩かっただけなのかな
まあ結果オーライだね
kuta — 今日 00:25
なんか奥にグリグリしたら、繋がった
真相は闇
まあ繋がったら、勝ちや
ちなみにPythonの0表示される問題は未だ未解決
あれどうしたらいいんやろ、、、
while Trueの位置ちょっと変えるだけで、全部0になったり、0が少しだけ含まれたり
ChatGPTとかcopilotは新しい関数の導入を勧めてくるしなー困る
ストーンチョコ — 今日 00:39
関数作りがちだよね
今のコード送ってくれたらまた見るよ～
kuta — 今日 00:43
マジ今送ってから、風呂入るわ
これが静かに数独の中に0がいるやつ
"""
総合演習: 数独の実装

数独とは，9×9のマス目に1から9までの数字を入れるパズルである．
ただし，以下のルールを満たすように数字を配置する．
- 各行・列には1から9までの数字を1回ずつ配置する．
展開
ex7-1-1.py
12 KB
こいつは堂々と0しかいなくなるやつの一例
この位置だとダメなのはわかるけど、while Trueを他の位置に入れてもこんな結果になってしまう
"""
総合演習: 数独の実装

数独とは，9×9のマス目に1から9までの数字を入れるパズルである．
ただし，以下のルールを満たすように数字を配置する．
- 各行・列には1から9までの数字を1回ずつ配置する．
展開
untitled01.py
13 KB
ストーンチョコ — 今日 01:01
ぱっと見た感じ for k in num の中に random.shuffle(num) 入れているのがまずいような気がする
どういうアルゴリズムにしたいか少し説明してほしいかも
kuta — 今日 03:14
画像
これに近いけど、いじればいじるほど別のエラーも出てもう分からん
kuta — 今日 03:29
とりあえず、列でランダムに作って、完成したのを検算して問題なければクリア、問題があれば一から作り直しが基本的な考え(ただ、やはり生成が難しく時間がかかるため、固定したデータを行と列で交換がいいかも)
kuta — 今日 23:13
なんかいい案浮かびました？
ストーンチョコ — 今日 23:16
今さっき情報数学概論の課題終わったのでいまから考えます
やりたいことは分かった
行ごとに付け足していく感じね
ただそれだとどこかしらの行でどのパターン試してもアウトになる可能性はあるかもというリスクはありそうな気がする
でも０が入った謎の数独が出来上がっちゃうって話か
kuta — 今日 23:19
お疲れ様です
僕も今地理と古文と数学教えて帰宅中
ストーンチョコ — 今日 23:19
３科目は辛すぎ
お疲れ様です
kuta — 今日 23:20
そもそも、行で成立してるリストを並べても、列またはブロックで不成立の可能性があまりにも高いため、作るのに死ぬほど時間かかるのかも
ストーンチョコ — 今日 23:21
ブロック？
kuta — 今日 23:21
通常営業や(￣ー￣) 
3*3の塊？
ストーンチョコ — 今日 23:22
それは今回考慮しないよ
kuta — 今日 23:22
あれ？そうなん？
ストーンチョコ — 今日 23:22
記憶が正しければ
kuta — 今日 23:22
そしたら、それもチェックしてるわ
ストーンチョコ — 今日 23:23
それも実装したのか
行、列の確認より難関
kuta — 今日 23:24
確かcheck_sudokuに加えたような気がする
ストーンチョコ — 今日 23:25
for k in range(3):
       for l in range(3):
           block = []
           for m in range(3):
               for n in range(3):
                   num = sudoku[3*k+m][3*l+n]
                   if num != 0 and num in block:
                       return False
                   block.append(num)

この部分だね
今回は要らないらしい
kuta — 今日 23:26
じゃあ削除か
ただ、0の出力はそこが原因ではないよね
おそらく
ストーンチョコ — 今日 23:27
原因ではないね
おそらく
いやワンちゃん原因説あるかも
kuta — 今日 23:28
マジ？
ストーンチョコ — 今日 23:28
消して動かしてみて
kuta — 今日 23:30
ちょい待ち
ストーンチョコ — 今日 23:31
自分の勘違い説あるかも
kuta — 今日 23:33
まだこんな感じですね
画像
ストーンチョコ — 今日 23:34
原因ではないな
勘違いでした
ストーンチョコ — 今日 23:34
このアルゴリズム自体問題がありそうな気はする
kuta — 今日 23:35
あとブロックは必要なのでは？
画像
kuta — 今日 23:35
というと？
ストーンチョコ — 今日 23:35
あれ条件加えられてる、、
もうちょい考える
いや途中経過出した方が速いな
自分の方で走らせます
kuta — 今日 23:38
なんかすいません
今度なんかお菓子買ってきます
ストーンチョコ — 今日 23:40
いや何も買ってこなくて大丈夫だよ笑
﻿

"""
総合演習: 数独の実装

数独とは，9×9のマス目に1から9までの数字を入れるパズルである．
ただし，以下のルールを満たすように数字を配置する．
- 各行・列には1から9までの数字を1回ずつ配置する．
- 9x9のマスを9つの3x3のブロックに分割し，それぞれのブロックには1から9までの数字を1回ずつ配置する．

イメージ:
1 2 3 | 4 5 6 | 7 8 9
4 5 6 | 7 8 9 | 1 2 3
7 8 9 | 1 2 3 | 4 5 6
---------------------
2 3 4 | 5 6 7 | 8 9 1
5 6 7 | 8 9 1 | 2 3 4
8 9 1 | 2 3 4 | 5 6 7
---------------------
3 4 5 | 6 7 8 | 9 1 2
6 7 8 | 9 1 2 | 3 4 5
9 1 2 | 3 4 5 | 6 7 8

以下の関数をそれぞれ実装し，以下のような仕様のプログラムを作成せよ．
- 任意のマスが空欄の状態の数独をランダムに生成
- ユーザの入力をループで受け付け，元々空欄だったマスに対して数字の更新を行うことができるようにする
    - 数字の入力が数独のルールに反する場合はその旨を表示し再度入力を促すようにすること．
- マスが全て埋まったら「おめでとうございます！」と表示してプログラムは終了することとする
"""

import random
import copy


def check_sudoku(sudoku: list[list[int]]) -> bool:
    """数独が矛盾した状態になっていないかをチェックする

    - 各行・列と，9つの3x3のブロックそれぞれに1から9までの数字が2回以上現れていないかをチェックし，問題ないならTrue，そうでないならFalseを返す
    - ただし0(空欄)は2回以上現れても問題ないものとする
    - また引数のリストについて，例えば[[1, 2, 3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9, 1, 2, 3], ...]のような形式の場合，数独の盤面は
    1 2 3 | 4 5 6 | 7 8 9
    4 5 6 | 7 8 9 | 1 2 3
    ...
    となっているものとする

    Args:
        sudoku (list[list[int]]): 数独の盤面を表すリスト．要素数は9x9で，各要素は0から9までの整数．0は空欄を表す

    Returns:
        bool: 数独が正しい場合はTrue，そうでない場合はFalse
    """
    for i in range(9):
       row = []
       col = []
       for j in range(9):
           if sudoku[i][j] != 0 and sudoku[i][j] in row:
               return False
           if sudoku[j][i] != 0 and sudoku[j][i] in col:
               return False
           row.append(sudoku[i][j])
           col.append(sudoku[j][i])
   
    for k in range(3):
       for l in range(3):
           block = []
           for m in range(3):
               for n in range(3):
                   num = sudoku[3*k+m][3*l+n]
                   if num != 0 and num in block:
                       return False
                   block.append(num)
    return True
         
                


def initialize_sudoku(n: int) -> (list[list[int]], list[list[bool]]):
    """9x9の数独を初期化する

    引数nの数だけマスを空欄にした数独を生成する．生成方法はどんなものでも構わないが例えば以下のような方法が考えられる．
    1. 9x9のlist[list[int]]を全て0で初期化
    2. 数独の盤面は1~9の数字でできたグラフ構造とみなし，深さ優先探索で解を求める．以下のような手順となる
        2.1: 1~9の数字を9*9=81個並べる組み合わせを全て列挙する
        2.2: その組み合わせを数独とみなし，組み合わせをcheck_sudoku関数でチェックし，問題ない一覧を作成する
        2.3: その中からランダムに1つ選び，それを数独の盤面とする
    3. n回だけマスを空欄にする．空欄にするマスもランダムに選ぶ．
      - 9x9のマスの中で(x, y)の座標をn個ランダムに選ぶという方法が考えられる．この場合重複した座標がないように注意すること
      - 返り値は初期化した数独の盤面9x9のlist[list[int]]と，空欄にしたマスの座標を示す9x9のlist[list[bool]]の2つを返す

    Args:
        n (int): 空欄にするマスの数．0 < n < 81 とする
    Returns:
        list[list[int]]: 9x9の数独．各数字は0から9までの整数．0は空欄を表すものとする．形式はcheck_sudoku関数の説明を参照
        list[list[bool]]: どこが空欄で初期化されたかを示す9x9のlist．空欄の場合はTrue，空欄でない場合はFalseとする
    """
    sudoku = [[0 for _ in range(0,9)] for _ in range(0,9)]
    num = [i for i in range(1,10)]
    for i in range(0,9):
        for j in range(0,9):
            if sudoku[i][j] == 0:
                for k in num:
                    random.shuffle(num)                            
                    sudoku[i][j] = k
                    if check_sudoku(sudoku):
                        break
                    else:
                         sudoku[i][j] = 0
                       
        

    blank_map = [[False for _ in range(0,9)] for _ in range(0,9)]
    indices = random.sample(range(81), n)
    for idx in indices:
        row, col = idx // 9, idx % 9
        sudoku[row][col] = 0
        blank_map[row][col] = True

    return sudoku, blank_map


def print_sudoku(sudoku: list[list[int]], blank_map: list[list[bool]]) -> None:
    """数独を出力する

    数独は9x9のマス目で，各マスには0から9までの数字が入る．空欄の場合は0を出力する．
    - 初期化時に空欄だったマスには，数字の右に*を出力する
    - 3x3のブロックごとに区切り線を入れる
        - |と-を使い，数字の左右には空白を1つずつ入れること．空白が2つ並んでいても採点上は気にしないことにする
    - 一番左の数字の左側，一番右の数字の右側には空白を入れない方が良いが，採点上は気にしないことにする
    例えば
    sudoku = [[1, 0, 3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9, 1, 2, 3], 以下省略...]
    blank_map = [[False, True, False, False, False, True, False, False, False], 以下全てFalseのリストとして省略...]
    の場合，以下のようになる
    1 0* 3 | 4 5 6* | 7 8 9
    4 5 6 | 7 8 9 | 1 2 3
    7 8 9 | 1 2 3 | 4 5 6
    ---------------------
    2 3 4 | 5 6 7 | 8 9 1
    5 6 7 | 8 9 1 | 2 3 4
    8 9 1 | 2 3 4 | 5 6 7
    ---------------------
    3 4 5 | 6 7 8 | 9 1 2
    6 7 8 | 9 1 2 | 3 4 5
    9 1 2 | 3 4 5 | 6 7 8
    と出力されるものとする

    Args:
        sudoku (list[list[int]]): 数独の盤面を表すリスト．要素数は9x9で，各要素は0から9までの整数．0は空欄を表す
        blank_map (list[list[bool]]): どこが空欄で初期化されたかを示す9x9のlist．空欄の場合はTrue，空欄でない場合はFalseとする
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if blank_map[i][j]:
                print(f"{sudoku[i][j]}* ", end="")
            else:
                print(f"{sudoku[i][j]} ", end="")
        print()

def check_valid_coordinate(blank_map: list[list[bool]], x: int, y: int) -> bool:
    """ユーザからの入力が有効かどうかをチェックする

    ユーザからの入力が有効かどうかをチェックする．有効な入力とは以下の条件を満たすものとする．
    - 初期化時に空欄のマスに対してのみ入力が有効
    - x, yが0以上8以下の整数であること
    有効な入力の場合はTrue，そうでない場合はFalseを返す
    (マス目のx座標は横軸，y座標は縦軸を表し，(0, 0)が左上，(0, 8)が右上，(8, 0)が左下，(8, 8)が右下となるようにする)

    Args:
        blank_map (list[list[bool]]): どこが空欄で初期化されたかを示す9x9のlist．空欄の場合はTrue，空欄でない場合はFalseとする
        x (int): ユーザが入力したマスのx座標．0 <= x <= 8
        y (int): ユーザが入力したマスのy座標．0 <= y <= 8

    Returns:
        bool: 有効な入力の場合はTrue，そうでない場合はFalse
    """
    if 0 <= x <= 8 and 0 <= y <= 8:
       return blank_map[y][x]
    return False
   
def handle_user_update(sudoku: list[list[int]], x: int, y: int, n: int) -> (list[list[int]], bool):
    """ユーザからのマス目の更新入力を処理する

    マスに入力してみて数独のルールに反する場合はマスを更新せず，元の状態の盤面とFalseを返す
    問題ないなら更新後の盤面とTrueを返す
    (マス目のx座標は横軸，y座標は縦軸を表し，(0, 0)が左上，(8, 0)が右上，(0, 8)が左下，(8, 8)が右下となるようにする)
    ヒント: check_sudoku関数を使う
    ヒント: 二重リストの完全なクローンをする方法として new_list = copy.deepcopy(old_list) がある

    Args:
        sudoku: 数独の盤面を表すリスト．要素数は9x9で，各要素は0から9までの整数．0は空欄を表す
        x: 更新するマスのx座標．0 <= x <= 8
        y: 更新するマスのy座標．0 <= y <= 8
        n: マス更新しようとする数字．0 <= n <= 9 (つまり，ユーザは0で更新することでマスを空欄にすることができる)

    Returns:
        list[list[int]]: 更新後の数独の盤面
        bool: マスの更新が成功した場合はTrue，失敗した場合はFalse
    """
    if 0 <= n <=9:
        sudoku_before = copy.deepcopy(sudoku)
        sudoku_before[y][x] = n
        if check_sudoku(sudoku_before):
            return sudoku_before, True
        return sudoku, False
        
    


def check_win(sudoku: list[list[int]]) -> bool:
    """数独が完成しているかをチェックする

    数独が完成しているかをチェックする．完成している場合はTrue，そうでない場合はFalseを返す
    完成している条件は，すべてのマスが1から9までの数字で埋まっていることと，check_sudoku関数がTrueを返すことである

    Args:
        sudoku (list[list[int]]): 数独の盤面を表すリスト．要素数は9x9で，各要素は0から9までの整数．0は空欄を表す

    Returns:
        bool: 数独が完成している場合はTrue，そうでない場合はFalse
    """
    for p in sudoku:
         for q in p:
                if q == 0:
                    return False
    return check_sudoku(sudoku)
 

# 実験用
# 実際にmain関数で動かしてみて，動作を確認してみよう
def main():
    # 数独の初期化．3箇所空欄にするものとする
    sudoku, blank_map = initialize_sudoku(3)
    print_sudoku(sudoku, blank_map)
    # ユーザの入力を受け付ける
    while True:
        x = int(input("x座標を入力してください: "))
        y = int(input("y座標を入力してください: "))
        if not check_valid_coordinate(blank_map, x, y):
            print("そのマスには入力できません")
            continue
        n = int(input("マスに入力する数字を入力してください: "))
        if n < 0 or n > 9:
            print("数字は0から9までの整数で入力してください")
            continue
        sudoku, success = handle_user_update(sudoku, x, y, n)
        if not success:
            print("その数字は入力できません")
            continue
        print_sudoku(sudoku, blank_map)
        if check_win(sudoku):
            print("おめでとうございます！")
            break


# このファイルを直接実行した時にのみmain関数を呼び出すif文．今の所はおまじない程度に考えておいて良い
if __name__ == "__main__":
    main()
ex7-1-1.py
12 KB