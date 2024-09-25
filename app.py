import json
from flask import Flask, jsonify
from question_loader import load_question_bank

app = Flask(__name__)

@app.route('/')
def get_questions():
    question_bank = load_question_bank('questions.json')
    # return jsonify(question_bank)  # Returns the entire question bank
    return jsonify(question_bank) # Returns the entire question bank

if __name__ == '__main__':
    app.run(debug=True)
