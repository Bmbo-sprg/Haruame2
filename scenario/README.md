# 「ハルジオンは雨と咲く」シナリオ要件定義

## ファイル構造とファイル名について

1 から 4 までの「部」に加えて、各部の中に「節」を適当な長さで設けてください。
各節ごとにファイルを作成してください。僕のほうでファイルの順番が分かるようなファイル名であればよいです。

拡張子は **.txt** でお願いします。Word で書いてメモ帳に貼り付けて保存、とかでも良いです（しかしそうした場合、勝手にインデントがついちゃうこともあるので気を付けましょう）

## 記述について

テキストは **切り替えごとに** 1 行空きで書いてください。例えば、

```
-結夏「これは一行目
これは二行目」

-結夏「でもこれは次クリックの一行目」

僕はすべてを理解した。
1 行空きで書いた場合と、
行を空けずに書いた場合との違いを。
```

と記述すると、結夏は

```
「これは一行目
これは二行目」
```

と話してから、

```
「でもこれは次クリックの一行目」
```

と話し、そこから地の文で、

```
僕はすべてを理解した。
1 行空きで書いた場合と、
行を空けずに書いた場合との違いを。
```

と続きます。
以下では行を空けずに書いた「改行を含まない 1 つ以上の文」たちの塊のことを
`論理行` と呼びます。

論理行には以下の種類があります。

### 1. 地の文

最初を文字列 `-` で始めなかったらなんでもいいです。目安 100 字以内ですが、
文字を小さくするなどの表現もできるのでそういう意味ではもっと詰められます。

会話文でも使えますが、一つの論理行の中で複数回クリックしたい時は、
`{w}` と挟んでください。例えば、

```
私は戸惑った。{w}一体どういうことだ。
```

と書けば、ワンクリックで「私は戸惑った。」とだけ表示され、
その後もう 1 クリックで「一体どういうことだ」がその後に表示されます。

その他にも色んな表示のさせ方（表示速度を変える、太字、下線、
一瞬で表示、一瞬で多くの論理行を表示 (DDLCにあるような演出まで出来ます) etc.）があります。
が、それらはこっちでやろうと思いますので、それらの表示に関して強い要望があれば、
「3. 注釈文」を使ってその旨書いておいてください。

また、プレイヤーが入力した文字に応じて内容を表示させたい・ランダムな文を表示させたい、
などの要望も可能です。「3. 注釈文」で書いてください。
要望が無くても僕がやるかもしれません。

### 2. 会話文

最初を文字列 `-` で始め、次に話者の名前（の略称）を続け、発話を鍵括弧
`「` `」` で囲んでください。鍵括弧は 1 論理行ごとに 1 つだけあります。
（文中の引用などは二重鍵括弧などを使ってください）

鍵括弧閉じ `」` の後には文字列を続けないでください。

話者には略称を付けることが可能です。ファイル内では統一してほしいです。
例えば、

```
# y: 結夏, s: 皐月

-y「あいうえお」

-s「かきくけこ」
```

と書くことは可能です。別に `結夏` とフルで書いても良いです。
ある発話が複数の論理行に分かれる場合、各論理行内でちゃんと鍵括弧を閉じてください。
例えば、

```
# OK 例

-y「あいうえお
かきくけこ」

# NG 例

-y「あいうえお

かきくけこ」

# 上の NG 例を OK にした例
# このように、発話を分割してください。

-y「あいうえお」

-y「かきくけこ」
```

### 3. 注釈文

既に上でも使っていますが、注釈文は文字列 `#` で始めます。
注釈文は、背景・立ち絵の表示に関する要望や、
ファイルの冒頭にこれがどのシーンかを表す説明など、幅広く使えます。
UI に関する要望でもいいです。極力実現させます。
ここは行頭が `#` であればなんでもいいので自分なりに使いやすい
文法にしてってください。用例：

```
# 第2部　過去
# 12月23日

# 背景：街

-y「クリスマスパーティーに行きますわ」

クリスマスパーティーに行く。

# 背景：クリパ

# a: 綾乃
# ここの席順どうしよっかな...

-a「ようこそ」
```

実際注釈文を `scene street` や `show ayano happy at left`
などのスクリプトに変換するのはシステム側でやっていきます
（たぶんそんなに作業量多くないと予想したため）。
もしかしたらその変換も手伝ってもらうかもしれません。
とりあえず今は、注釈文のスクリプトとしての文法を気にせずに、
日本語で心地良いままにシナリオを書いてください。

## 実例：最初のシーン

```
# 第1部　ハルジオンイベント
# 背景：ハルジオン咲いてる

# y: 結夏　s: 皐月

y「あ、ハルジオンだ」

緑道を並んで歩いていた彼女が、脇道を指さした。

s「へぇ。この花、ハルジオンって言うんだ。
知らなかった」

中心の黄色いボタンに、
羽のような花弁が行儀よく並べられている。

# 竹馬へ：ここハルジオン舞わせることできる？

今まで何度も見かけたことはあるが、
名前を知ったのは初めてだった。

y「ハルジオンはね、凄く可愛そうな花なんだよ。『貧乏草』って呼ばれることもあって、折ったり摘んだりすると貧乏になるなんて言われてるの」

彼女は何か特別な宝物を発見したかのように喜んで近寄り、
しゃがんでその花をまじまじと見つめた。

s「酷い風評被害だね。
人間のせいで不名誉なあだ名をつけられて」

僕も彼女に倣って前に屈み、横に並んだ。

# y：神妙な表情をする

y「でもね、花言葉は、『追想の愛』なんだよ。
この下を向いている様子が、
　　　　過去を思い出して何か考えてるみたいだから」

# 一秒空けてほしい

s「なんだか悲しい花言葉だな。故人を偲んでるとか？」

僕のネガティブな推測を振り払うように、
首を振りながら彼女は顔を上げた。

y「案外、昨日の晩御飯を思い出してるだけかもよ」

s「それは追想って言えるの？」

y「多分言えるよ。{w}私が保証する」

# 結夏消す

美しかった記憶は、段々と薄れていく。

「秋に咲くのはハルジオンじゃなく、ヒメジョンだよ」
と訂正することもできないまま、今日まで来た。

人は、
人は過ぎていくものだ。

そう、分かってはいるけれど。

僕には、彼女さえいれば、何でも良かった。

彼女の居場所は、一輪の花だけが知っている。
```