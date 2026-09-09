from pathlib import Path
import tempfile

from flask import Flask, render_template, request

from src.resume_parser import extract_text_from_pdf
from src.analyzer import analyze_resume

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        resume = request.files.get("resume")
        job_description = request.form.get("job_description", "").strip()

        if not resume or not resume.filename.lower().endswith(".pdf"):
            error = "Please upload a PDF resume."
        elif not job_description:
            error = "Please paste a job description."
        else:
            try:
                with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp:
                    resume.save(temp.name)
                    resume_text = extract_text_from_pdf(temp.name)
                result = analyze_resume(resume_text, job_description)
            except Exception as exc:
                error = str(exc)

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
