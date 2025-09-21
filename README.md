# IELTS Writing Practice & Feedback Hub

A professional, AI-powered web application that provides instant feedback on IELTS Writing Task 1 and Task 2. Built by SparkSkyTech to help learners worldwide improve their writing skills through realistic band scoring, detailed analysis, and actionable improvement tips.


## 🚀 Live Demo

**Production URL**: [https://ielts-writing-app.onrender.com](https://ielts-writing-app.onrender.com)

> **Note**: App may take 30-60 seconds to load initially due to Render's free tier cold start.

## 📸 Screenshots

*Add screenshots of your app interface here to showcase the UI*

## ✨ Key Features

### 🎯 Core Functionality
- **Realistic Band Scoring**: AI assessment from 4.0–9.0 based on official IELTS criteria
- **Comprehensive Analysis**: Detailed feedback on Task Response, Coherence & Cohesion, Lexical Resource, and Grammatical Range & Accuracy
- **Model Answers**: Full high-scoring sample responses for each prompt
- **Progress Tracking**: Session-based tracking of attempts, scores, and improvement trends
- **PDF Export**: Professional downloadable reports with feedback and statistics

### 🎨 User Experience
- **Smart Prompt Selection**: 14+ curated IELTS Writing Task 2 prompts from recent exams
- **Real-time Word Counter**: Live validation for minimum word requirements (150/250 words)
- **Dark/Light Mode**: Toggle between themes with persistent preferences
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- **Auto-save Progress**: Session-based progress tracking without registration

### 📚 Learning Resources
- **Integrated Video Tutorials**: Embedded YouTube lessons for writing improvement
- **Comprehensive Resource Hub**: Organized links to official IELTS materials
- **External Expert Resources**: Curated connections to British Council, IDP, Cambridge English
- **Social Learning**: Links to IELTS community groups and forums

## 🛠 Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Flask 3.0.0 (Python) |
| **AI Engine** | OpenAI GPT-3.5-turbo API |
| **Frontend** | HTML5, CSS3, JavaScript ES6 |
| **PDF Generation** | WeasyPrint |
| **Deployment** | Render.com |
| **Version Control** | Git/GitHub |
| **Environment** | python-dotenv |

## 🎯 Target Audience

- **IELTS Candidates**: Preparing for Academic or General Training modules
- **Self-Study Learners**: Seeking instant, detailed writing feedback
- **Educators**: Teachers and tutors using AI-assisted assessment tools
- **Institutions**: Schools integrating digital writing practice tools

## 📊 What You Get

Each submission provides:
- ✅ **Official Band Score** based on IELTS rubric
- ✅ **Detailed Strengths** analysis
- ✅ **Areas for Improvement** with specific examples
- ✅ **Actionable Tips** for score enhancement
- ✅ **Complete Model Answer** (Band 8+ quality)
- ✅ **Downloadable PDF Report** with progress statistics
- ✅ **Resource Recommendations** for continued learning

## 🚦 Getting Started

### For Users

1. **Visit the App**: [https://ielts-writing-app.onrender.com](https://ielts-writing-app.onrender.com)
2. **Select Task Details**: Choose Academic/General and Task 1/2
3. **Choose or Enter Prompt**: Use provided prompts or paste your own
4. **Write Your Response**: Minimum 150 words (Task 1) or 250 words (Task 2)
5. **Get Instant Feedback**: AI analysis with band score and improvement tips
6. **Download PDF**: Save your report for future reference
7. **Track Progress**: View your improvement over time

### For Developers

#### Prerequisites
- Python 3.11+
- OpenAI API key
- Git

#### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Anfal-AR/ielts-writing-app.git
   cd ielts-writing-app
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Open browser**: Navigate to `http://localhost:5000`

#### Environment Variables

Create a `.env` file with:
```env
OPENAI_API_KEY=your_openai_api_key_here
FLASK_ENV=development
FLASK_DEBUG=True
```

## 📁 Project Structure

```
ielts-writing-app/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── runtime.txt              # Python version for deployment
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
├── README.md                # Project documentation
├── LICENSE                  # MIT License
├── prompts.json             # IELTS writing prompts data
├── submissions.csv          # User submissions log
├── templates/               # HTML templates
│   ├── index.html          # Main application interface
│   └── error.html          # Error page template
├── static/                  # Static assets
│   ├── css/
│   │   └── styles.css      # Application styles
│   ├── images/
│   │   └── SparkSkyTech.png # Logo
│   └── js/
│       └── main.js         # JavaScript functionality
└── docs/                    # Documentation files
    └── User_Guide.md        # User guide
```

## 🔧 Configuration

### OpenAI API Setup
1. Sign up at [OpenAI Platform](https://platform.openai.com)
2. Generate an API key
3. Add to environment variables or Render dashboard

### Deployment on Render
1. Connect your GitHub repository
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `gunicorn app:app`
4. Add environment variable: `OPENAI_API_KEY`

## 📈 Usage Analytics

The app tracks (anonymously):
- Number of submissions
- Task type distribution
- Average processing time
- User session duration

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Reporting Issues
- Use GitHub Issues for bug reports
- Include error messages and steps to reproduce
- Specify browser and device information

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgments

- **OpenAI**: For providing the GPT-3.5-turbo API
- **British Council & IDP**: For IELTS assessment criteria
- **IELTS Community**: For feedback and testing
- **Open Source Libraries**: Flask, WeasyPrint, and other dependencies

## 🔗 Related Projects

- **[IELTS Study Plan Generator](https://www.sparkskytech.com/ielts)**: Personalized study planning tool
- **[SparkSkyTech Blog](https://www.sparkskytech.com/blog/ielts_blogs)**: IELTS tips and strategies
- **[YouTube Channel](https://www.youtube.com/@SparkSkyTech)**: Video tutorials and lessons

## 📞 Support & Contact

- **Website**: [www.sparkskytech.com](https://www.sparkskytech.com)
- **YouTube**: [@SparkSkyTech](https://www.youtube.com/@SparkSkyTech)
- **GitHub**: [@Anfal-AR](https://github.com/Anfal-AR)
- **Issues**: [GitHub Issues](https://github.com/Anfal-AR/ielts-writing-app/issues)

## 🚀 Roadmap

- [ ] User accounts and authentication
- [ ] Extended progress analytics
- [ ] Mobile app version
- [ ] Multi-language interface support
- [ ] Batch processing for educators
- [ ] API endpoint for third-party integrations

---

**Made with ❤️ by [SparkSkyTech](https://www.sparkskytech.com) for the global IELTS learning community.**

*This project is completely free and open-source, supporting accessible education worldwide.*
