from flask import Flask, render_template, request
import code_to_algorithm  # Import your algorithm conversion module

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', code="", algorithm="")
@app.route('/about')
def about():
    return render_template('register.html')
@app.route('/', methods=['POST'])
def process_code():
    code = request.form['code']
    algorithm = []

    try:
        algorithm = code_to_algorithm.convert_to_algorithm(code.splitlines())  # Convert code to lines
    except Exception as e:
        algorithm = [f"Error: {str(e)}"]

    return render_template('index.html', code=code, algorithm=algorithm)

if __name__ == '__main__':
    app.run(debug=True)
