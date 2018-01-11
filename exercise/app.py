from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    user_data = request.json
    exponent = int(user_data['exponent'])
    result = _exponentiate(exponent)
    return jsonify({'answer': result})

def _exponentiate(exponent):
    return 10 ** exponent


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
