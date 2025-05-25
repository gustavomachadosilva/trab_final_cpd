import pandas as pd
import time
from model.structures.separateChainingHash import *
from model.basic.movie import *
from model.basic.user import *
from model.basic.rating import *

class StructureBuilder:

    def __init__(self, moviesFilePath, ratingsFilePath, tagsFilePath):
        self.moviesFilePath = moviesFilePath
        self.ratingsFilePath = ratingsFilePath
        self.tagsFilePath = tagsFilePath

    def buildAll(self):
        self.buildMoviesStructure()

        begin = time.time()
        self.buildUsersStructure()
        end = time.time()

        print(f"user builder execution time: {end - begin:.4f} seconds")


    def buildMoviesStructure(self):
        df = pd.read_csv(self.moviesFilePath)
        hash = SeparateChainingHash(len(df))

        for row in df.itertuples():
            movie = Movie(row.movieId, row.title, row.genres, row.year)
            hash.insertValue(movie)
    

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

