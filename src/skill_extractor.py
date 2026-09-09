import re
from typing import Iterable

SKILLS = {
    "python", "java", "javascript", "typescript", "c++", "sql", "html", "css",
    "react", "node.js", "flask", "fastapi", "django", "pandas", "numpy",
    "scikit-learn", "tensorflow", "pytorch", "machine learning", "deep learning",
    "nlp", "data analysis", "data visualization", "power bi", "tableau",
    "git", "github", "docker", "aws", "azure", "gcp", "linux", "mongodb",
    "mysql", "postgresql", "excel"
}


def normalize_text(text: str) -> str:
    text = text.lower().replace("nodejs", "node.js").replace("scikit learn", "scikit-learn")
    return re.sub(r"\s+", " ", text).strip()


def extract_skills(text: str, skills: Iterable[str] = SKILLS) -> list[str]:
    normalized = normalize_text(text)
    found = []
    for skill in skills:
        pattern = rf"(?<![a-z0-9]){re.escape(skill.lower())}(?![a-z0-9])"
        if re.search(pattern, normalized):
            found.append(skill)
    return sorted(found)
