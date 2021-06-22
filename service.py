from flask import url_for

@app.route('/')
def index():
    return render_template('home.html')
