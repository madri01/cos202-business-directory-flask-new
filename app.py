from flask import Flask, render_template, request, redirect, url_for
from models import Directory

app = Flask(__name__)
directory = Directory()

@app.route('/')
def home():
    return render_template('home.html', recent=directory.get_recent_businesses(), total=directory.total)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    category = request.form.get('category')
    description = request.form.get('description')
    if name and category and description:
        directory.add_business(name, category, description)
        return render_template('confirmation.html', business=directory.businesses[-1])
    return redirect(url_for('add'))
# Global Directory instance for Stack
if __name__ == '__main__':
    app.run(debug=false)
