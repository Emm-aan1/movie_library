class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director
        self._is_rented = False

    def rent(self):
        if not self._is_rented:
            self._is_rented = True
            return True
        else:
            return False

    def return_movie(self):
        if self._is_rented:
            self._is_rented = False
            return True
        else:
            return False

class MovieLibrary:
    def __init__(self):
        self._movies = []

    def add_movie(self, movie):
        self._movies.append(movie)

    def list_all_movies(self):
        for movie in self._movies:
            print(movie.title, movie.director)

    def list_available_movies(self):
        for movie in self._movies:
            if not movie._is_rented:
                print(movie.title, movie.director)

    def rent_movie(self, title):
        for movie in self._movies:
            if movie.title == title:
                if movie.rent():
                    print(f"Thank you for renting '{movie.title}'. 😊")
                else:
                    print(f"Sorry, '{movie.title}' is not available. 😞")
                return
        print(f"Movie '{title}' not found in the library. 😞")

    def return_movie(self, title):
        for movie in self._movies:
            if movie.title == title:
                if movie.return_movie():
                    print(f"Thank you for returning '{movie.title}'. 😊")
                else:
                    print(f"'{movie.title}' was not rented. 😐")
                return
        print(f"Movie '{title}' doesn't belong to us. 😒")