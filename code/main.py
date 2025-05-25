from controller.structureBuilder import *
import time

moviesFilePath = "../dados-trabalho-completo/movies.csv"
ratingsFilePath = "../dados-trabalho-completo/ratings.csv"
tagsFilePath = "../dados-trabalho-completo/tags.csv"

structureBuilder = StructureBuilder(moviesFilePath, ratingsFilePath, tagsFilePath)

begin = time.time()
structureBuilder.buildAll()
end = time.time()

print(f"Execution time: {end - begin:.4f} seconds")
