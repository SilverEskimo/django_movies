import csv
import datetime
import os
import django
from django.db.models import Q, Count, Min, Max, Avg

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"
django.setup()

from movies_app.models import *
import movies_app.models


def create_movie(movie_name:str, movie_year: int, director: movies_app.models.Director=None, movie_description=None):
    movie = Movie.objects.create(
        name=movie_name,
        year=movie_year,
        director=director,
        description=movie_description
    )
    return movie


def create_director(director_name:str, birth_date: datetime.date):
    director = Director.objects.create(
        name=director_name,
        birth_date=birth_date
    )
    return director


def create_review(rating: float, review_date: datetime.date, movie: Movie, review_text=None):
    review = Review(
        rating=rating,
        review_date=review_date,
        movie=movie,
        review_text=review_text
    )
    try:
        review.full_clean()
        review.save()
        return review
    except Exception as e:
        print(e)


def insert_movies(file_name: str):
    with open(f"{file_name}.csv", "r") as f:
        csv_reader = csv.DictReader(f)
        list_of_movies = list(csv_reader)
        for movie in list_of_movies:
            m = create_movie(
                movie["Movie_Name"],
                int(movie["Release_date"])
            )
            create_review(float(movie["Rating"]), datetime.date.today(), m)


if __name__ == '__main__':
    insert_movies("IMDB")
