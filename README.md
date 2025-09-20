# IELTS Writing Practice & Feedback Hub

A professional, AI-powered web application that provides instant feedback on IELTS Writing Task 1 (Letters) and Task 2 (Essays). Built by SparkSkyTech to help learners worldwide improve their writing skills through realistic band scoring, model answers, and actionable tips.

## 🌟 Features

### Core Functionality
- **Instant Band Score Estimation**: Realistic scores from 4.0–9.0 based on official IELTS criteria
- **AI-Powered Feedback**: Detailed analysis of Task Response, Coherence, Lexical Resource, and Grammar
- **Model Answer Generation**: Full high-scoring responses tailored to each prompt
- **Progress Tracking**: Browser-based session tracking for attempts, best score, average score, and task history
- **Dark Mode Toggle**: User-friendly interface with light/dark theme support

### Interactive Experience
- **Prompt Selection Dropdown**: Choose from 14+ common IELTS Writing Task 2 prompts
- **Word Count Tracker**: Real-time word count with validation (150+ for Task 1, 250+ for Task 2)
- **YouTube Integration**: Embedded video tutorials for skill improvement
- **Free Downloadable PDF Reports**: Save feedback for offline review and study

### Comprehensive Learning Resources
- **Skill-Based Footer**: Official links organized by Listening, Reading, Writing, Speaking, Vocabulary, and more
- **Trusted Sources**: Curated links to British Council, IDP, IELTS Liz, Cambridge, and other expert sites
- **Facebook Community Access**: Join a global group of IELTS learners for peer support

## 🚀 Live Demo

**Production URL**:(https://ielts-writing-app.onrender.com)

## 🛠 Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **AI Engine**: OpenAI API (`gpt-3.5-turbo`) via `openai` Python library
- **PDF Generation**: WeasyPrint (server-side rendering)
- **Styling**: Responsive CSS with dark mode toggle using `localStorage`
- **Deployment**: Render.com (Web Service)
- **Version Control**: Git/GitHub
- **Environment Management**: `.env` + `python-dotenv`

## 📱 Responsive Design

The application is fully responsive and optimized for:
- Desktop computers (1920px+)
- Tablets (768px - 1024px)
- Mobile phones (320px - 767px)
- All modern browsers (Chrome, Firefox, Edge, Safari)

## 🎯 Target Users

- IELTS test candidates preparing for Academic or General Training modules
- Self-study learners seeking instant feedback
- Teachers and tutors looking for AI-assisted grading tools
- Educational institutions integrating digital writing practice

## 📋 Feedback Report Includes

Each submission generates:
- **Band Score**: Based on official IELTS rubric
- **Strengths**: What was done well
- **Weaknesses**: Areas needing improvement
- **Improvement Tips**: Actionable suggestions
- **Full Model Answer**: Band 8+ sample response
- **Downloadable PDF**: With progress stats and date stamp

## 🌐 Comprehensive IELTS Resources

Integrated directly in the footer:
- **Official Sites**: British Council, IDP, IELTS.org
- **Writing Tips**: IELTS Liz, Cambridge English
- **Free Tools**: SparkSkyTech's blog, YouTube channel, Facebook group
- **Vocabulary & Grammar**: Dedicated sections with direct links

## 🚦 Getting Started

### For Users
1. Visit (https://ielts-writing-app.onrender.com)
2. Select Task Type (Academic/General) and Task Number (1 or 2)
3. Enter or select a writing prompt
4. Write your essay or letter (min. 150/250 words)
5. Click "Get Feedback"
6. Review AI-generated feedback and model answer
7. Download as PDF for future reference

### For Developers
1. Clone the repository:
   ```bash
   git clone https://github.com/Anfal-AR/ielts-writing-app.git
   cd ielts-writing-app
