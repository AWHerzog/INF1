class Movie:
    def __init__(self, title: str, actors: list, duration: int):
        if not title:
            raise Warning("Title is empty")
        if not actors and self.__class__.__name__ != 'MovieBox':
            raise Warning("Actors list is empty")
        if duration < 1:
            raise Warning("Duration must be at least 1 minute")
        self._title = title
        self._actors = actors
        self._duration = duration

    def __repr__(self) -> str:
        actors_str = ', '.join(f'"{actor}"' for actor in self._actors)
        return f'Movie("{self._title}", [{actors_str}], {self._duration})'
    
    def __str__(self) -> str:
        return f"Title = {self._title}, Actors = {self._actors}, Duration = {self._duration}"
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Movie):
            return (self._title == other._title and self._actors == other._actors and self._duration == other._duration)
        return False
    
    def __hash__(self):
        return hash((self._title, tuple(self._actors), self._duration))

    def get_title(self) -> str:
        return self._title

    def get_actors(self) -> list:
        return self._actors.copy()
    
    def get_duration(self) -> int:
        return self._duration
class MovieBox(Movie):
    def __init__(self, title: str, movies: list):
        if not title:
            raise Warning("Title is empty")
        if not movies:
            raise Warning("There are no movies in the box")
        for movie in movies:
            if not isinstance(movie, Movie):
                raise Warning("All items in the movie list must be of type Movie")
        super().__init__(title, [], sum(movie.get_duration() for movie in movies))
        self._movies = movies

    def __repr__(self):
        movies_str = ', '.join(repr(movie) for movie in self._movies)
        return f'MovieBox("{self._title}", [{movies_str}])'
    
    def __str__(self):
        return f"MovieBox = {self._title}, Movies = [{self._movies}]"

    def __eq__(self, other):
        if not isinstance(other, MovieBox):
            return False
        return (self._title == other._title and self._movies == other._movies)

    def __hash__(self):
        return hash((self._title, tuple(self._movies)))

    def get_title(self):
        return self._title

    def get_actors(self):
        actor_list = []
        for movie in self._movies:
            actor_list.extend(movie.get_actors())
        return sorted(list(set(actor_list)))
        
    def get_duration(self):
        return sum(movie.get_duration() for movie in self._movies)

    def get_movies(self):
        return self._movies.copy()

    

class Library:
    def __init__(self):
        self._movielist = []

    def add_movie(self, movie: Movie):
        if movie not in self._movielist:
            self._movielist.append(movie)

    def get_movies(self) -> list:
        movies = []
        seen_titles = set()
        
        def collect_movies(item):
            if isinstance(item, MovieBox):
                for movie in item.get_movies():
                    collect_movies(movie)
            elif isinstance(item, Movie):
                if item.get_title() not in seen_titles:
                    seen_titles.add(item.get_title())
                    movies.append(item)
        
        for item in self._movielist:
            collect_movies(item)
        
        return sorted(movies, key=lambda m: m.get_title())

    def get_total_duration(self) -> int:
        duration = 0
        for m in self._movielist:
            if isinstance(m, Movie):
                duration += m.get_duration()
            elif isinstance(m, MovieBox):
                duration += m.get_duration()
        return duration

    


a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
b = Movie("The Godfather", ["Brando", "Pacino"], 175)
c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
d = MovieBox("Top Movies", [b, c])

l = Library()
l.add_movie(a)
l.add_movie(d)
print(l.get_movies())
print(l.get_total_duration())

