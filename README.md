# Pyxel_Web_Test
## PymunkをWeb版Pyxelで動かす
Pyxel × Pymunkで物理シミュレーションを始めよう！

https://qiita.com/malo21st/items/32b7865e7c78d4ac2741

「Pyxel × Pymunkで物理シミュレーションを始めよう！」を Webで動かしたい🌎

https://qiita.com/Kazuhito/items/cf7f2e0f42f47e611f3e

こちらの記事でWeb版のPyxelでPymunkを動かすのに大変なことをされていたので、もっと簡単に動かせないか試したら出来ました。

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

### 補足
packageにpymunkのwheelファイルを指定しただけでは動かず、その前提となるcffiモジュールが必要だったので、その記述も追加したら動きました。
cffiモジュールはPyodide公式で対応しているのでpackageにcffiと書くだけでOKでした。
