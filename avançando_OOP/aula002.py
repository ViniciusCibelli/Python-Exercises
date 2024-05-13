"""POLIMORFISMO --> USAMOS POLIMORFISMO PARA PERCORRER UMA LISTA USANDO MAIS DE UM TIPO DE OBJETO
   QUE PERTENCEM AO MESMO SUPERTIPO"""


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


class Movie(Shows):

    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self._duration = duration
        print(f"Creating object ... {self._name}")

    @property
    def duration(self):
        return f"The movie has about {self._duration} minutes"

    def print(self):
        print(f" {self._name} was released in {self._year}, have {self._duration} minutes and have {self._likes} likes.")


class Series(Shows):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self._seasons = seasons
        print(f"Creating object ... {self._name}")

    @property
    def seasons(self):
        return f"The serie has about {self._seasons} seasons"

    def print(self):
        print(f" {self._name} was released in {self._year}, have {self._seasons} seasons and have {self._likes} likes.")


a = Series("The vampire diaries", 2013, 7)
a.give_like()
b = Movie("batman begins", 2016, 120)
b.give_like()

series_and_movies = [a, b]
for program in series_and_movies:
    program.print()
