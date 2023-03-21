import datetime

from update_tables import *
from movies_app.models import *

if __name__ == '__main__':

    # Get all the actors in the db who are younger than 50 years old
    year_to_filter = datetime.date.today().year - 50
    q1 = Actor.objects.filter(birth_year__gt=year_to_filter)
    print(*q1, sep=",")

    # Get movies that last less than 2.5 hours and were released after 2005
    q2 = Movie.objects.filter(duration_in_min__lt=150, year__gt=2005)
    print(*q2, sep="\n")

    # Get all the movies that contain a word “criminal”, “mob” or “cop” in their description
    q3 = Movie.objects.filter(Q(name__icontains="tar") | Q(name__icontains="mob") | Q(name__icontains="cop"))
    print(*q3, sep="\n")

    # Like previous, but get only movies that were released before 2010
    q4 = Movie.objects.filter((Q(name__icontains="tar") | Q(name__icontains="mob") | Q(name__icontains="cop")),
                              year__lt=1988)
    print(*q4, sep="\n")

    # Get list of actors, and add amount of movies they played in (for each one)
    q5 = Actor.objects.annotate(
        movies_count=Count('movies')
    )
    for actor in q5:
        print(actor.name, actor.movies_count)

    # Get average, min, and max rating in the system
    q6 = Review.objects.aggregate(
        Min('rating'),
        Max('rating'),
        Avg('rating')
    )
    print(q6)

    # Get Movies with their avg ratings
    q7 = Movie.objects.annotate(
          avg_rating=Avg('review__rating')
    )
    for movie in q7:
        print(movie.name, movie.avg_rating)

    # Get ratings that were created in 2023
    q8 = Review.objects.filter(
        review_date__year__gte=2023,
        review_date__year__lt=2024
    )
    print(*q8, sep="\n")

    # Get all the actors in the system with min and max rating of the movies they played in
    q9 = Actor.objects.annotate(
        min_val=Min('movie__review__rating'),
        max_val=Max('movie__review__rating')
    )
    for actor in q9:
        print(actor.name, actor.min_val, actor.max_val)

    # Get movies with average salary for actors in each one
    q10 = Movie.objects.annotate(
        avg_salary=Avg("movieactor__salary")
    )
    for actor in q10:
        if actor.avg_salary:
            print(actor.name, actor.avg_salary)

    # Get actors with their average salaries
    q11 = Actor.objects.annotate(
        avg_salary=Avg("movieactor__salary")
    )
    for actor in q11:
        if actor.avg_salary:
            print(actor.name, actor.avg_salary)

    # Get actors who played main roles at least once
    q12 = Actor.objects.annotate(
        main_role=Count(
            'movieactor__id',
            filter=Q(movieactor__main_role=True)
        )
    ).filter(
        main_role__gte=1
    )
    for actor in q12:
        print(actor.name, actor.main_role)

    # Get movies and amount of actors who played main roles
    q13 = Movie.objects.filter(
        movieactor__main_role=True
    ).annotate(
        num_of_actors=Count('actor')
    )
    for movie in q13:
        print(movie.name, movie.num_of_actors)



