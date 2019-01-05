from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/rumi/')
def rumi():
    return render_template('rumi.html')

@app.route('/yeats/')
def yeats():
    return render_template('yeats.html')


if __name__ == '__main__':
    app.run(debug=True)

