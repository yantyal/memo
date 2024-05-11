import markdown
import sys

def convert_md_to_html(md_file_path, html_file_path):
    # Markdownファイルを読み込む
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    # MarkdownをHTMLに変換
    html_content = markdown.markdown(md_content)

    # HTMLテンプレートに変換された内容を挿入
    html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Markdown Document</title>
    <link rel="stylesheet" type="text/css" href="./style.css">
</head>
<body>
    {html_content}
    <div id="toast"></div>
    <script src="script.js"></script>
</body>
</html>
"""

    # 完成したHTMLをファイルに出力
    with open(html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_template)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用法: python script.py [Markdownファイルのパス] [HTMLファイルの出力パス]")
    else:
        convert_md_to_html(sys.argv[1], sys.argv[2])
