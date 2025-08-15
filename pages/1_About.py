
# About this app

This is a **content-based movie recommendation** demo built with **Streamlit** and **scikit-learn**.
It uses TF‑IDF on movie overviews + genres and cosine similarity for recommendations.

**How to customize**
- Replace `data/movies.csv` with your dataset (columns: `title, year, genres, overview`).
- Tweak vectorizer settings in `build_model`.
- Style via `.streamlit/config.toml`.

**Deployed on Streamlit Cloud**
- Connect your GitHub repo and choose `app.py` as the entry point.
