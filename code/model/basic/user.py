class User:

    def __init__(self, id):
        self.id = id
        self.ratings = []
    
    def addRating(self, rating):
        self.ratings.append(rating)