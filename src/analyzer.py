from __future__ import annotations

from src.skill_extractor import extract_skills
from src.matcher import skill_match, text_similarity


def analyze_resume(resume_text: str, job_description: str) -> dict:
    """Run the first version of the explainable resume analysis pipeline."""
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)
    skill_result = skill_match(resume_skills, job_skills)
    similarity = text_similarity(resume_text, job_description)

    # Transparent weighted score; this is an internal project metric, not a claim
    # about any real applicant-tracking system's proprietary scoring formula.
    ats_score = round(0.6 * skill_result["match_percent"] + 0.4 * similarity, 2)

    return {
        "ats_style_score": ats_score,
        "text_similarity": similarity,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        **skill_result,
    }


if __name__ == "__main__":
    resume = "Python Pandas NumPy SQL Git data analysis machine learning"
    job = "We need Python, SQL, Pandas, Git, machine learning and Docker."
    result = analyze_resume(resume, job)
    for key, value in result.items():
        print(f"{key}: {value}")
