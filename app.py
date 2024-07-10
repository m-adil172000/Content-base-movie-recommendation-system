from flask import (
    Flask, 
    redirect,
    url_for, 
    render_template,
)
from forms import InputForm
import pickle
import pandas as pd
from flask import request
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#from transformers import pipeline


# Create the Hugging Face pipeline for text generation
#generator = pipeline('text-generation', model='gpt2')

#OTDB_API_URL = 'https://opentdb.com/api.php?amount=3&category=11&difficulty=easy&type=multiple'


movie_df = pd.read_csv('Data/movies_data.csv',index_col=False)
#similarity = pickle.load(open("similarity.pkl", "rb"))
movie_tags = pd.read_csv('movies_tags.csv', index_col=False)


tfidf = TfidfVectorizer(max_features=5000)
tfidf_matrix = tfidf.fit_transform(movie_tags['tags']).toarray()
similarity= cosine_similarity(tfidf_matrix)


# create the flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

# home page
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Movies Recommendation System")

def fetch_movie_url(movie_id):
    return f"https://www.themoviedb.org/movie/{movie_id}" 

def fetch_poster(movie_id):
    #movie_id = movie_df[movie_df.Title == movie_name].iloc[0].Id
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzOGIyYjAyNWQ2NjkwMGQ3NWRjYWY0OTgzMTI5MDk1MyIsIm5iZiI6MTcyMDYwMjg2Mi4yMzkxODcsInN1YiI6IjYyZGQ0NmQxZWE4NGM3MDA2NzRhYTU1ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LYt-56cu6Y4UzdvI36cNY3x-lnidhaOHAjnDiiCFu_M"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return "https://image.tmdb.org/t/p/original" + data['poster_path']

'''
def fetch_fun_facts(movie_title):
    try:
        prompt = f"Generate some fun facts about the movie {movie_title}."
        response = generator(prompt, max_length=100, num_return_sequences=1)
        fun_facts = response[0]['generated_text'].strip()
        return fun_facts
    except Exception as e:
        return f"Could not generate fun facts: {str(e)}"
'''

# Recommend page
@app.route("/recommend", methods=["GET","POST"])
def recommend():
    form = InputForm()
    if form.validate_on_submit():
        movie_name = form.movies.data
        print(f"Form validated. Redirecting with movie name: {movie_name}")
        return redirect(url_for("recommendation_page", movie_name=movie_name))
    return render_template("recommend.html", title="Recommend Movies", form=form)

@app.route("/recommendation_page", methods=['GET',"POST"])
def recommendation_page():
    movie_name = request.args.get('movie_name')
    recommended_movies=[]
    movie_idx = movie_df[movie_df.Title == movie_name].index[0]
    distances = similarity[movie_idx]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10]
    for i in movie_list:
        title = movie_df.iloc[i[0]].Title
        id = movie_df.iloc[i[0]].Id
        poster = fetch_poster(id)
        movie_link = fetch_movie_url(id)
        movie_tagline = movie_df.iloc[i[0]].Tagline
        #fun_facts = fetch_fun_facts(title)
        recommended_movies.append({'title': title, 'poster': poster, 'url':movie_link, 'tagline': movie_tagline})
    
    return render_template("recommendation_page.html", movie=movie_name, recommendations=recommended_movies, error=None)

if __name__ == "__main__":
    app.run(debug=True)




