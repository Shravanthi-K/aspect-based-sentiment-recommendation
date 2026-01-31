from aspect_sentiment import analyze_aspects
from recommender import calculate_score, recommend

print("Aspect-Based Sentiment & Recommendation System")
print("---------------------------------------------")

review = input("Enter product review: ")

aspect_results = analyze_aspects(review)

if not aspect_results:
    print("No known aspects found.")
else:
    score = calculate_score(aspect_results)
    decision = recommend(score)

    print("\nAspect Analysis:")
    for aspect, res in aspect_results.items():
        print(f"{aspect}: {res['sentiment']} ({res['score']:.2f})")

    print("\nFinal Decision:", decision)
