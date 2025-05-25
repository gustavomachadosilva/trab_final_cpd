from .rating import *

class User:

    def __init__(self, id):
        self.id = id
        self.ratings: list[Rating] = []
    
    def addRating(self, rating):
        self.ratings.append(rating)