import re
import sys
import os
import argparse


def generate_version_checker():
    # 1. コマンドライン引数の設定
    parser = argparse.ArgumentParser(description="Pyxel HTMLから実行環境のバージョンを調査するHTMLを生成します")
    parser.add_argument("input_file", help="調査対象のHTMLファイル（app2htmlの出力など）")
    args = parser.parse_args()

    # 入力ファイルの存在確認
    if not os.path.exists(args.input_file):
        print(f"Error: ファイル '{args.input_file}' が見つかりません。")
        sys.exit(1)

    # 2. 出力ファイル名の生成 (hoge.html -> hoge_version_check.html)
    base, _ = os.path.splitext(args.input_file)
    output_file = f"{base}_version_check.html"

    # 3. 入力ファイルの読み込み
    with open(args.input_file, "r", encoding="utf-8") as f:
        user_html_content = f.read()

    # 4. pyxel.js のURLを抽出
    js_match = re.search(r'src="([^"]*?/pyxel\.js)"', user_html_content)
    if not js_match:
        print("Error: HTML内に pyxel.js の script タグが見つかりません。")
        sys.exit(1)

    pyxel_url = js_match.group(1)

    # 5. 調査用HTMLの構築
    checker_html = f"""<!DOCTYPE html>
<html>
<body>
    <div id="out">Loading runtime info...</div>
    <script type="module">
        const out = document.getElementById('out');
        try {{
            const res = await fetch('{pyxel_url}');
            const code = await res.text();
            const pyoMatch = code.match(/PYODIDE_URL\\s*=\\s*"(.*?)"/);
            if (!pyoMatch) throw new Error("PYODIDE_URL not found");
            
            const pyodideJsUrl = pyoMatch[1];
            const pyodideMjsUrl = pyodideJsUrl.replace("pyodide.js", "pyodide.mjs");

            const {{ loadPyodide }} = await import(pyodideMjsUrl);
            const pyodide = await loadPyodide();
            const pyFullVer = pyodide.runPython("import sys; sys.version");

            out.innerHTML = `
                <p>Pyxel: {pyxel_url}</p>
                <p>Pyodide: ${{pyodideJsUrl}}</p>
                <p>Python: ${{pyFullVer.split(" ")[0]}}</p>
            `;
        }} catch (err) {{
            out.innerText = "Error: " + err.message;
        }}
    </script>
</body>
</html>"""

    # 6. 書き出し
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(checker_html)

    print(f"Success: {output_file} を生成しました。")


if __name__ == "__main__":
    generate_version_checker()
