# from flask import Flask, render_template, request, redirect, url_for
#
# app = Flask(__name__)
#
# wishes = []
#
# @app.route('/letter')
# def letter():
#     return render_template('letter.html')
#
# @app.route('/')
# def home():
#     return render_template('index.html')
#
# @app.route('/gallery')
# def gallery():
#     return render_template('gallery.html')
#
# @app.route('/wishes', methods=['GET', 'POST'])
# def wish_page():
#     if request.method == 'POST':
#         name = request.form['name']
#         message = request.form['message']
#         wishes.append({'name': name, 'message': message})
#         return redirect(url_for('wish_page'))
#     return render_template('wishes.html', wishes=wishes)
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

wishes = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/letter')
def letter():
    return render_template('letter.html')

@app.route('/wishes', methods=['GET', 'POST'])
def wish_page():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        wishes.append({'name': name, 'message': message})
        return redirect(url_for('wish_page'))
    return render_template('wishes.html', wishes=wishes)

if __name__ == '__main__':
    app.run(debug=True)
