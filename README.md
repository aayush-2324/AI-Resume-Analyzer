# 🤖 AI Resume Analyzer & Job Matcher

An NLP-powered resume analysis project that compares a candidate resume with a job description, calculates a transparent compatibility score, identifies matching and missing skills, and generates actionable improvement suggestions.

## 🎯 Project Goals

- Extract useful information from resumes
- Identify technical and professional skills
- Compare resume skills with a target job description
- Calculate an explainable ATS-style compatibility score
- Highlight matched and missing skills
- Recommend relevant job roles
- Provide practical resume improvement suggestions

## 🧠 Planned Architecture

```text
Resume PDF + Job Description
          ↓
    Text Extraction
          ↓
   Text Preprocessing
          ↓
     Skill Extraction
          ↓
 Resume ↔ Job Matching
          ↓
 Compatibility Scoring
          ↓
 Recommendations + Dashboard
```

## 🛠️ Tech Stack

- Python
- NLP
- Pandas / NumPy
- Scikit-learn
- PDF text extraction
- Flask or FastAPI
- HTML / CSS / JavaScript
- SQLite / SQL

## 📁 Project Structure

```text
AI-Resume-Analyzer/
├── data/
├── src/
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   ├── matcher.py
│   └── analyzer.py
├── app/
│   ├── app.py
│   ├── templates/
│   └── static/
├── outputs/
├── requirements.txt
├── .gitignore
└── README.md
```

## 📌 Development Roadmap

- [x] Repository setup
- [ ] Resume PDF text extraction
- [ ] Text preprocessing
- [ ] Skill extraction
- [ ] Job description parser
- [ ] Resume-job similarity model
- [ ] Explainable ATS-style scoring
- [ ] Skill-gap analysis
- [ ] Job-role recommendations
- [ ] Web dashboard
- [ ] Testing and deployment

> **Note:** Scores and recommendations will be generated from the implemented analysis pipeline; no fabricated hiring or ATS claims are used.

## 🚀 Future Improvements

- Semantic embeddings for better matching
- Resume section detection
- Multiple job-description comparison
- Resume improvement assistant
- Analytics dashboard
- Model evaluation with labeled examples

## 👨‍💻 Author

**Aayush** — B.Tech Data Science & AI Student
