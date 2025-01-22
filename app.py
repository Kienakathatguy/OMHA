from flask import Flask, render_template, request

app = Flask(__name__)

# Route chính cho việc ghi nhật ký
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Lấy nội dung từ form
        entry = request.form.get('entry')
        # Lưu tạm nội dung vào file text (hoặc cơ sở dữ liệu sau này)
        with open('entries.txt', 'a') as f:
            f.write(f"{entry}\n")
        return "Đã lưu nhật ký thành công!"
    return '''
        <h1>Nhật ký tâm sự</h1>
        <form method="POST">
            <textarea name="entry" placeholder="Viết những tâm sự tại đây..." rows="5" cols="50"></textarea><br>
            <button type="submit">Lưu</button>
        </form>
    '''

if __name__ == '__main__':
    port = os.environ.get("PORT", 5000)
    app.run(debug=True, host="0.0.0.0", port=int(port))
