movies = []

def add_movie(movie_title,movie_director,movie_year,movie_genre,movie_rating,movie_language,*movie_actors):
    movie={}
    movie["title"]=movie_title
    movie["director"]=movie_director
    movie["year"]=movie_year
    movie["genre"]=movie_genre
    movie["rating"]=movie_rating
    movie["language"]=movie_language
    movie["actors"]=movie_actors
    movies.append(movie)


def get_all_movies():
    return movies


def search_movie(movie_title):
    for var in movies:
        if var["title"]==movie_title:
            res=var
            break
    else:
        res="Movie not Available"
        
    return res


def delete_movie(movie_title):
    for var in movies:
        if var['title']==movie_title:
            index=movies.index(var)
            movies.pop(index)
            res="Movie deleted successfully"
            break
    else:
        res="movie not availabe. cant apply delete"
    return res


def update_rating(movie_title,new_rating):
    r= search_movie(movie_title)
    if type(r)==dict:
        r['rating']=new_rating
    else:
        print("movie details not found")


def get_movies_by_genre(movie_genre): 
    same_genre = [] 
 
    for var in movies: 
        if var["genre"] == movie_genre: 
            same_genre.append(var) 
 
    return same_genre


def get_movies_by_language(movie_language):
    result=[]
    for var in movies: 
        if var["language"] == movie_language: 
            result.append(var) 
 
    return result


def get_movies_by_actor(movie_actor): 
    actor_movies = [] 
 
    for var in movies: 
        for i in range(len(var["actors"])):
            if var["actors"][i] == movie_actor: 
                actor_movies.append(var) 
 
    return actor_movies


def get_movies_by_director(movie_director):
    movies_by_director=[]
    for var in movies:
        if var["director"]==movie_director:
            movies_by_director.append(var)
    return movies_by_director


def get_movies_by_year(movie_year): 
    movies_in_year = [] 
 
    for var in movies: 
        if var["year"] == movie_year: 
            movies_in_year.append(var) 
 
    return movies_in_year


def get_highest_rated_movie():
    ratings=[]
    for var in movies:
        ratings.append(var['rating'])
    max_r = max(ratings)
    index = ratings.index(max_r)
    print(f"highest rating is {movies[index]['title']} -  {movies[index]['rating']}")


def get_lowest_rated_movie():
    ratings=[]
    for var in movies:
        ratings.append(var['rating'])
    min_r = min(ratings)
    index = ratings.index(min_r)
    print(f"lowest rating is {movies[index]['title']} -  {movies[index]['rating']}")


def get_average_rating():
    ratings = []
    for var in movies:
        ratings.append(var['rating'])
    sum_r = 0
    for i in ratings:
        sum_r = sum_r + i
    avg_rating = sum_r / len(ratings)
    print(f'Average Rating is: {avg_rating}')


def get_actor_movie_count(movie_actor):
    actor_movies = [] 
    for var in movies: 
        for i in range(len(var["actors"])):
            if var["actors"][i] == movie_actor: 
                actor_movies.append(var) 
    print(actor_movies)
    print(f"Toatal no of movies : {len(actor_movies)}")


def get_genre_movie_count(movie_genre):
    movies_genre = [] 
    for var in movies: 
        if var["genre"] == movie_genre: 
            movies_genre.append(var) 
    print(movies_genre)
    print(f"Toatal no of movies related to genre : {len(movies_genre)}")


def get_most_popular_genre():
    movie_genres = {}

    for var in movies:
        if var['genre'] in movie_genres:
            movie_genres[var['genre']] += 1
        else:
            movie_genres[var['genre']] = 1

    highest_count = 0
    highest_genre = ""

    for genre in movie_genres:
        if movie_genres[genre] > highest_count:
            highest_count = movie_genres[genre]
            highest_genre = genre

    print(highest_genre)
    print(highest_count)


def movie_recommendation(movie_language, movie_genre, movie_rating):
    for var in movies:
        if var['language']== movie_language and var['genre']==movie_genre and var['rating']>=movie_rating:
            print(var)
