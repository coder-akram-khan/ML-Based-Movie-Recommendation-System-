import streamlit as st
import pickle as pkl
import pandas as pd
import requests
import time
from streamlit_lottie import st_lottie

# Function to fetch movie poster
def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=69a337e0d219ec48d1fab40299ca2750&language=en-US'
    response = requests.get(url)
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data.get('poster_path', '')

# Function to fetch additional movie details
def fetch_movie_details(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=69a337e0d219ec48d1fab40299ca2750&language=en-US'
    response = requests.get(url)
    data = response.json()
    return data.get('vote_average', 'N/A'), data.get('release_date', 'N/A'), data.get('overview', 'No overview available')

# Function to recommend movies
def recommend_movie(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    posters = []
    details = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))
        details.append(fetch_movie_details(movie_id))
    return recommended_movies, posters, details

# Load Data
movies = pkl.load(open("movies.pkl", 'rb'))
movies = pd.DataFrame(movies)
similarity = pkl.load(open("similarity.pkl", 'rb'))

# Streamlit UI Setup
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")
st.title("🎥 Movie Recommendation System")
st.markdown("## Find movies similar to your favorites!")

# Function to load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Load animation
lottie_animation = load_lottieurl("https://lottie.host/4793d478-b6c1-4761-b03b-a64c3e67f571/ZLXOty6ysq.json")  # Movie animation

# Layout for movie selection
col1, col2 = st.columns([3, 2])

with col1:
    selected_movie_name = st.selectbox("Select a movie:", movies['title'].values)
    movie_id = movies[movies['title'] == selected_movie_name]['id'].values[0]
    st.image(fetch_poster(movie_id), width=200)

with col2:
    st_lottie(lottie_animation, speed=1, height=400, key="movie_animation")

# Get Recommendations Button
if st.button("Get Recommendations"):
    with st.spinner('Fetching Recommendations...'):
        time.sleep(2)  # Simulate API delay
        #st.success("✅ Recommendations fetched successfully!")

        # Apply sci-fi animated design to "Recommended Movies" heading
        st.markdown("""
            <style>
            /* Google Fonts */
            @import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap");

            :root {
              --accent-color: #03e9f4;
              --box-shadow: 0 0 5px #03e9f4, 0 0 25px #03e9f4, 0 0 50px #03e9f4, 0 0 100px #03e9f4;
              --font: "Montserrat", sans-serif;
            }

            .animated-heading {
              font-size: 26px;
              font-weight: bold;
              text-align: center;
              text-transform: uppercase;
              color: var(--accent-color);
              letter-spacing: 3px;
              position: relative;
              display: inline-block;
              padding-bottom: 5px;
              margin: 20px auto;
              animation: glow 1s infinite alternate;
            }

            .animated-heading::after {
              content: "";
              position: absolute;
              left: 50%;
              bottom: -5px;
              width: 50px;
              height: 2px;
              background: var(--accent-color);
              transform: translateX(-50%);
            }

            @keyframes glow {
              0% { text-shadow: 0 0 5px #03e9f4; }
              100% { text-shadow: 0 0 20px #03e9f4, 0 0 30px #03e9f4; }
            }
            </style>
            <p class="animated-heading">🎞️ Recommended Movies</p>
        """, unsafe_allow_html=True)

        # Fetch recommendations
        names, posters, details = recommend_movie(selected_movie_name)

        # Display recommendations in a stylish layout
        col1, col2, col3, col4, col5 = st.columns(5)

        for i, col in enumerate([col1, col2, col3, col4, col5]):
            with col:
                st.image(posters[i], use_container_width=True)
                st.markdown(f"**{names[i]}**")
                st.markdown(f"⭐ {details[i][0]} | 📅 {details[i][1]}")
                st.caption(details[i][2][:100] + "...")

# Footer
st.markdown("---")
st.markdown("👨‍💻 Developed by **Akram Khan** | Powered by TMDB API")