# 🎬 Movie Recommendation System

![Movie Logo](https://github.com/coder-akram-khan/ML-Based-Movie-Recommendation-System-/blob/main/covermovie.png?raw=true)

---

## 📌 About the Project

🎥 The **Movie Recommendation System** is a **content-based filtering** model that suggests similar movies based on their **genres, cast, crew, and storyline**. Using **Natural Language Processing (NLP) and Machine Learning**, this system helps users discover movies they'll love! 🍿✨

---

## 🛠️ Technologies Used

🔹 **Programming Language**: ![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python)
🔹 **Libraries**:  
&nbsp;&nbsp;&nbsp;&nbsp;✅ **Streamlit** - Web App Framework  
&nbsp;&nbsp;&nbsp;&nbsp;✅ **Pandas** - Data Handling  
&nbsp;&nbsp;&nbsp;&nbsp;✅ **NumPy** - Numerical Computing  
&nbsp;&nbsp;&nbsp;&nbsp;✅ **scikit-learn** - Machine Learning  
&nbsp;&nbsp;&nbsp;&nbsp;✅ **NLTK** - Natural Language Processing  
&nbsp;&nbsp;&nbsp;&nbsp;✅ **Requests** - API Integration (TMDB API for Posters)  
&nbsp;&nbsp;&nbsp;&nbsp;✅ **Pickle** - Model Serialization  

---

## 🎯 Features

✅ **Content-Based Filtering** - Recommends movies based on similarity score  
✅ **Movie Posters** - Uses **TMDB API** to fetch high-quality posters  
✅ **Interactive UI** - Built with **Streamlit** for a smooth experience  
✅ **Fast & Efficient** - Uses **CountVectorizer** & **Cosine Similarity** for recommendations  
✅ **Lottie Animations** - Engaging UI elements for a great user experience  

---

## 🚀 How It Works

1️⃣ **Select a Movie** from the dropdown list.  
2️⃣ Click **"Recommend"** and instantly get **5 similar movie suggestions**.  
3️⃣ View the **movie posters** for each recommended film.  

![Demo GIF](https://github.com/coder-akram-khan/ML-Based-Movie-Recommendation-System-/blob/main/demo.gif?raw=true)

---

## 🏗️ Project Structure

```
movies-recommender-system/
│── app.py                      # Streamlit web app  
│── movie-recommender.ipynb      # Jupyter Notebook for model building  
│── similarity.pkl               # Precomputed similarity matrix  
│── dataset/                     # Contains dataset files  
│   ├── tmdb_5000_movies.csv  
│   ├── tmdb_5000_credits.csv  
│── movies.pkl                   # Processed movie dataset  
│── requirements.txt              # Required Python libraries  
```

---


### 🔧 Installation & Setup
```bash
# Clone this repository
$ git clone https://github.com/coder-akram-khan/ML-Based-Movie-Recommendation-System-.git

# Navigate to project directory
$ cd ML-Based-Movie-Recommendation-System-

# Install dependencies
$ pip install -r requirements.txt

# Run Streamlit App
$ streamlit run app.py
```

---

## 🔥 Future Enhancements

✅ **Hybrid Recommendations** (Collaborative + Content-Based Filtering)  
✅ **IMDb Ratings & Movie Duration Display**  
✅ **Trending & Popular Movie Suggestions**  
✅ **Genre-Based Filtering** for more refined results  

---

## 📬 Connect with Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/mr-akram-khan/)  
[![GitHub](https://img.shields.io/badge/GitHub-View_Repository-black?style=flat&logo=github)](https://github.com/coder-akram-khan)

🚀 **Enjoy your personalized movie recommendations!** 🍿🎥

