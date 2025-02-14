from flask import Flask, jsonify, request
from flask_cors import CORS
from google.cloud import translate_v2 as translate

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})  # CORS設定を更新

@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'Flask start!'})

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify(message='Hello World by Flask')

@app.route('/api/multiply/<int:id>', methods=['GET'])
def multiply(id):
    print("multiply")
    # idの2倍の数を計算
    doubled_value = id * 2
    return jsonify({"doubled_value": doubled_value})

@app.route('/api/echo', methods=['POST'])
def echo():
    print("echo")
    data = request.get_json()  # JSONデータを取得
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    # 'message' プロパティが含まれていることを確認
    message = data.get('message', 'No message provided')
    return jsonify({"message": f"echo: {message}"})

@app.route('/api/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text_to_translate = data['text']

    # 日本語から英語への翻訳を実行
    result = translate_client.translate(text_to_translate, target_language='en')

    return jsonify({"translated_text": result['translatedText']})

if __name__ == '__main__':
    app.run(debug=True)
