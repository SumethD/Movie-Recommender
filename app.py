import pickle
import streamlit as st
import requests

st.set_page_config(page_title="Movie Recommender System", page_icon="🎬", layout="wide", initial_sidebar_state="collapsed",)

st.markdown(
    """
    <h1 style='text-align: center;'>Movie Recommender System</h1>
    """,
    unsafe_allow_html=True
)
# Changing background color to white

movies = pickle.load(open('newfiles\\movies.pkl','rb'))
similarity = pickle.load(open('newfiles\\similarity.pkl','rb'))

movies_list =movies['title'].values 
movie_choice= st.selectbox('Search Movie For Recommendations', movies_list ) 

def fetchPoster(movieID):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=7804b1bdc89bc7778b2d68450665664c".format(movieID)
    try:
        data = requests.get(url)
        data.raise_for_status()  # Raise an exception for HTTP errors
        data = data.json()
        poster = data['poster_path']
        fullpath = "http://image.tmdb.org/t/p/w500"+ poster
        return fullpath, data 
    except Exception as e:
        st.error(f"Error fetching poster for movie ID {movieID}: {e}")
        return None



def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    rec_mvName = []
    rec_mvPoster = []
    rec_mvData = []  # Store movie details
    
    for i in distances[1:7]:
        movieID = movies.iloc[i[0]].movie_id
        name, data = fetchPoster(movieID)
        rec_mvName.append(movies.iloc[i[0]].title)
        rec_mvPoster.append(name)
        rec_mvData.append(data)
    
    return rec_mvPoster, rec_mvName, rec_mvData


if st.button('Show recommendations'):
    recommended_mvPoster, recommended_mvName, recommended_mvDetails = recommend(movie_choice)
    for i in range(len(recommended_mvPoster)):
        col1, col2 = st.columns([1, 3])  # Define column widths as needed
        with col1:
            st.image(recommended_mvPoster[i], caption=recommended_mvName[i], width=300)  # Display image in the first column
        with col2:
            with st.expander(f"Movie Details for {recommended_mvName[i]}"):  # Display movie details in the second column
                st.write("Overview:", recommended_mvDetails[i]['overview'])
                st.write("Popularity:", recommended_mvDetails[i]['popularity'])
                st.write("Release Date:", recommended_mvDetails[i]['release_date'])
                st.write("Genres:", ', '.join(genre['name'] for genre in recommended_mvDetails[i]['genres']))


     


