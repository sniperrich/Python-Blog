# 在你的 Flask 应用中的相应视图函数中
from flask import Flask, render_template, request, url_for, flash, redirect, session
import markdown
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Get Good Get ErosSense'
@app.route('/your_route')
def your_view_function():
    # 假设 post['content'] 包含了 Markdown 格式的内容
    post_content_markdown = "# Hello, Markdown!"

    # 使用 Markdown 库将 Markdown 转换为 HTML
    post_content_html = markdown.markdown(post_content_markdown)

    # 渲染模板，并将转换后的 HTML 传递给模板
    return render_template('your_template.html', post_content_html=post_content_html)
if __name__ == '__main__':

    app.run(debug=True, host="127.0.0.1",port=5005)