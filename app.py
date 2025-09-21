from flask import Flask, render_template, request, send_file, jsonify, session
import openai
import os
from dotenv import load_dotenv
import json
import csv
import datetime
from weasyprint import HTML
import tempfile
import secrets

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Load prompts from JSON
try:
    with open("prompts.json", "r", encoding="utf-8") as f:
        prompt_data = json.load(f)
        prompts_list = prompt_data["prompts"]
except FileNotFoundError:
    prompts_list = []
    print("Warning: prompts.json not found. Using empty prompts list.")

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

def word_count(text):
    return len(text.strip().split())

def get_band_score_from_feedback(feedback):
    """Extract band score from feedback text"""
    try:
        if "Band Score:" in feedback:
            line = feedback.split("Band Score:")[1].split("\n")[0].strip()
            # Extract numeric score
            score_str = ''.join(c for c in line if c.isdigit() or c == '.')
            return float(score_str) if score_str else 0.0
    except:
        pass
    return 0.0

def update_user_progress(band_score, task_type, task_number):
    """Update user progress in session"""
    if 'progress' not in session:
        session['progress'] = {
            'attempts': 0,
            'best_score': 0.0,
            'avg_score': 0.0,
            'scores': [],
            'task_1_attempts': 0,
            'task_2_attempts': 0,
            'academic_attempts': 0,
            'general_attempts': 0
        }
    
    progress = session['progress']
    progress['attempts'] += 1
    progress['scores'].append(band_score)
    progress['best_score'] = max(progress['best_score'], band_score)
    progress['avg_score'] = sum(progress['scores']) / len(progress['scores'])
    
    # Update specific counters
    if task_number == "1":
        progress['task_1_attempts'] += 1
    else:
        progress['task_2_attempts'] += 1
        
    if task_type == "Academic":
        progress['academic_attempts'] += 1
    else:
        progress['general_attempts'] += 1
    
    session['progress'] = progress
    session.modified = True

def get_gpt_feedback(prompt_text, user_writing, task_number, task_type):
    system_prompt = f"""
You are an experienced IELTS Writing Examiner. Evaluate the following Task {task_number} ({task_type}) response using official IELTS scoring criteria:
- Task Response / Achievement
- Coherence & Cohesion
- Lexical Resource
- Grammatical Range & Accuracy

Provide a realistic Band Score from 4.0 to 9.0 — do NOT limit yourself to 6.0–7.5.
If the writing is clearly below standard, feel free to give lower scores (e.g., 5.0 or 4.5).
If the writing is exceptional, don't hesitate to give higher scores (8.0, 8.5, or even 9.0).

Also provide:
- Strengths: What was done well?
- Weaknesses: Where improvements are needed
- Improvement Tips: Practical suggestions
- A full model answer that reflects high-scoring writing style and length

User Prompt: {prompt_text}
User Writing: {user_writing}

Return your response in exactly this format:

Band Score: [score]

Strengths:
- [point 1]
- [point 2]
- [point 3]

Weaknesses:
- [point 1]
- [point 2]
- [point 3]

Improvement Tips:
- [tip 1]
- [tip 2]
- [tip 3]

Model Answer:
[full model answer here - write a complete, high-scoring response of appropriate length]

📚 Useful Resources:
📌 Official IELTS Info: https://www.ielts.org
📘 British Council – Skills Practice: https://learnenglish.britishcouncil.org/skills
📝 IDP IELTS Guides: https://www.ieltsidpindia.com/information/prepare-for-ielts
🎯 IELTS Liz – Expert Tips: https://ieltsliz.com
📘 SparkSkyTech IELTS Hub: https://www.sparkskytech.com/ielts
📱 IELTS Study Plan Generator (Free App): https://www.sparkskytech.com/apps/ielts-study-plan-generator
📄 Free Model Answers: https://www.sparkskytech.com/ielts/ielts-free-resources
🎥 Watch Video Lessons: https://www.youtube.com/@SparkSkyTech
🛒 Digital Study Tools: https://www.sparkskytech.com/shop/learning-education  

"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_writing}
            ],
            max_tokens=1500,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Error getting feedback: {str(e)}. Please check your OpenAI API key and internet connection."

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    writing = ""
    task_type = "Academic"
    task_number = "1"
    prompt_text = ""
    word_count_result = 0

    if request.method == "POST":
        writing = request.form.get("writing", "")
        task_type = request.form.get("task_type", "Academic")
        task_number = request.form.get("task_number", "1")
        prompt_select = request.form.get("prompt_select", "")
        prompt_text = prompt_select or request.form.get("prompt_text", "")

        word_count_result = word_count(writing)
        min_words = 250 if task_number == "2" else 150

        if word_count_result < min_words:
            result = f"⚠️ Please write at least {min_words} words for Task {task_number}. Current word count: {word_count_result}"
        else:
            result = get_gpt_feedback(prompt_text, writing, task_number, task_type)
            
            # Update progress tracking
            band_score = get_band_score_from_feedback(result)
            if band_score > 0:
                update_user_progress(band_score, task_type, task_number)

            # Save submission to CSV
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                with open("submissions.csv", "a", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow([timestamp, task_type, task_number, prompt_text[:100], writing[:100], word_count_result, band_score])
            except Exception as e:
                print(f"Error saving to CSV: {e}")

    return render_template(
        "index.html",
        writing=writing,
        task_type=task_type,
        task_number=task_number,
        prompt_text=prompt_text,
        result=result,
        prompts=prompts_list,
        word_count=word_count_result,
        progress=session.get('progress', None)
    )

@app.route("/progress")
def progress():
    """API endpoint to get user progress"""
    return jsonify(session.get('progress', {
        'attempts': 0,
        'best_score': 0.0,
        'avg_score': 0.0,
        'scores': [],
        'task_1_attempts': 0,
        'task_2_attempts': 0,
        'academic_attempts': 0,
        'general_attempts': 0
    }))

@app.route("/reset_progress")
def reset_progress():
    """Reset user progress"""
    session.pop('progress', None)
    return jsonify({'status': 'success'})

@app.route("/download", methods=["POST"])
def download():
    result = request.form.get("result", "")
    prompt_text = request.form.get("prompt_text", "")
    writing = request.form.get("writing", "")
    task_type = request.form.get("task_type", "Academic")
    task_number = request.form.get("task_number", "1")

    # Extract Band Score
    band_score = "Not available"
    if result.startswith("Band Score:"):
        band_score = result.splitlines()[0]

    # Get current progress
    progress = session.get('progress', {})
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="UTF-8">
        <style>
          body {{
            font-family: 'Arial', sans-serif;
            padding: 30px;
            background: #ffffff;
            color: #333;
            line-height: 1.6;
          }}
          .header {{
            text-align: center;
            border-bottom: 3px solid #667eea;
            padding-bottom: 20px;
            margin-bottom: 30px;
          }}
          h1 {{
            color: #667eea;
            font-size: 28px;
            margin-bottom: 10px;
          }}
          .subtitle {{
            color: #666;
            font-size: 16px;
          }}
          .score-highlight {{
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            margin: 20px 0;
          }}
          .section {{
            margin: 25px 0;
            padding: 20px;
            background: #f9f9f9;
            border-left: 4px solid #667eea;
            border-radius: 5px;
          }}
          .section h2 {{
            color: #667eea;
            font-size: 20px;
            margin-bottom: 15px;
          }}
          .writing-content {{
            background: white;
            padding: 15px;
            border-radius: 5px;
            border: 1px solid #ddd;
          }}
          .feedback-content {{
            white-space: pre-wrap;
            background: white;
            padding: 15px;
            border-radius: 5px;
            border: 1px solid #ddd;
            font-family: 'Courier New', monospace;
            line-height: 1.8;
          }}
          .progress-stats {{
            display: flex;
            justify-content: space-around;
            background: #f0f4ff;
            padding: 15px;
            border-radius: 10px;
            margin: 20px 0;
          }}
          .stat {{
            text-align: center;
          }}
          .stat-number {{
            font-size: 24px;
            font-weight: bold;
            color: #667eea;
          }}
          .stat-label {{
            font-size: 12px;
            color: #666;
          }}
          .footer {{
            margin-top: 40px;
            text-align: center;
            color: #888;
            border-top: 1px solid #ddd;
            padding-top: 20px;
          }}
          .logo {{
            color: #667eea;
            font-weight: bold;
            font-size: 18px;
          }}
        </style>
      </head>
      <body>
        <div class="header">
          <h1>IELTS Writing Feedback Report</h1>
          <div class="subtitle">AI-Powered Analysis by SparkSkyTech</div>
        </div>

        <div class="score-highlight">
          {band_score}
        </div>

        <div class="progress-stats">
          <div class="stat">
            <div class="stat-number">{progress.get('attempts', 0)}</div>
            <div class="stat-label">Total Attempts</div>
          </div>
          <div class="stat">
            <div class="stat-number">{progress.get('best_score', 0):.1f}</div>
            <div class="stat-label">Best Score</div>
          </div>
          <div class="stat">
            <div class="stat-number">{progress.get('avg_score', 0):.1f}</div>
            <div class="stat-label">Average Score</div>
          </div>
        </div>

        <div class="section">
          <h2>📝 Task Details</h2>
          <p><strong>Task Type:</strong> {task_type}</p>
          <p><strong>Task Number:</strong> {task_number}</p>
          <p><strong>Word Count:</strong> {word_count(writing)} words</p>
          <p><strong>Date:</strong> {datetime.datetime.now().strftime("%B %d, %Y at %H:%M")}</p>
        </div>

        <div class="section">
          <h2>❓ Prompt</h2>
          <div class="writing-content">{prompt_text}</div>
        </div>

        <div class="section">
          <h2>✍️ Your Writing</h2>
          <div class="writing-content">{writing}</div>
        </div>

        <div class="section">
          <h2>🎯 Detailed Feedback</h2>
          <div class="feedback-content">{result}</div>
        </div>

        <div class="footer">
          <div class="logo">SparkSkyTech IELTS Writing Practice Hub</div>
          <p>Continue your IELTS journey at <strong>www.sparkskytech.com/ielts</strong></p>
          <p><small>Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</small></p>
        </div>
      </body>
    </html>
    """

    try:
        temp_dir = tempfile.gettempdir()
        pdf_path = os.path.join(temp_dir, f"ielts_feedback_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf")
        
        HTML(string=html_content).write_pdf(pdf_path)
        return send_file(pdf_path, as_attachment=True, download_name="ielts_writing_feedback.pdf")
    except Exception as e:
        return f"Error generating PDF: {str(e)}", 500

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error="Page not found"), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error="Internal server error"), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=False)