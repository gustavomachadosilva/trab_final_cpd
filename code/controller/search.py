from .structureBuilder import *
from model.basic.movie_utils import *
from model.basic.movie import *

class Search:

    def __init__(self, structureBuilder):
        self.structureBuilder: StructureBuilder = structureBuilder
    
    def searchMoviesByPrefix(self, prefix: str) -> list[Movie]:

        moviesList: list[Movie] = []

        for id in self.structureBuilder.trieMovies.search_prefix(prefix):
            movie: Movie = self.structureBuilder.hashMovie.findById(id)
            if movie:
                moviesList.append(movie)

        selection_sort_movies_by_global_rating(moviesList)

        return moviesList
    
    def searchByUserId(self, userId) -> list[Movie]:
        moviesList: list[Movie] = []

        user: User = self.structureBuilder.hashUser.findById(userId)
        if user is None:
            print("Usuário não encontrado!")
            return

        for rating in user.ratings:
            movie: Movie = self.structureBuilder.hashMovie.findById(rating.movieId)
            if movie:
                moviesList.append((movie, rating.value))

        selection_sort_by_rating_then_global(moviesList)     
        moviesList = moviesList[:20]

        return moviesList
    
    def searchByGenre(self, max, genre) -> list[Movie]:
        
        moviesList: list[Movie] = []

        for linkedList in self.structureBuilder.hashMovie.linkedLists:
            current = linkedList.head

            while (current != None):
                
                movie: Movie = current.value

                if (movie.ratingsCounter >= 1000):
                    movieHasGenre = False

                    genres = current.value.genres
                    genres = genres.split("|")

                    i = 0
                    while(i<len(genres) and movieHasGenre == False):
                        if (genres[i] == genre):
                            movieHasGenre = True
                        i += 1    
                    
                    if (movieHasGenre == True):
                        moviesList.append(movie)
                
                current = current.next

        selection_sort_movies_by_global_rating(moviesList)     
        moviesList = moviesList[:max]

        return moviesList

    
    def searchByTags(self, listOfTags) -> list[Movie]:
        moviesList: list[Movie] = []

        parts = self.formatTags(listOfTags)

        for tag in parts:
            for id in self.structureBuilder.trieTags.search_string(tag):
                movie: Movie = self.structureBuilder.hashMovie.findById(id)
                if movie:
                    moviesList.append(movie)

        moviesList = list(set(moviesList))

        selection_sort_movies_by_global_rating(moviesList)

        return moviesList

    def formatTags(listOfTags):

        parts = listOfTags.split(",")

        for i in range(len(parts)):
            parts[i] = parts[i].replace("'", "")
            parts[i].strip()
        
        return parts