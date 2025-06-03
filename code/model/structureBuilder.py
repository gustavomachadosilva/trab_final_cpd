import pandas as pd
import time
from .structures.separateChainingHash import *
from .structures.trie import *
from .basic.movie import *
from .basic.user import *
from .basic.rating import *

class StructureBuilder:

    def __init__(self, moviesFilePath, ratingsFilePath, tagsFilePath):
        self.moviesFilePath = moviesFilePath
        self.ratingsFilePath = ratingsFilePath
        self.tagsFilePath = tagsFilePath
        self.moviesTrie = None
        self.moviesHash = None

    def buildAll(self):
        self.buildMoviesStructure()

        begin = time.time()
        self.buildUsersStructure()
        end = time.time()

        for id in self.moviesTrie.search_prefix("America"):
            print(self.moviesHash.findById(id))

        print(f"user builder execution time: {end - begin:.4f} seconds")


    def buildMoviesStructure(self):
        df = pd.read_csv(self.moviesFilePath)
        hash = SeparateChainingHash(len(df))
        trie = Trie()

        for row in df.itertuples():
            movie = Movie(row.movieId, row.title, row.genres, row.year)
            hash.insertValue(movie)
            trie.insert(row.title, row.movieId)

        self.moviesTrie = trie
        self.moviesHash = hash
    

    def buildUsersStructure(self):
        df = pd.read_csv(self.ratingsFilePath)
        hash = SeparateChainingHash(140000)
        user: User = None

        for row in df.itertuples():
            movie: Movie = hash.findById(row.movieId)

            if (user == None or user.id != row.userId):
                user = hash.findById(row.userId)

            if (user == None):
                user = User(row.userId)
                hash.insertValue(user)

            rating = Rating(row.movieId, row.rating, row.date)
            user.addRating(rating)

            if (movie != None):
                movie.addRating(float(row.rating))

