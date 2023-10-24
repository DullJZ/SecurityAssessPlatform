from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def api():
    print("Score got!")
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(port=15001)