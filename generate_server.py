import json

# function to create the server code based on the config
def generate_server_code(config):
    code = '''from flask import Flask, request, jsonify

app = Flask(__name__)

# Global middlewares
@app.before_request
def logger():
    print(f"Incoming request: {request.method} {request.path}")
'''

    for route in config['routes']:
        method = route['method']
        path = route['path']
        response = json.dumps(route['response'], indent=4)

        code += f'''

@app.route("{path}", methods=["{method}"])
def {path.strip('/').replace('/', '_') or 'home'}():
    return jsonify({response})
'''

    code += '''

if __name__ == "__main__":
    app.run(debug=True)
'''
    return code

# main driver
def main():
    with open('config.json') as file:
        config = json.load(file)

    server_code = generate_server_code(config)

    with open('server.py', 'w') as server_file:
        server_file.write(server_code)

    print("✅ Server code successfully generated in 'server.py'!")

if __name__ == "__main__":
    main()
