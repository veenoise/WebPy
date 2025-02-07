from flask import Flask, request, jsonify
from lexer import Token
from flask_cors import CORS
from parser import Parser

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def home():
    data = request.data
    
    tokenizer = Token(data)
    tokenizer.tokenize()

    parser = Parser(tokenizer.token_list)
    syntax_error = parser.parse()

    return jsonify({
        "token_list": tokenizer.token_list, 
        "error": tokenizer.error,
        "syntax_error": syntax_error
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)