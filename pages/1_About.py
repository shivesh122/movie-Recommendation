import streamlit as st

st.set_page_config(page_title="About - Movie Recommender", layout="wide")

st.title("🎬 About This App")

st.markdown("""
Welcome! This is a **Content-Based Movie Recommendation System** built using **Streamlit** and **scikit-learn**.

---

### 👤 Creator
**Shivesh Tiwari**  
Check out my portfolio: [My Work](https://shivesh-portfolio.vercel.app)

---

### ⚡ Features
- Recommend movies **by selecting a movie you like**
- Recommend movies **by typing a description of your mood or preference**
- Filter recommendations by **genre** and **year range**
- Clean and interactive interface, easy to use

---

### 📁 Dataset
- `data/movies.csv` contains:
  - `title` (Movie Title)  
  - `year` (Release Year)  
  - `genres` (Comma-separated genres)  
  - `overview` (Short description of the movie)  

You can replace it with your own dataset, keeping the same column names.

---

### 🛠 How to Customize
1. Edit `app.py` to adjust TF-IDF or recommendation logic.  
2. Update `.streamlit/config.toml` to change theme, colors, or layout.  
3. Add more metadata (cast, director, keywords) to improve recommendations.

---

### 🚀 Deployment
- Push the repository to **GitHub**  
- Deploy on **[Streamlit Community Cloud](https://share.streamlit.io)** → select `app.py` as the main file  
- Your app will be live with a public URL for sharing
""")

