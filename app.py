import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

st.set_page_config(page_title="Movie Review Analyzer", layout="centered")

st.title("🎬 Movie Review Sentiment Analyzer")
st.write("Type your movie review and I'll tell if it's Positive or Negative")

# Sample movie recommendations
movies = {
    "positive": ["3 Idiots", "Bahubali", "RRR", "KGF", "Pushpa"],
    "negative": ["Race 3", "Humshakals", "Tees Maar Khan", "Action Jackson"]
}

@st.cache_resource
def train_model():
    df = pd.read_csv("movie_reviews.csv")
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['review'])
    model = LogisticRegression()
    model.fit(X, df['sentiment'])
    return model, vectorizer

model, vectorizer = train_model()

user_review = st.text_area("Enter your movie review here:")

if st.button("Analyze Sentiment"):
    if user_review:
        review_vector = vectorizer.transform([user_review])
        prediction = model.predict(review_vector)[0]
        
        if prediction == "positive":
            st.success(f"Result: POSITIVE 😊")
            st.write("**Recommended Movies for you:**")
            st.write(", ".join(movies["positive"][:3]))
        else:
            st.error(f"Result: NEGATIVE 😡")
            st.write("**If you didn't like this, try these:**")
            st.write(", ".join(movies["negative"][:3]))
    else:
        st.warning("Please enter a review first!")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit + ML")