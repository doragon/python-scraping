# 概要

[ポケモンカードゲーム サン&ムーン Wiki](https://wiki.xn--rckteqa2e.com/wiki/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E3%82%AB%E3%83%BC%E3%83%89%E3%82%B2%E3%83%BC%E3%83%A0_%E3%82%B5%E3%83%B3%26%E3%83%A0%E3%83%BC%E3%83%B3) からスクレイピングするスクリプト。

上記wikiにてリンク切れとなっている個所に関しては、当然ですが失敗します。

## CSV形式のテキストファイルへ出力

```Shell
python .\src\scraping.py
```

## 結果の抜粋

### csv.txt

```CSV
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

### card_detail.txt

```Text
{'no': ['No.010'], 'name': ['キャタピー(C)'], '種類': ['たねポケモン'], 'HP': ['50'], '色': ['草'], 'ワザ1': ['ひとやすみ', '無', '', 'このポケモンのHPを「20」回復する。'], 'ワザ2': ['かじる', '無無', '20', ''], 'にげるコスト': ['－無'], '弱点': ['炎×2'], '抵抗力': ['なし'], 'イラスト': ['KanakoEo'], 'シリーズ': ['コレクションサン'], 'レアリティ': ['C(●)'], 'コレクションナンバー': ['001/060']}
{'no': ['No.011'], 'name': ['トランセル(C)'], '種類': ['1進化ポケモン'], '進化': ['キャタピーから進化'], 'HP': ['80'], '色': ['草'], 'ワザ1': ['てっぺき', '無', '', 'コインを1回投げオモテなら、次の相手の番、このポケモンはワザのダメージを受けない。'], 'ワザ2': ['むしくい', '無無無', '40', ''], 'にげるコスト': ['－無無無'], '弱点': ['炎×2'], '抵抗力': ['なし'], 'イラスト': ['YukaMorii'], 'シリーズ': ['コレクションサン'], 'レアリティ': ['C(●)'], 'コレクションナンバー': ['002/060']}
{'no': ['No.012'], 'name': ['バタフリー(C)'], '種類': ['2進化ポケモン'], '進化': ['トランセルから進化'], 'HP': ['130'], '色': ['草'], 'ワザ1': ['ねんりき', '無', '30', 'コインを1回投げオモテなら、相手のバトルポケモンをマヒにする。'], 'ワザ2': ['ふきとばし', '無無無', '80', '相手のバトルポケモンをベンチポケモンと入れ替える。[バトル場に出すポケモンは相手が選ぶ。]'], 'にげるコスト': ['－無'], '弱点': ['炎×2'], '抵抗力': ['なし'], 'イラスト': ['chibi'], 'シリーズ': ['コレクションサン'], 'レアリティ': ['U(◆)'], 'コレクションナンバー': ['003/060']}
```
