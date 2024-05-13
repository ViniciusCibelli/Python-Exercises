"""HERANÇA DE BUILT-IN --> como herdar apenas alguns comandos especificos de uma BUILD-IN:
        como herdar um built-in inteiro trás muita complexidade, o ideal seria fazer algo PARCIALMENTE
        para isso desfazemos a herança e, criar um comando dentro da classe usando o comando desejado e
        usar: @property para chamar o comando
   TRANSFORMAR UMA CLASSE IN ITERABLE --> usar #__getitem__(self, item)
        desta forma temos todas as vantagens de um iterável.
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
        series_and_movies.append(self)
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

    @property
    def size(self):
        return f"Your playlist has {len(self._programs)} TV Shows."


a = Series("The vampire diaries", 2013, 7)
b = Movie("batman begins", 2016, 120)
c = Movie("vinitchones e os 7 anões", 2022, 180)
d = Series("vinitchones macetando pp7 e vinitin", 2021, 5)

series_and_movies = []
a.give_like()
b.give_like()
c.give_like()
d.give_like()
d.give_like()

#series_and_movies = [a, b, c, d]

weekend = Playlist("weekend", series_and_movies)

for program in weekend:
    print(program)

print(weekend.size)
print(a in weekend)
print(weekend[0])
