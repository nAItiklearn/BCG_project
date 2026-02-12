from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot_adapter import ChatbotJSONAdapter

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

bot = ChatbotJSONAdapter()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    query = data.get('query', '')
    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    response = bot.process_query_json(query)
    return jsonify(response)

if __name__ == '__main__':
    print("Starting Flask API server on port 5000...")
    app.run(port=5000, debug=True)
