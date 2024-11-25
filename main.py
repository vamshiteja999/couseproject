from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('index.html')

@app.route('/privacy')
def privacy():
    return render_template('index.html')

@app.route('/terms')
def terms():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)