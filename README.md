
# 🎬 Streamlit Movie Recommender (Ready-to-Deploy)

A minimal, good-looking, **content-based** movie recommendation app using **TF‑IDF + cosine similarity**.

## 🚀 Quickstart
1. **Download and extract** this zip.
2. Push to **GitHub** (include all files).
3. Go to **Streamlit Community Cloud** → *New app* → choose your repo → entry point: `app.py`.
4. Click **Deploy**. Your app will be live at a public URL.

## 🧩 Tech
- Streamlit for UI
- scikit-learn for TF‑IDF and cosine similarity
- pandas / numpy for data handling

## 📁 Dataset
Demo dataset lives at `data/movies.csv` with columns:
- `title` (str)
- `year` (int)
- `genres` (comma-separated str)
- `overview` (str)

Replace it with your own file keeping the same column names.

## 🛠 Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🧪 Customizing
- Theme: `.streamlit/config.toml`
- About page: `pages/1_About.py`
- Vectorizer: edit `build_model` in `app.py`

## 💡 Tips for Better Recs
- Add more fields (cast, director, keywords) to the `text` feature.
- Use embeddings (e.g., sentence-transformers) for semantic recommendations if your plan allows it.
- For big datasets, use an ANN index (FAISS, Spotify Annoy).

---

Made for quick portfolio deployment.
