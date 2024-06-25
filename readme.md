# 使い方

* file.txtに書いてある内容から3つのデータを選び取る
``` bash
$ python3 random-choice.py --file file.txt -k 3
```

* items.txtに書いてある内容から1つのデータを選び取る

``` bash
$ python3 random-choice.py --file items.txt -k 1
```

## 引数
    -f, --file
        選び取るデータが改行区切りになっているファイル
    -k
        ランダムに選び取るサンプルの個数

# メモ

* ファイルのエンコーディングはUTF-8のみ
* ソースコードは型ヒントをつけています。（ただしリファレンスにもある通り型チェックは行われていません）
* 選び取られるデータは重複しません。（random.sample()参考）
