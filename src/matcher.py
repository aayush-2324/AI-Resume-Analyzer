from __future__ import annotations

from typing import Iterable

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def text_similarity(resume_text: str, job_description: str) -> float:
    """Return cosine similarity between resume and job-description text as a percentage."""
    if not resume_text.strip() or not job_description.strip():
        return 0.0

    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform([resume_text, job_description])
    score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
    return round(float(score) * 100, 2)


def skill_match(resume_skills: Iterable[str], job_skills: Iterable[str]) -> dict:
    resume_set = {skill.lower() for skill in resume_skills}
    job_set = {skill.lower() for skill in job_skills}

    if not job_set:
        return {"matched": [], "missing": [], "match_percent": 0.0}

    matched = sorted(resume_set & job_set)
    missing = sorted(job_set - resume_set)
    percent = round(len(matched) / len(job_set) * 100, 2)

    return {
        "matched": matched,
        "missing": missing,
        "match_percent": percent,
    }
