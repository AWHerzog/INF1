
class Movie:
    def __init__(self, title, actors, duration):
        if not title:
            raise Warning("Title cannot be empty")
        self._title = title

        if not actors:
            raise Warning("Actor list cannot be empty")
        self._actors = actors

        if duration < 1:
            raise Warning("Duration must be at least 1 minute")
        self._duration = duration

    def get_title(self):
        return self._title

    def get_actors(self):
        return self._actors

    def get_duration(self):
        return self._duration

    def __repr__(self):
        actors_repr = "[" + ", ".join(f'"{actor}"' for actor in self._actors) + "]"
        return f'Movie("{self._title}", {actors_repr}, {self._duration})'

    def __eq__(self, other):
        return isinstance(other, Movie) and self._title == other._title

    def __hash__(self):
        return hash((self._title, tuple(self._actors), self._duration))
    

class MovieBox:
    def __init__(self, title, movies):
        if not title:
            raise Warning("Title cannot be empty")
        self._title = title

        if not movies:
            raise Warning("Movies list cannot be empty")
        for movie in movies:
            if not isinstance(movie, Movie):
                raise Warning("All items in movies list must be instances of Movie or its subclass")
        self._movies = movies

    def get_title(self):
        return self._title

    def get_actors(self):
        all_actors = set()
        for movie in self._movies:
            all_actors.update(movie.get_actors())
        return sorted(all_actors)

    def get_duration(self):
        return sum(movie.get_duration() for movie in self._movies)

    def get_movies(self):
        return self._movies

    def __repr__(self):
        movies_repr = "[" + ", ".join(repr(movie) for movie in self._movies) + "]"
        return f'MovieBox("{self._title}", {movies_repr})'

    def __eq__(self, other):
        return isinstance(other, MovieBox) and self._title == other._title and self._movies == other._movies

    def __hash__(self):
        return hash((self._title, tuple(self._movies)))
    

class Library:
    def __init__(self):
        self._movies = set()

    def add_movie(self, movie):
        if isinstance(movie, Movie) or isinstance(movie, MovieBox):
            self._movies.add(movie)
        else:
            raise TypeError("Only Movie or MovieBox instances can be added.")

    def get_total_duration(self):
        total_duration = 0
        for movie in self._movies:
            total_duration += movie.get_duration()
        return total_duration

    def get_movies(self):
        unique_movies = set()
        for item in self._movies:
            if isinstance(item, Movie):
                unique_movies.add(item)
            elif isinstance(item, MovieBox):
                unique_movies.update(item.get_movies())

        return sorted(unique_movies, key=lambda movie: movie.get_title())
    


a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
b = Movie("The Godfather", ["Brando", "Pacino"], 175)
c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
d = MovieBox("Top Movies", [b, c])

l = Library()
l.add_movie(a)
l.add_movie(d)
print(l.get_movies())
print(l.get_total_duration())

