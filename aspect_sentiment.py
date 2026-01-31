from transformers import pipeline
import re

# -------------------------------
# 1. Define aspects
# -------------------------------
ASPECTS = {
    "camera": ["camera", "photo", "lens"],
    "battery": ["battery", "charging", "backup", "poor"],
    "price": ["price", "cost", "expensive", "cheap", "high", "low"],
    "display": ["display", "screen"]
}

# -------------------------------
# 2. LOAD MODEL (THIS WAS MISSING / MOVED)
# -------------------------------
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# -------------------------------
# 3. Sentence splitter (NO NLTK)
# -------------------------------
def split_sentences(text):
    parts = re.split(r'[.!?]|but|and', text.lower())
    return [p.strip() for p in parts if p.strip()]

# -------------------------------
# 4. Aspect-based sentiment
# -------------------------------
def analyze_aspects(review):
    results = {}
    sentences = split_sentences(review)

    for sentence in sentences:
        for aspect, keywords in ASPECTS.items():
            if aspect not in results and any(word in sentence for word in keywords):

                prediction = sentiment_model(sentence)[0]
                label = prediction["label"]
                score = prediction["score"]

                # Aspect-specific rule for PRICE
                if aspect == "price":
                    if any(w in sentence for w in ["high", "expensive"]):
                        label = "NEGATIVE"
                    elif any(w in sentence for w in ["low", "cheap", "affordable"]):
                        label = "POSITIVE"

                results[aspect] = {
                    "sentiment": label,
                    "score": score
                }

    return results
