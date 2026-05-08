from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify({
        "id": user_id,
        "name": "John Doe",
        "email": "john@example.com"
    })

@app.route('/api/data', methods=['POST'])
def post_data():
    return jsonify({"status": "Data received", "code": 201}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
