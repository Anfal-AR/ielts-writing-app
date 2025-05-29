from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

def get_gpt_feedback(prompt_text, user_writing, task_number, task_type):
    """Send prompt + user writing to GPT for feedback"""
    system_prompt = f"""
You are an IELTS Writing Examiner. Evaluate the following Task {task_number} ({task_type}) response.
Score it on the IELTS band scale (0–9), and give detailed feedback.

Return your response in this format:

Band Score: [score]
Strengths: [list of strengths]
Weaknesses: [list of weaknesses]
Model Answer: [a full model answer for this prompt]
Improvement Tips: [tips for improvement]
Resources: [suggest 2–3 useful websites/books for IELTS writing]

User Prompt: {prompt_text}
User Writing: {user_writing}
"""

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error getting feedback: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_writing = request.form["writing"]
        task_type = request.form["task_type"]
        task_number = request.form["task_number"]
        prompt_text = request.form.get("prompt_text", "Describe the chart below.")

        result = get_gpt_feedback(prompt_text, user_writing, task_number, task_type)

        return render_template("index.html",
                               writing=user_writing,
                               task_type=task_type,
                               task_number=task_number,
                               prompt_text=prompt_text,
                               result=result)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)