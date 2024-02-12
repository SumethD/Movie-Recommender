# Movie Recommender System

This is a Movie Recommender System built using Streamlit, a Python library for creating web applications. The app recommends movies based on a similarity matrix calculated from movie features.

## Features

- **Movie Selection:** Users can select a movie from a dropdown menu to get recommendations.
- **Recommendations:** Upon selecting a movie, the app displays a set of recommended movies along with their details.
- **Movie Details:** Users can expand each recommendation to view additional details such as overview, popularity, release date, and genres.
- **Visual Interface:** The app provides an intuitive interface with images of recommended movies and collapsible sections for details.

## Technologies Used

- **Python:** The backend of the app is developed using Python programming language.
- **Streamlit:** The app's frontend and web interface are built using Streamlit, a Python library for creating web applications.
- **Requests:** The `requests` library is used to make HTTP requests to retrieve movie data from an external API.
- **Pickle:** The `pickle` module is used to load preprocessed movie data and similarity matrices from pickle files.

## Warning: Cannot clone and run it becuz the pickle file for the model is too large . 


## How to Run the App

1. **Clone the Repository:**
2. Empty the newfiles 
3. Create a python conda env .
4. Install the dependencies **pip install -r requirements.txt** + scikit-learn + nltk + matplotlib + pandas
4. run the improvedModel.ipynb file too get the pickle files (the movies and the model)
6. Run **streamlit run app.py**