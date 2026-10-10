# PySpark Practice App

An interactive Streamlit application for practicing PySpark questions with instant feedback and code execution.

## Features

- 🎯 Multiple choice questions on PySpark fundamentals
- 💻 Interactive code challenges with live execution
- 📊 Score tracking
- ⚡ Instant feedback and explanations
- 🔄 Quiz reset functionality

## Prerequisites

- Python 3.8+
- Java 8 or higher (required for PySpark)

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sufaila/pyspark-practice-app.git
cd pyspark-practice-app
```

### 2. Create Virtual Environment

**On Mac/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**On Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

## Usage

1. Answer multiple choice questions by selecting an option and clicking "Submit Answer"
2. Solve code challenges by writing PySpark code in the editor
3. Click "Run Code" to execute and validate your solution
4. Your score updates automatically
5. Click "Reset Quiz" to start over

## Project Structure

```
pyspark-practice-app/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .gitignore         # Git ignore rules
```

## Question Types

### Multiple Choice (MCQ)
- Test your understanding of PySpark concepts
- Get explanations after each answer

### Code Challenges
- Write actual PySpark code
- Execute against live Spark session
- Get feedback on your solution

## Next Steps

Enhance the app with:
- More question categories (Joins, Aggregations, Window Functions, RDDs)
- Difficulty levels (Beginner, Intermediate, Advanced)
- Progress tracking with SQLite
- User authentication and leaderboard
- Question explanations with code examples
- Time limits and performance metrics

## Troubleshooting

**Java error?**
- Install Java 8+: https://www.java.com/en/download/

**PySpark import error?**
- Reinstall: `pip install --upgrade pyspark`

**Port 8501 already in use?**
```bash
streamlit run app.py --server.port 8502
```

## License

MIT License

## Author

Built with ⚡ for PySpark learners
