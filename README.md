# Hassaku🍊
画像一致でウィンドウ内の部品を特定し、操作するライブラリ。(予定)

## 環境構築
### ライブラリのインストール
```sh
pip install -r requirements.txt
```

### 部品特定用画像の準備
- Hassakuを使って実装したアプリのワーキングディレクトリに ```resources``` ディレクトリを用意する
- ```resources``` ディレクトリ内にウィドウから検索する画像を配置。対応画像フォーマットは ```.png``` 、 ```.bmp``` 
  - ```resources``` ディレクトリ以下に子ディレクトリを作成し、画像を配置した場合、 ```resources``` ディレクトリ直下のフォルダ以下の全ファイルで画像一致を試みます
      - 画面の拡大率などで同一画像でサイズが異なるものを用意したい時等に使用してください
  - Hassakuは ```resources``` ディレクトリ直下の画像ファイル名(拡張子を除く)もしくはディレクトリ名で検索画像を指定します

# サンプル
フォルダ構成
```sh
sample
 ├─ sample.py
 ├─ resources
 │   ├ 1.png
 │   └ 2
 │     ├ small.png
 │     └ big.png
 └─Hassaku
```

sample.py
```python
from hassaku import Hassaku 

hassaku = Hassaku()

"""
「test.txt - メモ」帳には以下の文字列が記載

1 2 3 4 5 
6 7 8 9 10
"""

# resources/1.pngの座標を取得
print(hassaku.find_image_from_window("test.txt - メモ帳", "1"))

# resources/2フォルダ以下の画像で検索
print(hassaku.find_image_from_window("test.txt - メモ帳", "2"))

```

実行結果
```sh
# 1の出現座標(左上x座標, 左上y座標, 右下x座標, 右下y座標)のリスト
# 1 と 10 で2回出現しているので2個取得
[(21, 109, 28, 128), (101, 129, 108, 148)]
# 2の出現座標
[(41, 111, 49, 126)]
```
