class Movie:

    sumRatings: float = 0.0
    ratingsCounter: int = 0

    def __init__(self, id: int, title: str, genres: str, year: int) -> None:
        self.id = id
        self.title = title
        self.genres = genres
        self.year = year
        
    def addRating(self, rating: float):
        self.ratingsCounter += 1
        self.sumRatings += rating

    def getGlobalRating(self) -> float:
        return self.sumRatings / float(self.ratingsCounter)