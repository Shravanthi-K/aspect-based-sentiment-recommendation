import streamlit as st
from aspect_sentiment import analyze_aspects
from recommender import calculate_score, recommend

st.title("Aspect-Based Sentiment & Recommendation System")

review = st.text_area("Enter product review:")

if st.button("Analyze"):
    if review.strip() == "":
        st.warning("Please enter a review")
    else:
        aspect_results = analyze_aspects(review)

        if not aspect_results:
            st.error("No known aspects found")
        else:
            score = calculate_score(aspect_results)
            decision = recommend(score)

            st.subheader("Aspect Analysis")
            for aspect, res in aspect_results.items():
                st.write(f"**{aspect.capitalize()}**: {res['sentiment']} ({res['score']:.2f})")

            st.subheader("Final Recommendation")
            st.success(decision)
