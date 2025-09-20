import json
from weasyprint import HTML
import os

# Load prompts
with open("prompts.json", "r", encoding="utf-8") as f:
    prompt_data = json.load(f)
    prompts_list = prompt_data["prompts"]

# Build HTML content
html_content = """
<h1>IELTS Writing Task 2 – 14 High-Scoring Model Answers</h1>
<p>Practice with real IELTS-style prompts and sample Band 8+ essays.</p>
"""

for prompt in prompts_list:
    html_content += f"""
    <div style="page-break-after: always;">
        <h2>{prompt['title']}</h2>
        <p><strong>Prompt:</strong> {prompt['prompt']}</p>
        <hr>
        <p><strong>Model Answer:</strong></p>
        <pre>{prompt['model_answer']}</pre>
    </div>
    """

# Generate PDF
HTML(string=html_content).write_pdf("model_answers_freebie.pdf")
print("✅ Generated 'model_answers_freebie.pdf'")