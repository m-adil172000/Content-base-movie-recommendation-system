from flask_wtf import FlaskForm
import pandas as pd
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired

movies = pd.read_csv('Data/movies_data.csv')


class InputForm(FlaskForm):
    movies = SelectField(
        label="Movies",
        choices= movies.Title.unique().tolist(),
        validators=[DataRequired()]
    )

    submit = SubmitField("Recommend")