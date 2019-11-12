# movie database

"""
- Enter 'a' to add a movie,
- Enter 'l' to see your movies,
- Enter 'f' to find a movie
- Enter 'q' to quit.
- Add movies
- See movies
- Find a movie
- Stop running the program

Tasks:
[x]: Where to store the movies
[x]: What is the format of a movie
    movie = {
        'name': ... (str),
        'director': ... (str),
        'year': ... (int)
    }
[x]: Show the user the main interface and get their input
[x]: Allow users to add movies
[]: Show all of their movies
[]: Find a movie
[x]: Stop running the program when they type 'q'.

"""
movies = []


def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, 'q' to quit. ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print("Unknown command, please try again")

        user_input = input("\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, 'q' to quit. ")


def add_movie():
    name = input("Enter the movie name: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def show_movies(movies):
    for movie in movies:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")


def find_movie():
    find_by = input("What property of the movie are you looking for [name, director, or year]? ")  # one name, director, or year
    looking_for = input("What are you searching for? ")

    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    show_movies(found_movies)


def find_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)

    return found


menu()

print(movies)
