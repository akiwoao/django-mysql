# **VScodeセットアップ**

- [**VScodeセットアップ**](#vscodeセットアップ)
  - [**VScodeインストール手順**](#vscodeインストール手順)
  - [**設定**](#設定)
  - [**拡張機能**](#拡張機能)
    - [**共通の拡張機能**](#共通の拡張機能)
    - [**フロントエンドの拡張機能**（HTML,CSS,JavaScript向け）](#フロントエンドの拡張機能htmlcssjavascript向け)
    - [**バックエンドの拡張機能**（Python向け）](#バックエンドの拡張機能python向け)

<br>

## **VScodeインストール手順**

1. 公式サイトからインストーラをダウンロード
    <https://code.visualstudio.com/download>
2. インストーラを起動、追加タスクの設定で[codeで開く]アクションを追加するに
    チェックを入れる、他はデフォルトでインストール
3. 完了をクリック後、VScodeが起動されればインストール完了

<br>

## **設定**

メニューの「表示」から「コマンドパレット」を選択
settingsと入力し、ユーザー設定（settings.json）を開き、下記に修正後、再起動

```console
{
    /* ---emmet--- */
    // true の場合、Emmet 候補をスニペットとして表示
    "emmet.showSuggestionsAsSnippets": true,
    // 有効にすると、TAB キーを押したときに Emmet 省略記法が展開されます。
    "emmet.triggerExpansionOnTab": true,
    // Emmet のスニペットで使用される変数
    "emmet.variables": {
        "lang": "ja" // Emmet で展開される HTML の言語を変更
    },
    /* ---window--- */
    // フォルダーを新しいウィンドウで開くか、最後のアクティブ ウィンドウを置き換えるかを制御します。
    "window.openFoldersInNewWindow": "on",
    // アクティブなエディターに基づいてウィンドウのタイトルを制御します。
    "window.title": "${activeEditorMedium}${separator}${rootName}",
    /* ---explorer--- */
    // ごみ箱を経由したファイル削除時にエクスプローラーが確認を求めるかどうかを制御します。
    "explorer.confirmDelete": false,
    // 貼り付けで重複するエクスプローラー項目に新しい名前を付けるときに使用する名前付け規則を制御します。
    "explorer.incrementalNaming": "smart",
    /* ---editor--- */
    // 他の修正候補と一緒にスニペットを表示するかどうか、およびその並び替えの方法を制御します。
    "editor.snippetSuggestions": "top",
    // エディターでインライン カラー デコレーターと色の選択を表示する必要があるかどうかを制御します。
    "editor.colorDecorators": false,
    // 構文ハイライトをクリップボードにコピーするかどうかを制御します。
    "editor.copyWithSyntaxHighlighting": false,
    // ドラッグ アンド ドロップによる選択範囲の移動をエディターが許可するかどうかを制御します。
    "editor.dragAndDrop": false,
    // 貼り付けた内容がエディターにより自動的にフォーマットされるかどうかを制御します。
    "editor.formatOnPaste": true,
    // ファイルを保存するときにフォーマットします。
    "editor.formatOnSave": true,
    // エディターで入力後に自動的に行のフォーマットを行うかどうかを制御します。
    "editor.formatOnType": true,
    // 表示するミニマップの最大幅を特定の列数に制限します。
    "editor.minimap.maxColumn": 60,
    // ミニマップ スライダーを表示するタイミングを制御します。
    "editor.minimap.showSlider": "always",
    // ミニマップのサイズを制御します。
    "editor.minimap.size": "fit",
    // 行にカラー ブロックではなく実際の文字を表示します。
    "editor.minimap.renderCharacters": false,
    // マウスを使用して複数のカーソルを追加するときに使用する修飾キーです。
    "editor.multiCursorModifier": "ctrlCmd",
    // ミニマップ スライダーを表示するタイミングを制御します。
    "editor.minimap.showSlider": "always",
    // エディターで制御文字を表示するかどうかを制御します。
    "editor.renderControlCharacters": true,
    // エディターで空白文字を表示するかどうかを制御します。
    "editor.renderWhitespace": "all",
    // とじしろのの折りたたみコントロールを表示するタイミングを制御します。
    "editor.showFoldingControls": "always",
    // 単語に関連したナビゲーションまたは操作を実行するときに、単語の区切り文字として使用される文字。
    "editor.wordSeparators": "`~!@#$%^&*()-=+[{]}\\|;:'\",.<>/?　、。！？「」【】『』（）",
    // 行の折り返し方法を制御します。
    "editor.wordWrap": "on",
    // エディターが現在の行をどのように強調表示するかを制御します。
    "editor.renderLineHighlight": "all",
    // 各言語に対して上書きされるエディター設定を構成します。
    "[csv]": {
        // 行の折り返し方法を制御します。
        "editor.wordWrap": "off"
    },
    "[json]": {
        // 他のすべてのフォーマッタ設定よりも優先される、既定のフォーマッタを定義します。
        "editor.defaultFormatter": "esbenp.prettier-vscode"
    },
    "[log]": {
        // 行の折り返し方法を制御します。
        "editor.wordWrap": "off"
    },
    "[python]": {
        // 1 つのタブに相当するスペースの数。
        "editor.tabSize": 2
    },
    "[tsv]": {
        // Tabキーで半角スペースを挿入
        "editor.insertSpaces": false,
        // 行の折り返し方法を制御します。
        "editor.wordWrap": "off"
    },
    /* ---debug--- */
    // デバッグ中にエディターの行内に変数値を表示します。
    "debug.inlineValues": true,
    // いつ内部デバッグ コンソールを開くかを制御します。
    "debug.internalConsoleOptions": "openOnSessionStart",
    // いつデバッグ ビューを開くかを制御します。
    "debug.openDebug": "openOnSessionStart",
    /* ---search--- */
    // 検索結果に行番号を表示するかどうかを制御します。
    "search.showLineNumbers": true,
    // フルテキスト検索および Quick Open でファイルやフォルダーを除外するための glob パターンを構成します。
    "search.exclude": {
        "**/tmp": true
    },
    /* ---files--- */
    // 既定の改行文字。
    "files.eol": "\n",
    //有効にすると、ファイルの保存時に最新の行を末尾に挿入します。
    "files.insertFinalNewline": true,
    // 有効にすると、ファイルの保存時に最終行以降の新しい行をトリミングします。
    "files.trimFinalNewlines": true,
    // 有効にすると、ファイルの保存時に末尾の空白をトリミングします。
    "files.trimTrailingWhitespace": true,
    // ファイルとフォルダーを除外するために glob パターンを構成します。
    "files.exclude": {
        // エクスプローラーから非表示にするファイル
        "**/*.map": true,
        "**/node_modules": true
    },
    /* ---terminal--- */
    // アクティブなターミナル セッションがある場合に、終了時に確認を行うかどうかを制御します。
    "terminal.integrated.confirmOnExit": true,
    // ターミナルで選択したテキストをクリップボードにコピーするかどうかを制御します。
    "terminal.integrated.copyOnSelection": true,
    /* ---workbench--- */
    // エディターに表示するラベルの書式を制御します。
    "workbench.editor.labelFormat": "short",
    // エディターのタブのサイズ設定を制御します。
    "workbench.editor.tabSizing": "shrink",
    // ワークベンチで使用されるファイル アイコン テーマを指定するか、ファイル アイコンを表示しないように 'null' を指定します。
    "workbench.iconTheme": "material-icon-theme",
    // 起動時にどのエディターを表示するかを制御します。無い場合、前のセッションを復元します。
    "workbench.startupEditor": "readme",
    /* ---html--- */
    // 再フォーマットしてはならないタグの、コンマ区切りの一覧。
    "html.format.unformatted": null,
    // コンテンツを再フォーマットしてはならないタグの、コンマ区切りの一覧。
    "html.format.contentUnformatted": "pre, code, textarea, title, h1, h2, h3, h4, h5, h6, p",
    // 直前に改行を 1 つ入れるタグの、コンマで区切られたリストです。
    "html.format.extraLiners": "",
    // 1 行あたりの最大文字数 (0 = 無効にする)。
    "html.format.wrapLineLength": 0,
    "editor.guides.bracketPairs": true,
    "remote.SSH.remotePlatform": {
        "AWS": "linux"
    },
    "files.watcherExclude": {
        "**": true
    },
    "workbench.editor.enablePreview": false,
    "[markdown]": {
        "editor.quickSuggestions": {
            "other": "on",
            "comments": "off",
            "strings": "off"
        },
        "editor.defaultFormatter": "DavidAnson.vscode-markdownlint"
    },
    "markdownlint.config": {
        "MD033": false
    },
    "editor.detectIndentation": false,
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "markdown.preview.breaks": true,
    "prettier.tabWidth": 4,
    "prettier.documentSelectors": ["markdown"]
}
```

<br>

## **拡張機能**

### **共通の拡張機能**

Code Spell Checker
Error Lens
Excel Viewer
Git Graph
Git History
GitLens — Git supercharged
indent-rainbow
Japanese Language Pack for Visual Studio Code
Live Server
Log File Highlighter
Markdown All in One
Material Icon Theme
Output Colorizer
Path Intellisence
Prettier - Code formatter
Remote Development
Rest Client
zenkaku

### **フロントエンドの拡張機能**（HTML,CSS,JavaScript向け）

Auto Close Tag
Auto Rename Tag
CSS Peek
ES7+ React/Redux/React-Native snippets
HTML CSS Suport

### **バックエンドの拡張機能**（Python向け）

autoDocstring - Python Docstring Generator
Pylance
Python
Jupyter
