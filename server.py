from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html', number=3, color="#9EC5F8")

@app.route('/play/<int:num>')
def play_num(num):
    return render_template('index.html', number=num, color="#9EC5F8")

@app.route('/play/<int:num>/<string:color>')
def play_numColor(num,color):
    return render_template('index.html', number=num, color=color)

if __name__=="__main__":
    app.run(debug=True)