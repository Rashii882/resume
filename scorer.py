def rate_resume(text):
    score = 5
    if len(text) > 500:
        score += 2
    if "project" in text.lower():
        score += 1
    if "experience" in text.lower():
        score += 1
    return min(score, 10)