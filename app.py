import json
import os
from flask import Flask, jsonify
from question_loader import load_question_bank

app = Flask(__name__)

@app.route('/')
def get_questions():
    question_bank = load_question_bank('questions.json')
    # return jsonify(question_bank)  # Returns the entire question bank
    return jsonify(question_bank) # Returns the entire question bank

# @app.route('/cognitive')
# def get_cognitive_questions():
#     question_bank = load_question_bank('questions.json')
#     cognitive_questions = get_questions_by_category("Cognitive", question_bank)
#     return jsonify(cognitive_questions)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use the port from the environment or default to 5000
    app.run(host='0.0.0.0', port=port)
