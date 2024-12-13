from flask import Flask, request, jsonify
from lexer import Token
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def home():
    data = request.data
    
    tokenizer = Token(data)
    tokenizer.tokenize()

    return jsonify({
        "token_list": tokenizer.token_list, 
        "error": tokenizer.error
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)