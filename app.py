
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="🎬 Movie Recommender", layout="wide", page_icon="🎥")

@st.cache_data
def load_data():
    df = pd.read_csv("data/movies.csv")
    df["text"] = (df["overview"].fillna("") + " " + df["genres"].fillna(""))
    return df

@st.cache_resource
def build_model(texts):
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1,2), min_df=1)
    tfidf = vectorizer.fit_transform(texts)
    sim = cosine_similarity(tfidf)
    return vectorizer, tfidf, sim

def recommend_by_title(df, sim, title, top_k=10, allowed_genres=None, year_range=None):
    if title not in df["title"].values:
        return pd.DataFrame(columns=["title","year","genres","similarity"])
    idx = df.index[df["title"] == title][0]
    scores = list(enumerate(sim[idx]))
    # sort by similarity descending, skip same movie
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:]
    recs = df.iloc[[i for i,_ in scores]].copy()
    recs["similarity"] = [s for _, s in scores]

    # optional filters
    if allowed_genres:
        recs = recs[recs["genres"].str.contains("|".join(allowed_genres), case=False, na=False)]
    if year_range:
        y0, y1 = year_range
        recs = recs[(recs["year"] >= y0) & (recs["year"] <= y1)]

    return recs.head(top_k)[["title","year","genres","similarity"]]

def search_by_query(df, vectorizer, tfidf, query, top_k=10, allowed_genres=None, year_range=None):
    q_vec = vectorizer.transform([query])
    scores = cosine_similarity(q_vec, tfidf).flatten()
    recs = df.copy()
    recs["similarity"] = scores

    # optional filters
    if allowed_genres:
        recs = recs[recs["genres"].str.contains("|".join(allowed_genres), case=False, na=False)]
    if year_range:
        y0, y1 = year_range
        recs = recs[(recs["year"] >= y0) & (recs["year"] <= y1)]

    recs = recs.sort_values("similarity", ascending=False)
    return recs.head(top_k)[["title","year","genres","similarity"]]

# ---------------- UI ----------------
st.title("🎬 Movie Recommendation System")
st.markdown("Simple, fast, content-based recommendations. Upload your own dataset later to scale it up.")

df = load_data()
vectorizer, tfidf, sim = build_model(df["text"].tolist())

with st.sidebar:
    st.header("Controls")
    mode = st.radio("Recommendation Mode", ["By Movie Title", "By Text Query"])
    top_k = st.slider("Number of recommendations", 3, 20, 8)
    all_genres = sorted({g.strip() for row in df["genres"].dropna().tolist() for g in row.split(",")})
    allowed_genres = st.multiselect("Filter by genres (optional)", all_genres)
    year_min, year_max = int(df["year"].min()), int(df["year"].max())
    year_range = st.slider("Year range", year_min, year_max, (year_min, year_max))
    st.caption("Tip: Narrow genres/year to focus results.")

if mode == "By Movie Title":
    title = st.selectbox("Pick a movie you like", sorted(df["title"].tolist()))
    if st.button("Recommend 🎯", use_container_width=True):
        recs = recommend_by_title(df, sim, title, top_k=top_k, allowed_genres=allowed_genres or None, year_range=year_range)
        st.subheader(f"Because you liked **{title}**")
        st.dataframe(recs.reset_index(drop=True))
else:
    query = st.text_input("Describe what you feel like watching", value="space exploration drama with emotions")
    if st.button("Search & Recommend 🔎", use_container_width=True):
        recs = search_by_query(df, vectorizer, tfidf, query, top_k=top_k, allowed_genres=allowed_genres or None, year_range=year_range)
        st.subheader("Top Matches")
        st.dataframe(recs.reset_index(drop=True))

st.markdown("---")
with st.expander("📁 How to use your own dataset"):
    st.markdown(
        """
        1. Replace `data/movies.csv` with your file. Keep columns: `title`, `year`, `genres`, `overview`.
        2. If your column names differ, rename them in the code where `load_data()` reads the CSV.
        3. For larger datasets, consider precomputing embeddings or switching to approximate nearest neighbors.
        """
    )
