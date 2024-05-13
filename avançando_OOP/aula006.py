"""PYTHON DATA MODEL (Dunder Methods): métodos para serem implementados e dar mais funcionalidades as classes
    Para adicionar propriedade de tamanho na classe usar: def __len__(self):
    Transformar uma classe em uma sequência --> usar #__getitem__(self, item)
    EXISTEM DIVERSOS -- PESQUISAR MAIS QUANDO NECESSÁRIO...
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


class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __getitem__(self, item):
        return self._programs[item]

    @property
    def list(self):
        return self._programs

    def __len__(self):
        return len(self._programs)


a = Series("The vampire diaries", 2013, 7)
b = Movie("batman begins", 2016, 120)
c = Movie("vinitchones e os 7 anões", 2022, 180)
d = Series("vinitchones macetando pp7 e vinitin", 2021, 5)

series_and_movies = [a, b, c, d]

weekend = Playlist("weekend", series_and_movies)

for program in weekend:
    print(program)

print(f"Your playlist has {len(weekend)} TV shows")
