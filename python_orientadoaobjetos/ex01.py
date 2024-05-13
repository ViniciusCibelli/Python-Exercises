class Data:

    def __init__(self, day, month, year):
        print("Construindo objeto...")
        self.day = day
        self.month = month
        self.year = year

    #def date(self):
        #print(f"{self.day}/{self.month:02}/{self.year}")

    def __str__(self):
        return (f"{self.day}/{self.month:02}/{self.year}")

class Retangulo:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__area = x * y

    def obter_area(self):
        return self.__area