from flask import Flask, request, jsonify

app = Flask(__name__)

# Global middlewares
@app.before_request
def logger():
    print(f"Incoming request: {request.method} {request.path}")


@app.route("/", methods=["GET"])
def home():
    return jsonify({
    "message": "Welcome to the home page!"
})


@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({
    "message": "Hello, world!"
})


@app.route("/user", methods=["POST"])
def user():
    return jsonify({
    "message": "User created successfully!"
})


if __name__ == "__main__":
    app.run(debug=True)
