import random
from datetime import date

#Klasa bazowa
class Base:
    def __init__(self, type_card, title, year):
        self.type_card = type_card
        self.title = title
        self.year = year
        
        


#Klasa movies
class Movieinformation(Base):
    def __init__(self, title, year, type, numplays):
        super().__init__("Movie",title, year)
        
        self.type = type
        self.numplays = numplays
        
          
    def play(self):
        self.numplays += 1
        return self.numplays

    def info(self):
        informations = self.title + "\t" + f"({str(self.year)})"
        return informations


#Klasa series
class Seriesinformation(Base):
    def __init__(self, title, year, type, episodenum, seasonnum, numplays):
        super().__init__("Series",title, year)
        self.typ = type
        self.episodenum = episodenum
        self.seasonnum = seasonnum
        self.numplays = numplays
    
    #Wyświetlenia
    def play(self):
        self.numplays += 1
        return self.numplays
    
    #Informacje
    def info(self):
        informations = self.title + " " + "S" + str(self.seasonnum) + "E" + str(self.episodenum)
        return informations



#Klasa biblioteki
class Library:
    movieserialsbase = []
    
    #Wyswietlanie series
    def get_series(self):
        print("Series list: ")
        for i in self.movieserialsbase:
            if i.type == 'Series':
                print(i)
            sorted(i)
    
    #Wyświetlanie movies
    def get_movies(self):
        print("Movies list: ")
        for i in self.movieserialsbase:
            if i.type == 'Movies':
                print(i)
            sorted(i)

    
    #Wyszukiwanie z listy
    def search(self):
        find = input("Find Movie or serial by its title: ")
        for i in self.movieserialsbase:
            if find == i.title:
                print(i.title)

    
    #Generowanie wyświetleń
    def generate_views(self):
        add_movies(self)
        movie.movies.title
        moviesample = random.sample(self.title,1)
        print(moviesample)
        seriessample = Seriesinformation.choice(self.title)
        seriessample.title = seriessample
        sample = random.sample(zip(moviesample,seriessample), 1)
        print(sample)
        
        #sample = random.sample(self.movieserialsbase(self.title), 1)
        #print(sample)
        #title = self.movieserialsbase)
        #numplay = title(self.numplays)
        #randomnum = random.randint(1,100)
        #numplay.append(randomnum)
        
                
        
    


    #Wyświetlenia *10
    def views_times_ten(self, generate_views):
        for i in range(11):
            generate_views()
            i += 1

    
    #Najpopularniejsze tytuły
    def top_titles(self):
        viewcount = 0
        content_type = input("Show top titles of movies or series? ")
        if content_type == 'Movies':
            for i in self.movieserialsbase:
                for x in range(4):
                    for y in self.movieserialsbase:
                        if y.type == 'Movies':
                            if i.numplays > viewcount:
                                viewcount += i.numplays
                                print(i.title)
                                x += 1
        elif content_type == 'series':
            for i in self.movieserialsbase:
                for x in range(4):
                    for y in self.movieserialsbase:
                        if y.type == 'Series':
                            if i.numplays > viewcount:
                                viewcount += i.numplays
                                print(i.title)
                                x += 1
    
    #Dodawanie movies
    def add_movies(self):
        movies_title = input("Ttile of movie: ")
        movies_year = int(input("Movie year: "))
        movies_type = input("Movie type: ")
        movie_numplays = random.randint(1,100)
        newMovie = Movieinformation(movies_title, movies_year, movies_type, movie_numplays)
        self.movieserialsbase.append(newMovie)

        
        
    #Dodawanie series        
    def add_series(self):
        series_title = input("Title of series: ")
        series_year = int(input("Series year: "))
        series_type = input("Series type: ")
        series_season = int(input("Series season numbers: "))
        series_episode = int(input("Series episode numbers: "))
        series_numplays = random.randint(1,100)
        newSeries = Seriesinformation(series_title, series_year, series_type,series_season, series_episode, series_numplays)
        self.movieserialsbase.append(newSeries)    
        
    
    #Pokazanie listy movieserialsbase
    def show_library(self):
        print("Library of movies and series: ")
        for i in self.movieserialsbase:
            if i.type_card == 'Movie':
                print(i.info())
            elif i.type_card == 'Series':
                print(i.info())
        




def main():
    library = Library()
    today = date.today()
    fdate = date.today().strftime('%d/%m/%y')
    option = input(("Which one do you want to add (movies/series): "))
    
    if option == 'movies':
        quantity = int(input("How many do you want to add? "))
        for i in range(quantity):
            library.add_movies()
    
    elif option == 'series':
        quantity = int(input("How many do you want to add? "))
        for i in range(quantity):
            library.add_series()    
    
    print("Movie library: ")
    library.show_library()

    
    library.generate_views()
    print(f"The most popular movies and series of the day {fdate}")
    #library.top_titles()


if __name__ == "__main__":
    main() 
