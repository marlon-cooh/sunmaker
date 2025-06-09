from flask import Flask, jsonify #type: ignore
from flask_cors import CORS # type: ignore

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r"/*": {"origins": "*" }})
# CORS(app, resources={r"/*": {
#     "origins": "http://localhost:8080", 
#     "allow_headers" : "Access-Control-Allow-Origin"
#         }
#     }
# )

@app.route('/', methods=['GET'])
def greetings():
    return ("Hello, World! This is the backend of the application.", 200)

@app.route('/shark', methods=['GET'])
def shark():
    return "Baby Shark, doo doo! 🦈🦈🦈", 200

if __name__ == '__main__':
    app.run(debug=True)
