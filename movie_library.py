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
            print("Movie is already rented")
            return False

    def return_movie(self):
        if self._is_rented:
            self._is_rented = False
            return True
        else:
            print("Movie is not rented")
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
            if movie.rent():
                print(movie.title, movie.director)

    def rent_movie(self, title):
        for movie in self._movies:
            if movie.title == title:
                if movie.rent():
                    print("Movie rented. Do enjoy your movie! 😊")
                return
        print("Movie not found. Try another movie 😊")

    def return_movie(self, title):
        for movie in self._movies:
            if movie.title == title:
                if movie.return_movie():
                    print("Movie returned. Thank you! 😊")
                return
        print("Wrong movies. Please return the actual movie rented out. 😒")
