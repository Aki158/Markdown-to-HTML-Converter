# Markdown-to-HTML-Converter

## 🌱概要
MarkdownをHTMLへ変換できるスクリプト

## ✨デモ
![output](https://github.com/Aki158/Markdown-to-HTML-Converter/assets/119317071/128c78e8-07e3-481f-aaf4-d4db42557db1)

## 📝説明
このスクリプトは、コマンド入力を利用してMarkdownをHTMLへ変換できるスクリプトです。

スクリプトの実行には、ターミナルという黒い画面にコマンドを入力します。

Markdownは、簡単な記法を使って書式付きの文書を作成することができます。

Webエンジニアやwebデザイナーなどのコンテンツクリエーターは、Markdownで文書を作成することがあります。

このスクリプトでは、文書作成時にMarkdownを使用しアウトプットとしてHTMLに変換させたい!という場面に使えるスクリプトです。

基本的な機能として、MarkdownをHTMLへ変換することができます。

また、MarkdownとHTMLそれぞれのファイルのイメージは、下記リンクから確認することができます。
- [Markdown](https://github.com/Aki158/Markdown-to-HTML-Converter/blob/main/sample.md)
- [HTML](https://github.com/Aki158/Markdown-to-HTML-Converter/blob/main/index.html)

### 追記
このスクリプトの作成後に拡張版を作成しました。

詳細は、下記リンクをクリックして確認ください。

[Markdown-to-HTML](https://github.com/Aki158/Markdown-to-HTML)

### 補足
#### 用語集
[説明](#説明)で登場する用語について補足します。

用語の意味がわからない時は、下記表を確認してください。

| 用語 | 意味 |
| ------- | ------- |
| Markdown | 簡単な記法で読みやすく、HTMLなどの他の形式に変換できることを目的としたテキストベースの軽量マークアップ言語です。 |
| HTML | Webページを作成するための標準的なマークアップ言語です。<br>テキスト、画像、リンク、フォームなどのWebコンテンツをブラウザに表示する際に必要となる指示を提供しています。 |
| スクリプト | 一連のコマンドや命令を記述したテキストファイルのことで、コンピュータに特定のタスクを自動的に実行させるために使用されます。<br>スクリプトは、特定のスクリプト言語（例：Bash、Python、Perl、Ruby、JavaScriptなど）で書かれます。<br>今回は、Pythonを使用してスクリプトを作成しています。 |
| ターミナル | コンピュータに対してテキストベースのコマンド入力と出力を行うインターフェースのことです。<br>このインターフェースは、コマンドラインインターフェース（CLI）とも呼ばれます。<br>[デモ](#デモ)の途中に登場する黒い画面のことです。 |
| コマンド | コンピュータに対して特定の操作を実行するよう指示するテキストベースの命令です。<br>コマンドを入力することで、コンピュータは、コマンドの意味を読み取りアクションをおこします。 |

#### Markdownの記述方法について
下記記事にわかりやすく一覧でまとめてありました。

不明な点がある場合は、確認してください。

[Markdown記法一覧](https://qiita.com/oreo/items/82183bfbaac69971917f#:~:text=Markdown%EF%BC%88%E3%83%9E%E3%83%BC%E3%82%AF%E3%83%80%E3%82%A6%E3%83%B3%EF%BC%89%E3%81%AF%E3%80%81,%E3%82%82%E9%96%8B%E7%99%BA%E3%81%95%E3%82%8C%E3%81%A6%E3%81%84%E3%82%8B%E3%80%82)

#### HTMLについて
下記ドキュメントに基本的な情報がわかりやすく記載してありました。

不明な点がある場合は、確認してください。

[HTML の基本](https://developer.mozilla.org/ja/docs/Learn/Getting_started_with_the_web/HTML_basics)

## 🧰前提条件
このスクリプトを実行するには、下記ソフトウェアを事前にインストールしておく必要があります。

インストールされていない場合は、[インストール](#インストール)/[使用方法](#使用方法)/[使用例](#使用例)で記載されているコマンドが実行できませんので

必ずインストールしてから進めてください。

### Git
Gitがインストールされていない場合は、下記手順でインストールしてください。

1. ターミナルを起動する。<br>使用するOSによりターミナルの名称が異なりますので注意してください。<br>(例. Windows:コマンドプロンプト,mac:ターミナル)

2. Gitがインストールされているか確認する。<br>`git version 2.34.1` のように表示された場合は、Gitがインストールされています。<br>以降の手順はスキップしてください。<br>**また、ターミナルは引き続き使用しますので開いたままにしてください!**
```
git --version
```

3. システムを更新する
```
sudo apt-get update
```

4. Gitをインストールする
```
sudo apt install git
```

5. Gitがインストールされたことを確認する。<br>`git version 2.34.1` のように表示されていれば、Gitのインストールは完了です!
```
git --version
```

### Python 3.x
[Python](https://www.python.org/downloads/)の公式サイトからあなたのPCのOSに合わせて、ダウンロードしてください。

ダウンロードしたファイルを使用してインストールできます。

Pythonがインストールされているかは、下記コマンドで確認することができます。

`Python 3.10.12`のように表示されていれば、Pythonはインストールされています。

```
python3 --version
```

### pip
pipは、Python用のパッケージマネージャで、パッケージのインストールと管理を行うことができます。

[pipのインストールガイド](https://pip.pypa.io/en/stable/installation/)に従って、pipをインストールしてください。

aptを使用してpipをインストールする場合は、下記手順でインストールしてください。

1. pipがインストールされているか確認する。<br>`pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)` のように表示された場合は、pipがインストールされています。<br>以降の手順はスキップしてください。
```
pip3 --version
```

2. システムを更新する
```
sudo apt-get update
```

3. pipをインストールする
```
sudo apt install python3-pip
```

4. pipがインストールされたことを確認する。<br>`pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)` のように表示されていれば、pipのインストールは完了です!
```
pip3 --version
```

### markdown

markdownは、MarkdownをHTMLへ変換する機能を提供しているPythonのパッケージです。

pipを使用して、下記手順でインストールしてください。

[pip](#pip)は、あらかじめインストールしておいてください。

また、markdownについて詳しく知りたい場合は、[markdownのプロジェクトの説明](https://pypi.org/project/Markdown/)を確認してください。

1. markdownがインストールされているか確認する。<br>Name/Version/Summaryなどが表示された場合は、markdownがインストールされています。<br>以降の手順はスキップしてください。
```
pip3 show markdown
```

2. markdownをインストールする
```
pip install markdown
```

3. markdownがインストールされたことを確認する。<br>Name/Version/Summaryなどが表示されていれば、markdownのインストールは完了です!
```
pip3 show markdown
```

## 🍴インストール
### クローン
このスクリプトをあなたのPCで実行するために、クローンします。

クローンとは、このスクリプトの実行に必要なファイル(リポジトリのコンテンツ)をあなたのPCのローカル環境へコピーすることです。

下記手順でクローンしてください。

1. リポジトリをクローンする
```
git clone https://github.com/Aki158/Markdown-to-HTML-Converter.git
```

2. クローンしたリポジトリへ移動する
```
cd Markdown-to-HTML-Converter
```

## 🚀使用方法
1. Markdownファイル(.md)を用意する
2. スクリプトを実行する
3. 生成されたファイル(.html)を確認する

## 🙋使用例
一通りの手順のイメージは[デモ](#デモ)を参考にしてください。

1. Markdownファイル(.md)を用意する。<br>インプットとなるファイルを作成してください。<br>ファイルは、Markdown形式で記述しておく必要があります。<br>今回は、動作確認をしたいので、クローンした際にコピーされたsample.mdというファイルを使用します。
2. スクリプトを実行する。<br>スクリプトを利用する際は、ターミナルに[コマンドの入力例](#コマンドの入力例)のようなコマンドを入力します。<br>今回は、[コマンドの入力使用例](#コマンドの入力使用例)のようにコマンドを入力しました。
3. 生成されたファイルを確認する。<br>index.htmlというHTMLファイルが生成されていました。

### 手順2の補足
#### コマンドの入力例
```
python3 file-converter.py markdown [inputpath] [outputpath]
```
| コマンド | 内容 |
| ------- | ------- |
| `[inputpath]`| 手順1.で用意したファイルのパスを入力します。<br>パスには、用意したファイルの名前まで含めてください。 |
| `[outputpath]`| スクリプトを利用することで、生成されるファイルのパスを入力します。<br>パスには、生成されるファイルの名前まで含めてください。 |

#### コマンドの入力使用例
```
python3 file-converter.py markdown ../python_practice/sample.md ../python_practice/index.html
```

## 💾使用技術
<table>
<tr>
  <th>カテゴリ</th>
  <th>技術スタック</th>
</tr>
<tr>
  <td>開発言語</td>
  <td>Python</td>
</tr>
<tr>
  <td rowspan=2>インフラ</td>
  <td>Ubuntu</td>
</tr>
<tr>
  <td>VirtualBox</td>
</tr>
</table>

## 👀機能一覧
![image](https://github.com/Aki158/Markdown-to-HTML-Converter/assets/119317071/e38f9ff0-4e14-4f40-92e3-736bed508215)

| 機能 | 内容 |
| ------- | ------- |
| markdown | markdownをhtmlに変換します。 |
| エラーハンドリング | コマンドが正しく入力されていない場合は、下記のようなメッセージが表示されて終了します。<br>・inputpathが存在しない場合:`Inputfile does not exist...`<br>・入力されるコマンドが4つではない場合:<br>　`　Wrong usage!`<br>　`useage : python3 file-converter.py markdown inputfile outputfile`<br>入力されたコマンドが、markdownでない場合:`Command not found...` |

## 📜作成の経緯
⭐️後で記載する!!!

作成した理由を記載する。

## ⭐️こだわった点
⭐️後で記載する!!!

テキストや参考にした記事などを再度読み返して技術の理解を深めてから書く。

ここがエンジニアに一番読んでもらいたい箇所なのでできるだけ詳細に書く。

## 📮今後の実装したいもの
- [x] オンラインでエディタに記述したMarkdownをHTMLへ変換できるサービスを作成する

## 📑参考文献
### 公式ドキュメント
- [Python](https://docs.python.org/ja/3/)

### 参考にしたサイト
- [Python_Download](https://www.python.org/downloads/)
- [pipのインストールガイド](https://pip.pypa.io/en/stable/installation/)
- [markdownのプロジェクトの説明](https://pypi.org/project/Markdown/)
- [Markdown記法一覧](https://qiita.com/oreo/items/82183bfbaac69971917f#:~:text=Markdown%EF%BC%88%E3%83%9E%E3%83%BC%E3%82%AF%E3%83%80%E3%82%A6%E3%83%B3%EF%BC%89%E3%81%AF%E3%80%81,%E3%82%82%E9%96%8B%E7%99%BA%E3%81%95%E3%82%8C%E3%81%A6%E3%81%84%E3%82%8B%E3%80%82)
- [HTML の基本](https://developer.mozilla.org/ja/docs/Learn/Getting_started_with_the_web/HTML_basics)

