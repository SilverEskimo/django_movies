from django.db import models
from django.db.models import RESTRICT
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
    class Meta:
        db_table = 'movies'

    name = models.CharField(max_length=128)
    year = models.IntegerField()
    director = models.ForeignKey(to="Director", on_delete=RESTRICT, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    duration_in_min = models.IntegerField(null=True)

    # for many to many relations
    actors = models.ManyToManyField('Actor', through="MovieActor")

    def __str__(self):
        return f"{self.name}, Year: {self.year}"


class Director(models.Model):
    # This is the Directors table
    class Meta:
        db_table = 'directors'

    name = models.CharField(max_length=128)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.name}, Birth date: {self.birth_date}"

# Add a new model Review that represents review for a specific movie.
# The model should contain the following fields: rating (1 to 10),
# review_date, review text - optional, foreign key to movie id.


class Review(models.Model):
    # This is the reviews table
    class Meta:
        db_table = 'reviews'

    movie = models.ForeignKey(to="Movie", on_delete=RESTRICT)
    rating = models.FloatField(
        validators=[
            MaxValueValidator(limit_value=10),
            MinValueValidator(limit_value=1)
        ]
    )

    review_date = models.DateField()
    review_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.movie.name}, Rating: {self.rating}, Date: {self.review_date}, Text: {self.review_text}"


class Actor(models.Model):
    class Meta:
        db_table = "actors"

    name = models.CharField(max_length=256, db_column='name', null=False, blank=False)
    birth_year = models.IntegerField(db_column='birth_year', null=False, blank=False)

    # for many to many relations
    movies = models.ManyToManyField(Movie, through="MovieActor")

    def __str__(self):
        return self.name


class MovieActor(models.Model):

    # Many to many relation
    class Meta:
        db_table = "movie_actors"

    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    salary = models.FloatField()
    main_role = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return f"{self.actor.name} in movie {self.movie.name}"
    