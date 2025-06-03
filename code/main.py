from view.app import *
from controller.structureBuilder import *

# moviesFilePath = "../dados-trabalho-completo/movies.csv"
# ratingsFilePath = "../dados-trabalho-completo/ratings.csv"
# tagsFilePath = "../dados-trabalho-completo/tags.csv"

# No meu precisa ser assim para funcionar
moviesFilePath = "dados-trabalho-completo/movies.csv"
ratingsFilePath = "dados-trabalho-completo/ratings.csv"
tagsFilePath = "dados-trabalho-completo/tags.csv"

structureBuilder = StructureBuilder(moviesFilePath, ratingsFilePath, tagsFilePath)

from view.app import *
from controller.structureBuilder import *

app = App(structureBuilder=structureBuilder)
app.mainloop()
