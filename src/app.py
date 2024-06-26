from flask import Flask, request, jsonify
from flask_cors import CORS
from services.gpt_service import GPTService
from services.jira_service import JiraService

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize GPTService
gpt_service = GPTService()
jira_service = JiraService()

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    input_text = data.get('input_text')
    user_role = data.get('user_role')
    if not input_text:
        return jsonify({"error": "No input_text provided"}), 400
    
    response = gpt_service.get_structured_response(input_text, user_role)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
