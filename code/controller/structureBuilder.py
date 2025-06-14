import pandas as pd
import time
from model.structures.separateChainingHash import *
from model.structures.trie import *
from model.basic.movie import *
from model.basic.user import *
from model.basic.rating import *

from model.basic.movie_utils import *


class StructureBuilder:

    def __init__(self, moviesFilePath, ratingsFilePath, tagsFilePath):
        self.moviesFilePath = moviesFilePath
        self.ratingsFilePath = ratingsFilePath
        self.tagsFilePath = tagsFilePath

        self.trieTags = None
        self.trieMovies = None
        self.hashMovie: SeparateChainingHash
        self.hashUser: SeparateChainingHash

    def buildAll(self):
        self.buildMoviesStructure()
        self.buildUsersStructure()
        self.buildTagsStructure()


    def buildMoviesStructure(self):
        df = pd.read_csv(self.moviesFilePath)
        self.hashMovie = SeparateChainingHash(len(df))
        self.trieMovies = Trie()

        for row in df.itertuples():
            movie = Movie(row.movieId, row.title, row.genres, row.year)
            self.hashMovie.insertValue(movie)
            self.trieMovies.insert(row.title, row.movieId)
    

    def buildUsersStructure(self):
        df = pd.read_csv(self.ratingsFilePath)
        self.hashUser = SeparateChainingHash(140000)
        user: User = None

        for row in df.itertuples():
            movie: Movie = self.hashMovie.findById(row.movieId)

            if (user == None or user.id != row.userId):
                user = User(row.userId)
                self.hashUser.insertValue(user)

            rating = Rating(row.movieId, row.rating, row.date)
            user.addRating(rating)

            if (movie != None):
                movie.addRating(float(row.rating))

    def buildTagsStructure(self):
        df = pd.read_csv(self.tagsFilePath)
        self.trieTags = Trie()
        
        for row in df.itertuples():
            self.trieTags.insert(row.tag, row.movieId)