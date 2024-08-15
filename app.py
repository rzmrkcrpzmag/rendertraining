from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    result_age = 0
    if request.method == 'POST':
        try:
            age = int(request.form['age'])
            result_age = age + 6
        except ValueError:
            result_age = ""
            
    return render_template("index.html", age=result_age)


if __name__ == '__main__':
  app.run(debug=True)
