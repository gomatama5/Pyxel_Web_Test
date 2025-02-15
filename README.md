# Pyxel_Web_Test
## 概要
Web版Pyxel公式では、Pyodideで公式対応**している**モジュールの導入方法の説明があります。

https://github.com/kitao/pyxel/blob/main/docs/pyxel-web-ja.md

そこで、Pyodideで公式対応**していない**モジュールの導入方法について調べました。

## PymunkをWeb版Pyxelで動かす
Pyxel × Pymunkで物理シミュレーションを始めよう！

https://qiita.com/malo21st/items/32b7865e7c78d4ac2741

「Pyxel × Pymunkで物理シミュレーションを始めよう！」を Webで動かしたい🌎

https://qiita.com/Kazuhito/items/cf7f2e0f42f47e611f3e

こちらの記事でWeb版のPyxelでPymunkを動かせるようにPymunk公式さんに対応していただいたようで、素晴らしいですね！

ただ、PyxelでPymunkモジュールをロードするのに大変なことをされていたので、もっと簡単に動かせないか試したら出来ました。

動作確認URL：
https://gomatama5.github.io/Pyxel_Web_Test/shot_bullet.html

最初の記事の.pyファイルをそのままWeb版のPyxelで動かせます！

### やり方
Web版のhtmlで
```
<pyxel-run name="shot_bullet.py"></pyxel-run>
```
を
```
<pyxel-run name="shot_bullet.py" packages="cffi,pymunk-6.11.1-cp312-cp312-pyodide_2024_0_wasm32.whl"></pyxel-run>
```
というようにpackageの記述を追加するだけでOKです。

尚、PymunkのPyodide対応Wasm Wheelは上記記事でも紹介されていますが、Pymunk公式GitHubのReleaseページにあります。

https://github.com/viblo/pymunk

### 補足
packageにPymunkのWheelファイルを指定しただけでは動かず、その前提となるcffiモジュールが必要だったので、その記述も追加したら動きました。
cffiモジュールはPyodide公式対応しているのでpackageにcffiと書くだけでOKでした。

# typehandlerをWeb版Pyxelで動かす
【typehandler】最短9行で実装！タイピングゲーム用のPythonモジュールを作ってみた

https://qiita.com/Prosamo/items/23e9a64c6199e035abf1

【40行で実装】Pyxelでタイピングゲームを作りたい！

https://qiita.com/Prosamo/items/3717b34e2ed110ebd8e5

こちらの記事でタイピングゲーム用のPythonモジュールを紹介されています。
これをWeb版のPyxelで動かしてみました。

動作確認URL：
https://gomatama5.github.io/Pyxel_Web_Test/simple_typing.html

### やり方
タイピングゲーム用のPythonモジュールのtypehandlerはPure Pythonで書かれているそうで、Wheelを指定するだけで動きました。
```
<pyxel-run name="simple_typing.py" packages="typehandler-0.5.1-py3-none-any.whl"></pyxel-run>
```

Wheelは、作者様が公開されているGitHubページのdistフォルダ以下からダウンロードするかpip downloadすればOKです。

https://github.com/Prosamo/typehandler/

### 補足
動作確認用コードは必要最小限に絞りました。
日本語を表示するとかもっとちゃんと作る場合は、上記の記事で作者様がサンプルを公開されているので、それを見ると良いでしょう。
