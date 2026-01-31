def calculate_score(aspect_results):
    score = 0
    for aspect in aspect_results:
        if aspect_results[aspect]["sentiment"] == "POSITIVE":
            score += 1
        elif aspect_results[aspect]["sentiment"] == "NEGATIVE":
            score -= 1
    return score

def recommend(score, threshold=1):
    if score >= threshold:
        return "RECOMMENDED ✅"
    else:
        return "NOT RECOMMENDED ❌"
