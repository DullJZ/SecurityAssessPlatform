
from flask import Flask, request, jsonify

app = Flask(__name__)

def detect_sql_injection(url):
    sql_keywords = ['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'DROP', 'UNION', 'EXEC', 'TRUNCATE', 'OR', 'AND']
    # 提取URL中的参数
    params = url.split('?')
    if len(params) < 2:
        return False
    url = params[1]
    url = url.split('&')
    if len(url) < 2:
        return False
    for i in url:
        t = i.split('=')[1]
        for keyword in sql_keywords:
            if keyword in t.upper():
                print('SQL Injection detected!')
                return True
    return False

@app.route('/post', methods=['POST'])
def post():
    data = request.get_json()
    print(data['url'])
    if detect_sql_injection(data['url']):
        return jsonify({'status': 'hack'})
    else:
        return jsonify({'status': 'safe'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
