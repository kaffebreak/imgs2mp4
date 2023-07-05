# imgs2mp4
複数の画像をまとめて動画にすることができます。

## 必要なもの
- opencv-python
- tqdm

### Install
普通のとき
```command
pip install opencv-python tqdm
```
pipenv入れてるとき
```command
pipenv install
```

## 使い方
1. このリポジトリをクローンする
2. 画像が入ってるディレクトリをmain.pyのPATHに入れる
3. 実行する

## 注意点
Twitterとかにあげるときは、H.264形式じゃないとだめなので、OpenH264をPythonのカレントディレクトリに入れてください。
[cisco/openh264](https://github.com/cisco/openh264/releases)