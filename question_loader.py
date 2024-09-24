import json
import os
import random

def get_file_path(filename):
    base_dir = os.path.dirname(__file__)
    return os.path.join(base_dir, 'Utils', filename)

def load_json_file(filename):
    with open(get_file_path(filename), 'r') as file:
        return json.load(file)

def load_question_bank(filename):
    return load_json_file(filename)['questions']

def get_questions_by_category(category, question_bank):
    return [q for q in question_bank if q['category'] == category]

def validate_answer(question, user_answer):
    correct_option = question['options'].index(question['answer']) + 1
    return user_answer == chr(64 + correct_option)

def calculate_cognitive_score(results):
    return sum(result["is_correct"] for result in results)

def generate_feedback(score, total_questions):
    percentage = (score / total_questions) * 100
    if percentage == 100:
        return "Excellent job! You got all the answers correct. Keep up the great work!"
    elif percentage >= 75:
        return "Great job! You have a strong understanding of the material. Consider reviewing areas where you struggled."
    elif percentage >= 50:
        return "Good effort! You have a decent grasp, but there's room for improvement. Focus on the questions you missed."
    else:
        return "It seems you may need to review the material further. Don't be discouraged—practice will help you improve!"

def analyze_cognitive_results(results):
    total_questions = len(results)
    correct_answers = calculate_cognitive_score(results)
    incorrect_answers = total_questions - correct_answers
    strengths = [result['question'] for result in results if result['is_correct']]
    weaknesses = [result['question'] for result in results if not result['is_correct']]

    return {
        "total_questions": total_questions,
        "correct_answers": correct_answers,
        "incorrect_answers": incorrect_answers,
        "strengths": strengths,
        "weaknesses": weaknesses
    }

def calculate_skills_score(results):
    return sum(result['difficulty'] for result in results if result['is_correct'])

def generate_skills_feedback(score, total_difficulty):
    percentage = (score / total_difficulty) * 100
    if percentage == 100:
        return "Outstanding work! You demonstrated excellent skills."
    elif percentage >= 75:
        return "Great skills! You're well on your way to mastery."
    elif percentage >= 50:
        return "Good effort! Focus on the areas where you struggled."
    else:
        return "Consider reviewing the material to improve your skills."

def analyze_skills_results(results):
    total_questions = len(results)
    total_units = sum(result['difficulty'] for result in results)
    score = calculate_skills_score(results)
    incorrect_answers = total_questions - sum(result["is_correct"] for result in results)
    strengths = [result['question'] for result in results if result['is_correct']]
    weaknesses = [result['question'] for result in results if not result['is_correct']]

    return {
        "total_questions": total_questions,
        "total_units": total_units,
        "score": score,
        "incorrect_answers": incorrect_answers,
        "strengths": strengths,
        "weaknesses": weaknesses
    }

def present_questions(questions):
    results = []
    for idx, question in enumerate(questions, 1):
        print(f"Question {idx}: {question['question']}")
        for i, option in enumerate(question['options'], 1):
            print(f"{chr(64 + i)}. {option}")

        answer = input("Your answer (A/B/C/D): ").upper()
        while answer not in ['A', 'B', 'C', 'D']:
            answer = input("Invalid choice. Please enter A, B, C, or D: ").upper()

        is_correct = validate_answer(question, answer)
        results.append({
            "question": question['question'],
            "user_answer": answer,
            "correct_answer": question['answer'],
            "is_correct": is_correct,
            "difficulty": question.get('difficulty', 1)
        })

        print("Correct!\n" if is_correct else f"Wrong! The correct answer was {question['answer']}\n")
    
    return results

def save_results_to_json(results, filename):
    with open(get_file_path(filename), 'w') as file:
        json.dump(results, file, indent=4)

def main():
    """
    Main function to load questions, present them to the user, calculate scores, generate feedback,
    analyze results, and save the results to a JSON file.
    The function performs the following steps:
    1. Loads the question bank from a JSON file.
    2. Retrieves cognitive and skills questions from the question bank.
    3. Randomly selects a subset of cognitive and skills questions.
    4. Presents the selected questions to the user and collects their responses.
    5. Calculates the cognitive and skills scores based on the user's responses.
    6. Prints the cognitive and skills scores.
    7. Generates and prints feedback for cognitive and skills scores.
    8. Analyzes the cognitive and skills results and prints the analysis.
    9. Compiles the results into a dictionary.
    10. Saves the compiled results to a JSON file.
    Note: The function assumes the existence of the following helper functions:
    - load_question_bank(filepath)
    - get_questions_by_category(category, question_bank)
    - present_questions(questions)
    - calculate_cognitive_score(results)
    - calculate_skills_score(results)
    - generate_feedback(score, total_questions)
    - generate_skills_feedback(score, total_units)
    - analyze_cognitive_results(results)
    - analyze_skills_results(results)
    - save_results_to_json(results, filepath)
    """
    question_bank = load_question_bank('questions.json')
    cognitive_questions = get_questions_by_category("Cognitive", question_bank)
    skills_questions = get_questions_by_category("Skills", question_bank)

    selected_cognitive_questions = random.sample(cognitive_questions, 2)
    selected_skills_questions = random.sample(skills_questions, 2)

    # cognitive_results = present_questions(selected_cognitive_questions)
    # skills_results = present_questions(selected_skills_questions)

    # cognitive_score = calculate_cognitive_score(cognitive_results)
    # skills_score = calculate_skills_score(skills_results)

    # print(f"Your cognitive score is: {cognitive_score}/{len(selected_cognitive_questions)}")
    # print(f"Your skills score is: {skills_score}/{sum(q['difficulty'] for q in selected_skills_questions)}")

    # cognitive_feedback = generate_feedback(cognitive_score, len(selected_cognitive_questions))
    # skills_feedback = generate_skills_feedback(skills_score, sum(q['difficulty'] for q in selected_skills_questions))

    # print("\nCognitive Feedback:")
    # print(cognitive_feedback)

    # print("\nSkills Feedback:")
    # print(skills_feedback)

    # cognitive_analysis = analyze_cognitive_results(cognitive_results)
    # skills_analysis = analyze_skills_results(skills_results)

    # print("\nCognitive Analysis:")
    # print(f"Total Questions: {cognitive_analysis['total_questions']}")
    # print(f"Correct Answers: {cognitive_analysis['correct_answers']}")
    # print(f"Incorrect Answers: {cognitive_analysis['incorrect_answers']}")
    # print("Strengths: ", ", ".join(cognitive_analysis['strengths']) if cognitive_analysis['strengths'] else "None")
    # print("Weaknesses: ", ", ".join(cognitive_analysis['weaknesses']) if cognitive_analysis['weaknesses'] else "None")

    # print("\nSkills Analysis:")
    # print(f"Total Questions: {skills_analysis['total_questions']}")
    # print(f"Total Units: {skills_analysis['total_units']}")
    # print(f"Score: {skills_analysis['score']}")
    # print(f"Incorrect Answers: {skills_analysis['incorrect_answers']}")
    # print("Strengths: ", ", ".join(skills_analysis['strengths']) if skills_analysis['strengths'] else "None")
    # print("Weaknesses: ", ", ".join(skills_analysis['weaknesses']) if skills_analysis['weaknesses'] else "None")

    # results_compilation = {
    #     "cognitive": {
    #         "score": cognitive_score,
    #         "feedback": cognitive_feedback,
    #         "analysis": cognitive_analysis,
    #         "detailed_results": cognitive_results
    #     },
    #     "skills": {
    #         "score": skills_score,
    #         "feedback": skills_feedback,
    #         "detailed_results": skills_results
    #     }
    # }

    # save_results_to_json(results_compilation, 'phase1_results.json')

if __name__ == "__main__":
    main()
