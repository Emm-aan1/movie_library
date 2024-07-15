from movie_library import MovieLibrary, Movie

def test_movie_library():
    # Create a movie library
    movie_library = MovieLibrary()

    # Add movies to the library
    movie_library.add_movie(Movie("The Shawshank Redemption", "Frank Darabont"))
    movie_library.add_movie(Movie("The Godfather", "Francis Ford Coppola"))
    movie_library.add_movie(Movie("The Dark Knight", "Christopher Nolan"))
    movie_library.add_movie(Movie("Pulp Fiction", "Quentin Tarantino"))

    # List all movies
    print("All movies in the library:")
    movie_library.list_all_movies()

    # List available movies
    print("\nAvailable movies in the library:")
    movie_library.list_available_movies()

    # Rent a movie
    print("\nRenting 'The Godfather':")
    movie_library.rent_movie("The Godfather")

    # List available movies after renting one
    print("\nAvailable movies after renting 'The Godfather':")
    movie_library.list_available_movies()

    # Try to rent a movie that is already rented
    print("\nTrying to rent 'The Godfather' again:")
    movie_library.rent_movie("The Godfather")

    # Return a movie
    print("\nReturning 'The Godfather':")
    movie_library.return_movie("The Godfather")

    # List available movies after returning one
    print("\nAvailable movies after returning 'The Godfather':")
    movie_library.list_available_movies()

    # Try to return a movie that isn't rented
    print("\nTrying to return 'The Godfather' again:")
    movie_library.return_movie("The Godfather")

    # Try to rent a movie that doesn't exist
    print("\nTrying to rent a non-existent movie 'Inception':")
    movie_library.rent_movie("Inception")

    # Try to return a movie that doesn't exist
    print("\nTrying to return a non-existent movie 'Inception':")
    movie_library.return_movie("Inception")

if __name__ == "__main__":
    test_movie_library()