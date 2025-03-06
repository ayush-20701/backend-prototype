from flask import Flask, request, jsonify
app = Flask(__name__) # create an instance of the Flask class
@app.route('/')
def home():
    return 'Welcome to my prototype API'
@app.route('/hello')
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route('/sum')
def sum_numbers():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        return jsonify({"sum": num1 + num2})
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide numbers."}), 400
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # Specify host and port