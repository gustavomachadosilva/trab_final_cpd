from view.app import *
from controller.structureBuilder import *

moviesFilePath = "dados-trabalho-completo/movies.csv"
ratingsFilePath = "dados-trabalho-completo/ratings.csv"
tagsFilePath = "dados-trabalho-completo/tags.csv"

structureBuilder = StructureBuilder(moviesFilePath, ratingsFilePath, tagsFilePath)
structureBuilder.buildAll()

app = App(structureBuilder=structureBuilder)
app.mainloop()