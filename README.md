# 概要

[ポケモンカードゲーム サン&ムーン Wiki](https://wiki.xn--rckteqa2e.com/wiki/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E3%82%AB%E3%83%BC%E3%83%89%E3%82%B2%E3%83%BC%E3%83%A0_%E3%82%B5%E3%83%B3%26%E3%83%A0%E3%83%BC%E3%83%B3) からスクレイピングするスクリプト

# urlの設定

scraping.pyのurlにtitle.txtにあるリンクをコピペする

```
# 例: ポケモンカードゲーム サン&ムーン ハイクラスパック GXウルトラシャイニー
url = '/wiki/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E3%82%AB%E3%83%BC%E3%83%89%E3%82%B2%E3%83%BC%E3%83%A0_%E3%82%B5%E3%83%B3%26%E3%83%A0%E3%83%BC%E3%83%B3_%E3%83%8F%E3%82%A4%E3%82%AF%E3%83%A9%E3%82%B9%E3%83%91%E3%83%83%E3%82%AF_GX%E3%82%A6%E3%83%AB%E3%83%88%E3%83%A9%E3%82%B7%E3%83%A3%E3%82%A4%E3%83%8B%E3%83%BC'
```

# CSV形式のテキストファイルへ出力

```
python .\scraping.py > list.txt
```

結果の抜粋

```
110/150,ポケモン,無,タイプ:ヌル,-
111/150,ポケモン,無,シルヴァディGX,RR
112/150,トレーナーズ,グッズ,エネくじ,-
121/150,トレーナーズ,ポケモンのどうぐ,ウォーターメモリ,-
128/150,トレーナーズ,サポート,アセロラ,-
145/150,トレーナーズ,スタジアム,ワンダーラビリンス◇,PR
146/150,エネルギー,無,カウンターエネルギー,-
151/150,トレーナーズ,サポート,エーテル財団職員,SR
161/150,ポケモン,草,ストライク,S
250/150,ポケモン,竜,ウルトラネクロズマGX,UR
```