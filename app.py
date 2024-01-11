from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/execute_command', methods=['POST'])
def execute_command():
    command = request.form['command']
    result = subprocess.check_output(command, shell=True, text=True)
    return result

if __name__ == '__main__':
    app.run(debug=True)
