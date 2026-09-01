from database import *

while True:

    print("\n========== MOVIE MANAGEMENT SYSTEM ==========")

    print("1. Add Movie")
    print("2. View All Movies")
    print("3. Search Movie")
    print("4. Delete Movie")
    print("5. Update Movie Rating")

    print("\n---------- FILTER MOVIES ----------")

    print("6. Movies by Genre")
    print("7. Movies by Language")
    print("8. Movies by Actor")
    print("9. Movies by Director")
    print("10. Movies by Year")

    print("\n---------- MOVIE ANALYTICS ----------")

    print("11. Highest Rated Movie")
    print("12. Lowest Rated Movie")
    print("13. Average Rating")
    print("14. Actor Movie Count")
    print("15. Genre Movie Count")
    print("16. Most Popular Genre")

    print("\n---------- RECOMMENDATION ----------")

    print("17. Recommend Movies")
    print("18. Exit")

    print("============================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        movie_title = input("Enter movie title: ")
        movie_director = input("Enter director name: ")
        movie_year = int(input("Enter release year: "))
        movie_genre = input("Enter genre: ")
        movie_rating = float(input("Enter movie rating: "))
        movie_language = input("Enter language: ")
        movie_actors = input("Enter actor names separated by spaces: ").split()

        add_movie(movie_title, movie_director, movie_year, movie_genre,
                  movie_rating, movie_language, *movie_actors)

    elif choice == 2:

        print(get_all_movies())

    elif choice == 3:

        movie_title = input("Enter movie title to search: ")
        print(search_movie(movie_title))

    elif choice == 4:

        movie_title = input("Enter movie title to delete: ")
        print(delete_movie(movie_title))

    elif choice == 5:

        movie_title = input("Enter movie title: ")
        new_rating = float(input("Enter new rating: "))
        update_rating(movie_title, new_rating)

    elif choice == 6:

        movie_genre = input("Enter genre: ")
        print(get_movies_by_genre(movie_genre))

    elif choice == 7:

        movie_language = input("Enter language: ")
        print(get_movies_by_language(movie_language))

    elif choice == 8:

        movie_actor = input("Enter actor name: ")
        print(get_movies_by_actor(movie_actor))

    elif choice == 9:

        movie_director = input("Enter director name: ")
        print(get_movies_by_director(movie_director))

    elif choice == 10:

        movie_year = int(input("Enter release year: "))
        print(get_movies_by_year(movie_year))

    elif choice == 11:

        get_highest_rated_movie()

    elif choice == 12:

        get_lowest_rated_movie()

    elif choice == 13:

        get_average_rating()

    elif choice == 14:

        movie_actor = input("Enter actor name: ")
        get_actor_movie_count(movie_actor)

    elif choice == 15:

        movie_genre = input("Enter genre: ")
        get_genre_movie_count(movie_genre)

    elif choice == 16:

        get_most_popular_genre()

    elif choice == 17:

        movie_language = input("Enter preferred language: ")
        movie_genre = input("Enter preferred genre: ")
        movie_rating = float(input("Enter minimum rating: "))

        movie_recommendation(movie_language, movie_genre, movie_rating)

    elif choice == 18:

        print("Exiting Movie Management System...")
        break

    else:

        print("Invalid choice. Please try again.")
