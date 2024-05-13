"""
HERDAR UM COMPORTAMENTO DE UM COMANDO ITERABLE/BUILT-IN --> exemplo: herdar os comandos de uma list:
   class Nome(list):
        super().__init__(variavel)
Isso faz com que um objeto herde os comandos que podem ser utilizados em um objeto iterable, consequentemente
    poupa uma quantidade absurda de comandos que devem ser feitos.
    tomar cuidado pois não se sabe todos os comandos existentes.
"""


class Shows:
    def __init__(self, name, year):
        self._name = name.title()
        self._year = year
        self._likes = 0

    @property
    def name(self):
        return f"The TV show's name is: {self._name}"

    @name.setter
    def name(self, new_name):
        self._name = new_name
        print(f"You changed the show's name to: {new_name.title()}")

    @property
    def year(self):
        return f"The show was released in {self._year}"

    def give_like(self):
        self._likes += 1
        print(f"You give a like to the show: {self._name}")

    @property
    def likes(self):
        return f"{self._name}, already got {self._likes} like(s)!"

    def __str__(self):
        return f" {self._name} was released in {self._year} and have {self._likes} likes."


class Movie(Shows):

    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self._duration = duration
        print(f"Creating object ... {self._name}")

    @property
    def duration(self):
        return f"The movie has about {self._duration} minutes"

    def __str__(self):
        return f" {self._name} was released in {self._year}, have {self._duration} minutes and have " \
               f"{self._likes} likes."


class Series(Shows):

    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self._seasons = seasons
        print(f"Creating object ... {self._name}")

    @property
    def seasons(self):
        return f"The serie has about {self._seasons} seasons"

    def __str__(self):
        return f" {self._name} was released in {self._year}, have {self._seasons} seasons and have {self._likes} likes."


class Playlist(list):
    def __init__(self, name, programs):
        self.name = name
        super().__init__(programs)


a = Series("The vampire diaries", 2013, 7)
b = Movie("batman begins", 2016, 120)
c = Movie("vinitchones e os 7 anões", 2022, 180)
d = Series("vinitchones macetando pp7 e vinitin", 2021, 5)

a.give_like()
b.give_like()
c.give_like()
d.give_like()
d.give_like()

series_and_movies = [a, b, c, d]

weekend = Playlist("weekend", series_and_movies)

print(f"Tamanho da playlist: {len(weekend)}")

for program in weekend:
    print(program)
