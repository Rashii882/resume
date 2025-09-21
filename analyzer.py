import re

# Dummy skillset list
SKILLS = ["Python", "Java", "C++", "SQL", "Machine Learning", "Data Analysis", "JavaScript", "React"]

def extract_skills(text):
    found = [skill for skill in SKILLS if skill.lower() in text.lower()]
    return found if found else ["No major skills detected"]

def generate_summary(text):
    # Very basic 2-line summary (can improve with NLP)
    lines = text.split("\n")
    return " ".join(lines[:2]) if len(lines) > 2 else "Aspiring professional with relevant skills."

def suggest_improvements(text):
    suggestions = []
    if "project" not in text.lower():
        suggestions.append("Add detailed project descriptions.")
    if "experience" not in text.lower():
        suggestions.append("Mention past work/internship experiences.")
    if "skills" not in text.lower():
        suggestions.append("Highlight your technical and soft skills.")
    return suggestions if suggestions else ["Your resume looks well-balanced."]