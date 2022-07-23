# O[1 0]章 思いついた

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　電脳数（Cyber Number）を思いついたぜ」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462d7c6e036697.png)  
「　また勝手な真似をして……」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762d7c6fae1599.png)  
「　それは　**数**　なの？」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　ベクトル（Vector）だぜ」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462d7c6e036697.png)  
「　じゃあ　`電脳数`　ではなくて　`ベクトル`　だろ」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　数とか ベクトル（Vector）を思いついたのではなくて、表記（Notation）を思いついたんだぜ」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762d7c6fae1599.png)  
「　じゃあ　思いついたのは　**表記**　よね」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　電脳ベクトル表記（Cyber Vector Notation） という名前の方が適切かだぜ？  
日本語にすると **電脳向量表記** （でんのうこうりょうひょうき）？」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462d7c6e036697.png)  
「　めんどくせ。　じゃあ　電脳数で」  

# O[2 0]章 Python実装

📖 [cyber-vector-notation](https://github.com/muzudho/cyber-vector-notation)  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「 👆 電脳向量表記は Python にクラスとして実装してある。もう使える。  
話しを聞くより、動かして覚えたい人は 使ってくれだぜ」  

# O[3 0]章 ベクトルを使おうぜ

```plaintext
[128 0 0 1]
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　👆 電脳向量表記のもとの数はベクトルなんで、こういうやつの **表記** を発案したわけだぜ」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762d7c6fae1599.png)  
「　**IP v4** なら `128.0.0.1` ねぇ」  

```plaintext
OAA128o0o0o1o0
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　👆 電脳向量表記では　こうだぜ」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462d7c6e036697.png)  
「　要らんことしてくれるの　わらう」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762d7c6fae1599.png)  
「　`O` とか `A` とか `o` とか、末尾に `o0` が余分に付いてるわよ」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　電脳向量表記を使っている、という明示で 左端に `O` を付けるぜ。  
`A` は 辞書順に並べるために 2桁以上の正の整数の前に詰めていく。詳しくはあとで説明する。  
小文字の `o` はカンマの代わりだぜ。  
大文字、小文字は区別しない」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　電脳向量表記では　右端の列には `0` を明示している必要があるぜ。  
これを `With trailing zero` 、略して **`trail_zero`ルール** と呼ぶぜ」  

## O[3 1 0]章 負数も扱おうぜ

```plaintext
[18 -4 -13 71]
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　👆 負数だって扱いたいよな」  

```plaintext
OA18o_6o__87o71o0
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　👆 電脳向量表記では　こうだぜ」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762d7c6fae1599.png)  
「　読みにくくなってるわよね」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　辞書順に並ぶ工夫をしてある」  

# O[4 0]章 フォルダーでも使おうぜ

```plaintext
📂 2022
└── 📂 07
    └── 📂 20
        └── 📄めんどくせ.txt
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　👆 また、上記のような　年月日フォルダー　も想定している。 以下を見てほしい」  

```plaintext
[2022], [7], [20]
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　👆 ベクトルが ワンライナー（１行）に 3個ある、と考えてほしい」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462d7c6e036697.png)  
「　ベクトルが　ネストしそうな雰囲気をしてるな」  

```plaintext
OAAA2022o0g7o0g20o0
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　👆 `g` でつないでくれだぜ。  
小文字の `g` は カンマ `,` に似ているから そうした」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462d7c6e036697.png)  
「　こんなフォルダー名付けてるやつのパソコン開けたくないよな」  

# O[5 0]章 章立てに振る番号でも使おうぜ

```plaintext
1. 食べ物
1.1. 果物
1.1.1. アップル
1.1.2. バナナ
1.1.11. キーウィ
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　👆 また、上記のような　ドキュメントの章立てに振る番号も想定している。 以下を見てほしい」  

```plaintext
[1]
[1, 1]
[1, 1, 1]
[1, 1, 2]
[1, 1, 11]
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　👆 ベクトルが 4行分ある、と考えてほしい」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762d7c6fae1599.png)  
「　ファイルエクスプローラーでも Word でも Excel でも Note でも Visual Studio でも プログラム仕様書 でも Confluence でも見かけるわねぇ。  
**職業プログラマーのIT利用技術にうんざりして生まれてきた数**　というだけある実例ねぇ」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　次の日の朝、ドキュメントを開くと　**リナンバリング**　されていることがある。  
`Id` もリナンバリング、文章番号も `リナンバリング`、特に　欠番，飛び番は嫌がられて　連番　だぜ」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462d7c6e036697.png)  
「　通し番号なんか　振るなだぜ」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　リモートの Windowsのフォルダー名に付いている章立ての番号が次の日リナンバリングされていて  
フォルダーへのパスが変わってるから ファイル アクセスできなくなっていることがある。  
それが嫌で **電脳向量表記のもとの数** は生まれてきた。  
言うなれば **電脳向量** だぜ」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462d7c6e036697.png)  
「　ショートカット 切れるしな」  

```plaintext
O1o0
O1o1o0
O1o1o1o0
O1o1o2o0
O1o1oA11o0
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　👆 電脳向量表記だぜ」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462d7c6e036697.png)  
「　リナンバリングされるのは　解決するのか？」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　伝説の BASIC 言語　よりいい感じに解決する」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　伝説の BASIC 言語では　1, 2, 3 ... ではなく 10, 20, 30 ... にしましょう、という習慣がある。  
20 と 30 の間に行を足したくなったら 25 を差し込めるからだぜ」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762d7c6fae1599.png)  
「　自己稠密な **小数** を使えばいいのに……」  

```plaintext
00. 食べ物
00.00. 果物
00.00.00. アップル
00.00.01. バナナ
00.00.10. キーウィ
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　👆 小数でも解決しない。 振り番に `0` を使われてしまったときだぜ。  
前ゼロを使って 2桁の数を使うシーンで `01` ではなく `00` から始まってるのをよく見かける。  
0 の前に記事を挿入しようと思っても、 0 より小さい数はない。小数を使っても無理。詰んだ」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462d7c6e036697.png)  
「　序数を 0 から始めるやつに 社内のルール作りをやらせるなだぜ。  
物を数えるときに　指０本立てるところから数え始めるのか」  

```plaintext
O[0 0] 食べ物
O[0.0 0] 果物
O[0.0.0 0] アップル
O[0 0 1 0] バナナ
O[0 0 10 0] キーウィ
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　👆　そういうとき、 (1) `trail-zero` して、」  

```plaintext
O[0 -1 0] 食べ物の前に
O[0 0] 食べ物
O[0.0 -1 0] 果物の前に
O[0.0 0] 果物
O[0.0.0 -1 0] アップルの前に
O[0.0.0 0] アップル
O[0 0 1 -1 0] バナナの前に
O[0 0 1 0] バナナ
O[0 0 10 -1 0] キーウィの前に
O[0 0 10 0] キーウィ
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　👆　(2) 右端の列を `-1` して `trail_zero` すれば　前に記事を挟める」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462d7c6e036697.png)  
「　見づら」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　この２ステップを合わせて `insert before here` 操作と呼ぶことにするぜ」  

```plaintext
O0o_9o0 食べ物の前に
O0o0 食べ物
O0o0_9o0 果物の前に
O0o0o0 果物
O0o0o0_9o0 アップルの前に
O0o0o0o0 アップル
O0o0o1_9O0 バナナの前に
O0o0o1o0 バナナ
O0o0o10o_9o0 キーウィの前に
O0o0o10o0 キーウィ
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　👆 `-1` は Windowsのフォルダーでは `0` より前に行かないので `辞書順記数法` を使って `_9` と書くぜ」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762d7c6fae1599.png)  
「　でも 会社の人が こんなん見たら あんたクビになるわよね」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　わたしは 会社の人に合わせて 生きてないんで」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462d7c6e036697.png)  
「　そんなやつ 面接で通すなだぜ」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　**電脳向量表記** の方が優れているんで」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762d7c6fae1599.png)  
「　確信犯の原義が適用できる人なの わらう」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462d7c6e036697.png)  
「　こんなダメなものが流行り始める前に プログラム言語と フォルダー名ソートの方を 改良してほしい」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　プログラム言語や OS が改良しても、 目の前の１つのアプリが対応してなかったら意味無いぜ。  
電脳向量表記は 一番だめなやつになるべく幅広く合うようにしている。最悪の中での原理的な妥協だぜ」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762d7c6fae1599.png)  
「　**バッドノウハウ** っていうのよそれ」  

# O[6 0]章 普通の表記と、電脳ベクトル表記の比較

```plaintext
# ふつう
2022年07月20日

# 電脳ベクトル表記
OAAA2023o7oA20o0
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　👆 フォルダーの名前で使うにはカンマ（`,`）が使えないので
小文字のオー(`o`)を使うこととし、  
10進数は、 `その桁数×２－１` の桁数があると考えて、前ゼロの代わりに 大文字のエー(`A`)で埋めてくれだぜ」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762d7c6fae1599.png)  
「　16進のとき、 `A` は邪魔じゃない？」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　16進という表記には対応していない。 10進にしろ」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　電脳数は、前ゼロという表記にも対応してないからな」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762d7c6fae1599.png)  
「　あなた以外の人類は　カンカンに怒りそう」  

```plaintext
# ふつう
[-1 -21 -321]

# 電脳ベクトル表記
O_9o__79o___679o0
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　👆 マイナスは Windowsのフォルダーの名前順では 0 の前にこないので アンダースコア(`_`)を使うこととし、  
`負数の桁数×２` の桁数があると考えて、前ゼロの代わりに アンダースコア(`_`)で埋めてくれだぜ。  
このとき、`あとで説明する数n + その負数` にしてくれだぜ」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762d7c6fae1599.png)  
「　**あとで説明する数n** って何？」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　1～9 の n は 10、 10～99 の n は 100、 100～999 の n は 1000 だぜ」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462d7c6e036697.png)  
「　その数の絶対値より1桁大きい数の中で最小の数だな」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「　詳しくは `辞書順記数法` を見てくれだぜ。負数の説明もある」  

# O[7 0]章 変数名，クラス名，フォルダー名，ファイル名 etc

```plain
_ 0 1 2 3 4 5 6 7 8 9  A G O a g o
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「 👆 電脳数は 上記の文字だけで記せる数で、大文字小文字を無視しても構わない（Ignore case）ぜ」  

```plaintext
var o2o1banana = new O2o1Banana()

o2o1banana.loadsVO2o1(r"C:\This\Is\A\Path\O2o1\bananaO3o2o1.txt")
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「 👆 変数名，クラス名，メソッド名，フォルダー名，ファイル名にも　たいてい使える文字だな」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462d7c6e036697.png)  
「 BASE64 みたいな考え方だ」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「 **電脳向量** がプログラムのクラス名やフォルダーの名前で使えないのが嫌で **電脳向量表記** が生まれてきた。  
事実は逆順で、先に **電脳向量表記** を作って、あとで **電脳向量** に気づいた」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762d7c6fae1599.png)  
「 名前の生態系や、プログラマーの文化や、数学の美的感覚を破壊しにいってるわね」  

```plaintext
📂 O___100o0
📂 O__99o0
📂 O__10o0
📂 O_9o0
📂 O0o0
📂 O1o_9o0
📂 O1o0
📂 O1o0o1o0
📂 O9o0
📂 OA10o0
📂 OA99o0
📂 OAA100o0
📂 OAA999o0
📂 OAAA1000o0
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「 👆 これで わたしは楽になった」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462d7c6e036697.png)  
「 こんな脳してるやつ 学校にいても 会社にいても おかしい人だと思われるの 妥当だぜ」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762d7c6fae1599.png)  
「 低賃金の仕事にしか就けないわよね」  

```plaintext
📂 OA10oAAA1000o0
📂 OAA100oAA100o0
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62d7c6c5ba4a3.png)  
「 👆 ベクトルの左の列の数から優先して昇順だぜ。 楽だろ」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462d7c6e036697.png)  
「 この表記を読むのも書くのも 楽じゃないだろ」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762d7c6fae1599.png)  
「 わらう」  

# O[8 0]章 関連する記事

📖 [電脳向量表記 (Cyber Vector Notation)](https://crieit.net/posts/Cyber-Number-Notation)