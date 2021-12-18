class Person(object):

    def __init__(self, name=None, birth_year=None, death_year=None):
        self.__name = name
        self.__birth_year = birth_year
        self.__death_year = death_year

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def birth_year(self):
        return self.__birth_year

    @birth_year.setter
    def birth_year(self, new_birth_year):
        self.__birth_year = new_birth_year

    @property
    def death_year(self):
        return self.__death_year

    @death_year.setter
    def death_year(self, new_death_year):
        self.death_year = new_death_year
