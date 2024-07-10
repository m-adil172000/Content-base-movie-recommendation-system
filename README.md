## Introduction
This Movie Recommendation System is a web application that recommends top 10 similar movies to the movie selected by them. It leverages the TMDb API for fetching movie details and then using machine learning and deep learning algorithms it recommends similar movies.

#ML-DL
- applied pre-processing steps on the dataframe and perfomred EDA
- Used NLTK library for text processing like lowercasing, removed punctuations, removed stop words, stemming
- used pickle to dump the data
- Applied text vectorization using Bag of words, tfidfvectorizer and BERT model. tfidfvectorizer gave the best result so used that for recommendations.
  

## Features
- Recommend movies similar to the one specified by the user.
- Display movie posters and relevant details.
- Interactive and user-friendly interface.
- Background colors and basic aesthetics styling.

## Technologies Used
- **Flask**: Web framework for Python.
- **TMDb API**: For fetching movie data.
- **Pandas**: For data manipulation and analysis.
- **Jinja2**: Templating engine for rendering HTML.
- **HTML/CSS**: For structuring and styling web pages.

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/m-adil172000/Content-base-movie-recommendation-system
.git
    cd movierecommendation
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up TMDb API key**:
    - Sign up on [TMDb](https://www.themoviedb.org/) and get an API key.
    - Create a `.env` file in the project root and add your API key:
      ```plaintext
      TMDB_API_KEY=your_tmdb_api_key
      ```


## Usage
- **Home Page**: Welcome message.
- **Recommend Page**: Input a movie name to get similar movie recommendations.
- **Recommendation Results**: View the list of recommended movies with their posters and links to their TMDb pages.

## Project Structure
movierecommendation/
├── static/
│ └── style.css
├── templates/
│ ├── layout.html
│ ├── home.html
│ ├── recommend.html
│ └── recommendation_page.html
├── forms.py
├── app.py
├── requirements.txt
├── df_merged_dict.pkl
├── movies_tags.csv
├── df_merged.pkl
