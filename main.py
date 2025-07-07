from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/meu-webhook', methods=['POST'])
def receber_webhook():
    print("Headers:", dict(request.headers))
    print("Raw data:", request.data)
    print("JSON:", request.get_json(silent=True))
    return jsonify({"status": "recebido"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)