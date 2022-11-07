# **git・github 運用ルール**

- [**git・github 運用ルール**](#gitgithub-運用ルール)
  - [**git インストール手順**（git version2.38.0 時点）](#git-インストール手順git-version2380-時点)
    - [**インストール確認**](#インストール確認)
    - [**git の初期設定**](#git-の初期設定)
  - [**github 登録手順**](#github-登録手順)
  - [**git 基本用語**](#git-基本用語)
  - [**ブランチ運用**](#ブランチ運用)
  - [**ブランチ命名規則**](#ブランチ命名規則)
  - [**コード管理の流れ**（VScode 上のターミナルから実行）](#コード管理の流れvscode-上のターミナルから実行)

<br>

## **git インストール手順**（git version2.38.0 時点）

1. 公式サイトよりダウンロード（Windows 版）
2. ライセンスへの同意（そのまま Next）
3. インストール先フォルダ（そのまま Next）
4. コンポーネント（ショートカットが必要なら「On the Desktop」にチェック）
5. スタートメニューの表示名（そのまま Next）
6. エディタ設定（VScode 等、自分の使っているエディタを選択）
7. デフォルトブランチ名（そのまま Next）
8. Windows の環境設定 PATH への追加設定（そのまま Next）
9. HTTPS アクセスルート（そのまま Next）
10. テキストファイル改行（「Checkout Windows-style」を選択）
11. その他はデフォルト設定、最後に Install で完了

### **インストール確認**

コマンドプロンプトで以下のコマンドを実行
git のバージョンが表示されればインストール成功

```console
git --version
```

### **git の初期設定**

Windows メニューの中に「Git」フォルダが作成されているので、その中の「Git Bash」フォルダをクリックし起動
ユーザー名とメールアドレスの設定（以下のコマンドを実行）

```console
git config --global user.name “[自分の名前]”（例：TetsuyaAoki）
```

```console
git config --global user.email “[自分のメールアドレス]”
```

「Git Bash」を再起動、「pwd」コマンドを実行しカレントディレクトリとホームが一致しているかを確認

```console
pwd
```

「git config -l」コマンドを実行し、ユーザー名とメールアドレスの設定を確認したら初期設定は完了

```console
git config -l
    user.name = [設定した名前]
    user.email = [設定したメールアドレス]
```

参考
[Git 初期設定から VSCode と GitHub の連携まで徹底解説](https://literacyboxes.com/git-install-windows/)

<br>

## **github 登録手順**

1. アカウント基本情報の登録
    Username（氏名）
    Email address（メールアドレス）
    Password（パスワード）
2. 仮登録完了後、登録確認メールが送られてきたら、メール本文のコードを仮登録完了画面に入力
3. アンケート入力（アンケートページが出る場合）
4. プラン選択（無料プラン）
5. 「Learn Git and GitHub without any code!」と表示されたら登録完了

参考
[github とは？登録方法から活用方法までご紹介](https://pig-data.jp/blog_news/blog/whatisgithub/)
[Github に登録して、リポジトリを作成する！【2022 年版】](https://codelikes.com/github-account-register/)

<br>

## **git 基本用語**

| 用語               | 意味                                                       |
| ------------------ | ---------------------------------------------------------- |
| リポジトリ         | ソースファイルなどを管理するための格納場所                 |
| リモートリポジトリ | チームメンバーとサーバー上で共有するリポジトリ             |
| ローカルリポジトリ | マスターリポジトリをコピーして各担当者が管理するリポジトリ |
| クローン           | リポジトリをコピー（複製）する                             |
| フォーク           | 他の開発者のリポジトリを GitHub 上でクローンする           |
| イニット           | リポジトリを新規作成する                                   |
| プル               | マスターリポジトリのデータをローカルリポジトリに取り込む   |
| プッシュ           | ローカルリポジトリの変更内容をマスターリポジトリに加える   |
| コミット           | ファイルやディレクトリの作業をローカルリポジトリに記録     |
| ワークツリー       | ユーザーが作業中のディレクトリ                             |
| マージ             | 異なるリポジトリの変更内容を統合                           |
| コンフリクト       | 同じファイルの同一箇所で同時に変更が起こってしまうエラー   |

参考
[【Git 入門】基礎知識から使い方、学習法までわかりやすく解説](https://www.sejuku.net/blog/72524)

<br>

## **ブランチ運用**

ブランチ運用は GitHubFlow を採用する。
![GitHubFlow](https://image.itmedia.co.jp/ait/articles/1708/01/l_at-it-git-15-009.jpg)

GitHubFlow の 6 つのルール

- master ブランチは常にデプロイ可能である
- 作業用ブランチを master から作成する（例：feature/login）
- 作業用ブランチを定期的にプッシュする
- プルリクエストを活用する
- プルリクエストが承認されたら master へマージする
- master へのマージが完了したら直ちにデプロイを行う

参考
[git-flow、GitHub Flow を開発現場で使い始めるためにこれだけは覚えておこう](https://atmarkit.itmedia.co.jp/ait/articles/1708/01/news015.html)

<br>

## **ブランチ命名規則**

永続ブランチ

- デフォルトブランチ：master

一時ブランチ

- バグフィックスブランチ 例：bug/○○/○○
- ホットフィックスブランチ（緊急バグ） 例：hotfix/○○/○○
- 機能開発ブランチ 例：feature/○○/○○

<br>

ブランチの 5 つの命名規則

- カテゴリー名で始める 例：bug、feature など
- 区切り文字としてスラッシュを使用する 例：feature/○○ など
- 開発者名を使用する 例：tetsuya/feature/○○ など
- 半角小文字のみ
- 長いブランチ名を避ける

**<span style="color: red; ">まとめると tetsuya/feature/○○/○○ などのブランチ名に統一する</span>**

参考
[ブランチ命名規則と開発効率化](https://takeda-no-nao.net/programming/git/git-branch-naming-convention/)

<br>

## **コード管理の流れ**（VScode 上のターミナルから実行）

準備

```console
# gitで管理するフォルダを設定する
git init

# ローカル環境にリモートリポジトリからソース取得
git clone [クローン先URL]
cd [クローンして生成されたディレクトリ]

# アップロード先のリポジトリを設定する
git remote add origin [アップロード先URL]（https:~）
```

プル

```console
# ローカルリポジトリでmasterに入る
git checkout master

# リモートリポジトリを最新の状態にする
git pull
```

ブランチを切る

```console
# 自身のローカル環境にあるブランチを確認
git branch
    tetsuya/feature/○○
    * master
    （*が付いているのが今いるブランチ）

# ブランチを作る
git branch [ブランチ名]

# ブランチに移動
git checkout [移動先のブランチ名]
```

ソースコードの改修を行う（プログラミング）

変更した箇所の確認

```console
# 変更したファイルの一覧を確認
git status
    modified：修正したファイル
    deleted：削除したファイル
    Untracked files：新規作成したファイル

# 変更したファイルのソースコードを確認（qキーで終了）
git diff
```

コミット

```console
# 変更したファイルを選択
git add [ファイル名]

# コミット対象を確認
git status

# コミットする（-mでコメント）
git commit -m "コメント"
```

プッシュ

```console
# コミットログを確認する（qキーで終了）
git log

# プッシュ
git push origin [プッシュするブランチ名]
```

マージ（個人でやらない）

```console
# masterブランチに移動
git checkout master

# masterブランチにブランチをマージ
git merge [ブランチ名]

# リモートブランチを更新
git push origin master
```

以降、プルから繰り返す

参考
[VSCodeでGit・GitHubを使う方法を解説する【初心者向き】](https://miya-system-works.com/blog/detail/vscode-github/)
[gitを使った開発の流れとgitコマンドの基本操作](https://qiita.com/suzutsuki0220/items/be10604e9e13126eba44)
[gitを初めて使う時コミット→プッシュ→マージの流れ](https://qiita.com/yukiyoshimura/items/7aa4a8f8db493ab97c2b)
[Githubでチーム開発するためのマニュアル](https://qiita.com/siida36/items/880d92559af9bd245c34)
