from update_tables import *
from movies_app.models import *


if __name__ == '__main__':
    pass
    # q1 = Movie.objects.filter(year__gt=1990)
    # print(q1)
    #
    # q2 = Movie.objects.filter(year__lt=2000, name__icontains="sky")
    # print(q2)
    #
    # # Add review text “GREAT MOVIE” to reviews with rating higher than 9.4
    # q3 = Review.objects.filter(rating__gte=9).update(review_text="GREAT MOVIE")
    # print(Review.objects.filter(
    #     review_text="GREAT MOVIE"
    #     )
    # )
    #
    # # Get all the reviews for movie “pulp fiction”
    # q4 = Review.objects.filter(movie__name__icontains="pulp fiction")
    # print(q4)
    #
    # # Add new review with rating 10 and text “wow” to all the movies that contain “god father” in their name
    # q5 = Movie.objects.filter(name__icontains="godfather")
    # for movie in q5:
    #     create_review(10, datetime.date.today(), movie, "incredible!")
    #
    # # Add the following durations to the movies:
    #     # Interstellar - 2h 49min
    #     # The Godfather - 2h 55min
    #     # Scarface - 2h 50 min
    # movies_to_update = {
    #     "Interstellar": 169,
    #     "The Godfather": 175,
    #     "Scarface": 170
    # }
    #
    # for k, v in movies_to_update.items():
    #     Movie.objects.filter(name=k).update(duration_in_min=v)
    #
    # # Get all the movies that last more than 2h 50min
    # print(Movie.objects.filter(duration_in_min__gt=170))
    #
    # # Get all the movies with duration longer than 120 min and release year before 2000
    # print(Movie.objects.filter(duration_in_min__gt=120, year__lt=2000))
    #
    # # Get all the movies with rating higher than 9.4
    # movies = Movie.objects.prefetch_related('review_set').all()
    # for m in movies:
    #     res = m.review_set.filter(rating__gt=9.4)
    #     if res:
    #         print(f"Movie Name: {m.name}\nRatings:")
    #         print(*res, sep="\n")

    # Get 5 movies with highest rating (hint: look in django documentation how to run order by queries)





