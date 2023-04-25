from flask import Flask, render_template

app = Flask(__name__)

@app.route("/music")
def music():
    return render_template('music.html')

if __name__ == '__main__':
    app.run()