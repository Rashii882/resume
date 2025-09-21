from flask import Flask, render_template, request
from utils.pdf_reader import extract_text_from_pdf
from utils.analyzer import extract_skills, generate_summary, suggest_improvements
from utils.scorer import rate_resume

app = Flask(_name_)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "resume" not in request.files:
        return "No file uploaded!"

    file = request.files["resume"]
    text = extract_text_from_pdf(file)

    skills = extract_skills(text)
    rating = rate_resume(text)
    suggestions = suggest_improvements(text)
    summary = generate_summary(text)

    return render_template("result.html",
                           skills=skills,
                           rating=rating,
                           suggestions=suggestions,
                           summary=summary)

if _name_ == "_main_":
    app.run(debug=True)