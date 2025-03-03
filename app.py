from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Get the JSON payload from Freshworks
    print("Received data:", data)  # Log the request

    response = {
        "message": "Webhook received successfully",
        "received_data": data
    }
    return jsonify(response), 200  # Return a success response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
