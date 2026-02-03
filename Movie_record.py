import csv
import os
from fileinput import close

Genres = {
          "1":"Romantic",
          "2":"Action",
          "3":"Supernatural",
          "4":"Superhero",
          "5":"Comedy",
          "6":"Animated",
          "7":"Science Fiction",
          "8":"Biography",
          "9":"Children's",
          "10":"Fantasy",
          "11":"Horror",
          "12":"Thriller",
          "13":"Documentary",
          "14":"Drama",
          "15":"Musical",
          "16":"Historical",
          "17":"Crime",
          "18":"SitCom",
          "19":"Western",
          "20":"Mystery",
          "21":"War",
          }
Country = {
          "0":"N/A",
          "1":"England",
          "2":"France",
          "3":"Germany",
          "4":"Italy",
          "5":"America",
          "6":"Australia",
          "7":"Canada",
          "8":"Japan",
          "9":"Türkiye",
          "10":"India",
          "11":"Russia",
          "12":"Ireland",
          "13":"China"
}
Rating = {
            "0":"N/A",
            "1":"⭐        ",
            "2":"⭐⭐      ",
            "3":"⭐⭐⭐    ",
            "4":"⭐⭐⭐⭐  ",
            "5":"⭐⭐⭐⭐⭐"
}

Movies = {}
TvSeries = {}
Anime = {}

#------------------------------------------------------------------------------------------
def movies():
    def add_movie():
        read_movies()
        while True:
            try:
                movie_count = int(input("How many movies do you want to add? : "))
                for _ in range(movie_count):
                    while True:
                        title = input("Enter the movie title: ").strip()

                        if title in ["q","quit"]:
                            print("You choose to quit from entering a movie to the database.")
                            return

                        if title in Movies:
                            print("Movie title is already stored in database")
                        elif len(title) <= 4:
                            print("Movie title is too short")
                            print("Please enter a valid movie title")
                        else:
                            while True:
                                try:
                                    while True:
                                        y = input("Enter the movie year: ").strip()
                                        if len(y) < 4:
                                            print("Movie year is too short")
                                        elif not y.isdigit():
                                            print("Movie year must be an integer")
                                        else:
                                            year = y
                                            break

                                    while True:
                                        r = input("Enter the movie rating: ").strip()
                                        if r in ["1", "2", "3", "4", "5"]:
                                            rate = r
                                            break
                                        else:
                                            print("Movie rating must be between 1 and 5")

                                    while True:
                                        for i in Country:
                                            if 10 > int(i) > 0:
                                                print(f"0{i}. {Country[i]}")
                                            elif int(i) >= 10:
                                                print(f"{i}. {Country[i]}")

                                        c = input("Enter the country movie was produced : ").strip()
                                        if c in Country.keys():
                                            country = c
                                            print(f"`{title}` was produced in `{Country[c]}`")
                                            break
                                        else:
                                            print("Please enter a valid country code.")


                                    count = int(input("How many genres this movie has? "))
                                    print("\n----------------------------------------------")
                                    print("             ----- Genres ----                ")
                                    print("----------------------------------------------\n")
                                    for k in Genres:
                                        print(f"{k}. {Genres[k]}")
                                    print("\n----------------------------------------------\n")



                                    selected_genres = []
                                    for _ in range(count):
                                        while True:
                                            gen = input("Enter the movie genre number: ").strip()
                                            if gen in Genres:
                                                if gen not in selected_genres:
                                                    print(f"You added `{title}` to the `{Genres[gen]}` genre.")
                                                    selected_genres.append(gen)
                                                    break
                                                else:
                                                    print("You already entered this genre.")
                                            else:
                                                print("Invalid genre number.")
                                    Movies[title] = [year] + [country] + [rate] + selected_genres

                                    print("\nYou added ---->")
                                    print(f"{title:25} -> {', '.join(Genres[g] for g in selected_genres)}")

                                    write_movies()
                                    break
                                except ValueError:
                                    print("Please enter a valid integer")
                            break
                break
            except ValueError:
                print("Invalid input. Please try again.")

    def write_movies():
        with open("Movies.csv", "w", newline="") as csvfile:  # clear file safely

            writer = csv.writer(csvfile)
            for title in Movies:
                writer.writerow([title] + Movies[title])

    def read_movies():
        Movies.clear()
        with open("Movies.csv", "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:
                    title = row[0]
                    year = row[1]
                    country = row[2]
                    rating = row[3]
                    genre_ids = [g.strip() for g in row[4:] if g.strip()]
                    Movies[title] = [year] + [country] + [rating] + genre_ids

    def print_movies():
        read_movies()
        print("\n----------------------------------------------")
        print("     --- Movies in the movie database ---     ")
        print("----------------------------------------------\n\n")

        name = "Movie"
        ge = "Genre"
        y = "Year"
        con = "Country"
        r = "Rating"
        for j in range(137):
            print("-",end="")

        print(f"  {name:^58}  | {y:^10}  |{con:^13}|{r:^10}|{ge:^35}")

        for j in range(137):
            print("-",end="")
        print()

        i = 1
        for title,data in Movies.items():
            year = data[0]
            country = data[1]
            rating = data[2]
            genre_ids = data[3:]
            genre_names = [Genres[genre_id] for genre_id in genre_ids if genre_id in Genres]
            if i < 10:
                print(f" 0{i:1}. {title:58}  {year:13} {Country[country]:<10} {Rating[rating]} {', '.join(genre_names)}")
            else:
                print(f"{i:3}. {title:58}  {year:13} {Country[country]:<10} {Rating[rating]} {', '.join(genre_names)}")
            i =  i + 1

        for j in range(125):
            print("-",end="")
        print()

        count = i - 1
        print(f"Number of movies in the database are {count}")

        for j in range(125):
            print("-",end="")
        print()

        input("Press enter to continue...\n\n")

    def search_by_year():
        while True:
            try:
                choice = input("\nEnter the movie year: ")
                if len(choice) < 4:
                    print("Please enter a valid year")
                elif choice.isdigit():
                    y = choice
                    read_movies()

                    print("\n----------------------------------------------")
                    print(f"         Movies Released in {y}")
                    print("----------------------------------------------\n")
                    i = 1
                    for title, data in Movies.items():
                        year = data[0]
                        if y == year:
                            if i < 10:
                                print(f" 0{i}. {title}")
                            else:
                                print(f"{i:3}. {title}")
                            i += 1
                    j = i - 1
                    print("\n----------------------------------------------")
                    print(f"In the year `{y}`, `{j}` movies were released.")
                    print("----------------------------------------------")
                    input("\nPress enter to continue...\n\n")
                    break
                else:
                    print("Invalid input.\nPlease try again.")
            except ValueError:
                print("Invalid input.\nPlease try again.")

    def search_by_name():
        read_movies()
        while True:
            letter = input("\nEnter the first letter: ").capitalize()
            print()

            if letter.lower() in ["quit","exit"]:
                break

            elif len(letter) > 1:
                print("\nMovie Details")
                i = 1
                for title, data in Movies.items():
                    if letter.lower() in title.lower():
                        gen = data[3:]

                        if i < 10:
                            print(f"Movie No. 0{i}")
                        else:
                            print(f"Movie No. {i}")

                        print(f"Movie         : {title}\n"
                              f"Released year : {data[0]}\n"
                              f"Country       : {Country[data[1]]}\n"
                              f"Rating        : {Rating[data[2]]}")

                        print("Genres        : ", end="")
                        genre_names = [Genres[j] for j in gen if j in Genres]  # Map IDs to names
                        print(", ".join(genre_names))
                        print()

                        i+=1

                if i == 1:
                    print(f"The are 0 movies with `{letter}` in the database.")

                input("Press enter to continue...\n\n")


            elif len(letter) == 1:
                i = 0
                print(f"Movies with the starting letter `{letter.upper()}`")
                print("-------------------------------------")
                for title, data in Movies.items():
                    if title[0] == letter.capitalize():
                        print(title)
                        i = i + 1
                print()

                if i < 1:
                    print(f"There are zero movies with letter starting with `{letter}`.\n")
                input("Press enter to continue...\n\n")

            else:
                print("Invalid input.\nPlease try again.\n")

    def search_by_genre():
        read_movies()

        def find():
            print(f"You choose {Genres[genre]} genre.")
            i = 1
            for title, data in Movies.items():
                if genre in data[1:]:
                    if i < 10:
                        print(f" 0{i}. {title}")
                    else:
                        print(f"{i:3}. {title}")
                    i = i + 1

            input("Press enter to continue...\n\n")

        while True:
            print("\n----------------------------------------------")
            print("             ----- Genres ----                ")
            print("----------------------------------------------\n")
            for k in Genres:
                print(f"{k}. {Genres[k]}")
            print("\n----------------------------------------------\n")

            genre = input("Enter the genre : ").capitalize()

            if genre.lower() in ["q","quit"]:
                break

            match genre:
                case "01"|"1"|"Romantic":
                    find()
                case "02"|"2"|"Action":
                    find()
                case "03"|"3"|"Supernatural":
                    find()
                case "04"|"4"|"Superhero":
                    find()
                case "05"|"5"|"Comedy":
                    find()
                case "06"|"6"|"Animated":
                    find()
                case "07"|"7"|"Science Fiction":
                    find()
                case "08"|"8"|"Biography":
                    find()
                case "09"|"9"|"Children;s":
                    find()
                case "10"|"Fantasy":
                    find()
                case "11"|"Horror":
                    find()
                case "12"|"Thriller":
                    find()
                case "13"|"Documentary":
                    find()
                case "14"|"Drama":
                    find()
                case "15"|"Musical":
                    find()
                case "16"|"Historical":
                    find()
                case _:
                    print("Invalid input.\nPlease try again.")

    def search():
        while True:
            print("\n\n----------------------------------------------")
            print("          -----  Search Menu  -----           ")
            print("----------------------------------------------")
            print("01. Search for movies released in a specific year.\n02. Search for movies by name.\n03. Search for movies in Genres\n04. Super Search\n05. Exit search menu")
            choice = input("Enter your choice : ").capitalize().strip()
            print("----------------------------------------------\n")

            if choice in ["01", "1"]:
                print("You chose to search movies released in a specific year.")
                print("----------------------------------------------\n")
                search_by_year()
            elif choice in ["02", "2"]:
                print("You chose to search movies by name.")
                print("----------------------------------------------\n")
                search_by_name()
            elif choice in ["03", "3"]:
                print("You chose to search movies in Genres.")
                print("-----------------------------------------------\n")
                search_by_genre()
            elif choice in ["04", "4"]:
                print("You chose to search movies using Super Search.")
                print("------------------------------------------------\n")
                super_search()
            elif choice in ["05", "5"]:
                print("You chose to exit search menu.")
                print("----------------------------------------------")
                break
            else:
                print("Invalid input.\nPlease try again.\n")

    def sort_alphabetically():
        read_movies()
        # alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

        # i = 1
        # for title, data in Movies.items():
        #     try:
        #         title_1 = title[0].lower()
        #         inter = alphabet.index(title_1)
        #         print(inter)
        #     except ValueError:
        #         print(title)

        one = None
        sort = sorted(Movies.keys())
        for movie in sort:
            two = movie[0]
            if two.isalpha():
                if one != two :
                    one = two
                    print(f"\n{movie[0]}\n----------------------")
            else:
                print("#")

            print(movie)

        input("\nPress Enter to continue...\n\n")

    def super_search():
        while True:
            user_in = input("What are the criteria you would like to search for? \n01. Multiple Genres\n02. Genre & Country\n03. Genre & Country & Year\n04. Genre & Country & Year & Rating\n05. Exit the super search\nEnter your choice : ")

            if user_in.lower() in ["05", "5","exit the super search","exit"]:
                break

            match user_in:
                case "01"|"1"|"multiple genres":
                    search_printer(user_in)
                case "02"|"2":
                    search_printer(user_in)
                case "03"|"3":
                    search_printer(user_in)
                case "04"|"4":
                    print()
                    genre_country_year_n_rating()
                    print()
                    input("\nPress Enter to continue...")
                case _:
                    print("Invalid input.\nPlease try again.")

    def search_printer(user_in):
        listing = []
        if user_in.lower() in ["01", "1"]:
            listing = multiple_genres()
        elif user_in.lower() in ["02", "2"]:
            listing = genre_n_country()
        elif user_in.lower() in ["03", "3"]:
            listing = genre_country_n_year()

        print()
        if listing.__len__() != 0:
            for i in listing:
                print(i)
            print()
            input("\nPress Enter to continue...")
        else:
            print("There are 0 movies with this criteria in the database.")

    gen = []
    super_search_movies = []

    def multiple_genres():
        read_movies()

        while True:
            count = input("How many genres do you want to use for the search? ")
            if count.isdigit() :
                if 0 < int(count) < 20:
                    count = int(count)
                    break
            else:
                print("Please enter a number between 1 and 20")

        for i in Genres.keys():
            if int(i) < 10:
                print(f"0{i}  {Genres[i]}")
            else:
                print(f"{i}  {Genres[i]}")

        print()
        for j in range(count):
            while True:
                genre = input(f"0{j+1}. Enter a genre id or name : ")
                if genre in Genres.keys():
                    gen.append(genre)
                    break
                elif genre in Genres.values():
                    for key,value in Genres.items():
                        if genre.lower() == value.lower():
                            gen.append(key)
                    break
                else:
                    print("Invalid input.\nPlease enter a valid genre id or genre name.")
            j += 1

        print()
        print(f"The {count} genres you chose to search your movies by are",end=" ")
        for k in gen:
            print(f"{Genres[k]}",end=",")
        print()
        print()

        gen_movie = []
        for title, data in Movies.items():
            movie_genres = data[3:]
            if all(g in movie_genres for g in gen):
                gen_movie.append(title)

        return gen_movie

    def genre_n_country():
        read_movies()
        multiple_genres()

        for i in Country:
            if int(i) < 10:
                print(f"0{i}. {Country[i]}")
            else:
                print(f"{i}. {Country[i]}")

        while True:
            country = input("\nEnter a country id or country : ")
            if country in Country.keys():
                country = int(country)
                break
            elif country in Country.values():
                for key,value in Country.items():
                    if country == value:
                        country = int(key)
                break
            else:
                print("Invalid input.\nPlease enter a valid country id or country name.")

        print(f"The country is {Country[str(country)]}.")

        country_movie = []
        for title, data in Movies.items():
            movie_genres = data[3:]
            if country == int(data[1]):
                if all(g in movie_genres for g in gen):
                    super_search_movies.append(title)
                    country_movie.append(title)

        return country_movie

    def genre_country_n_year():
        read_movies()
        genre_n_country()
        print()
        movie_years = []

        for title, data in Movies.items():
            movie_years.append(data[0])

        movie_years.sort()
        min_year = movie_years[0]
        max_year = movie_years[-1]

        while True:
            year = input(f"\nEnter the year you want to search for (min year {min_year}) - (max year {max_year}) : ")
            if year in movie_years:
                print(f"The year you chose for the search is {year}.")
                break
            else:
                print("The year you chose for the search is invalid.")
        year_movies = []
        for title, data in Movies.items():
            for titles in super_search_movies:
                if title in titles:
                    if year == data[0]:
                        super_search_movies.remove(titles)
                        year_movies.append(title)

        return year_movies

    def genre_country_year_n_rating():

        while True:
            choice = input("How do you want to search using ratings?"
                           "01. One Rating"
                           "02. Rating Range")

            if choice in ["1","01","one rating"]:
                one_rating()
                break
            elif choice in ["2","02","rating range"]:
                rating_range()
                break
            else:
                print("Invalid input.\nPlease try again.")

    def one_rating():
        read_movies()
        genre_country_n_year()

        for i in Rating:
            print(f"0{i}. {Rating[i]}")

        while True:
            rate = input("\nEnter rating you want to search for : ")
            if rate.isdigit() and 0 <= int(rate) < 6:
                print(f"Rating you chose for the search is {Rating[rate]}.")
                break
            else:
                print("Invalid input.\nPlease enter a number between 0 and 6.")
        k = 0
        for title, data in Movies.items():
            for titles in super_search_movies:
                if title == titles:
                    if rate == data[2]:
                        super_search_movies.append(title)
                        k += 1
        if k < 1:
            print("No movies were found.")

    def rating_range():
        read_movies()
        genre_country_n_year()

        for i in Rating:
            print(f"0{i}. {Rating[i]}")
        print()

        while True:
            min_rate = input("\nEnter lowest rating you want to use for the search : ")
            if min_rate.isdigit() and 0 <= int(min_rate) < 6:
                print(f"The lowest rating you chose for the search is {Rating[min_rate]}.")
                break
            else:
                print("Invalid input.\nPlease enter a number between 0 and 6.")

        while True:
            max_rate = input("\nEnter highest rating you want to use for the search : ")
            if max_rate.isdigit() and 0 <= int(max_rate) < 6:
                if int(max_rate) > int(min_rate):
                    print(f"The highest rating you chose for the search is {Rating[max_rate]}.")
                    break
                else:
                    print(f"The highest rating must be greater than {min_rate}.")
            else:
                print("Invalid input.\nPlease enter a number between 0 and 6.")

        k = 0
        for title, data in Movies.items():
            for titles in super_search_movies:
                if title == titles:
                    if min_rate >= data[2] >= max_rate:
                        super_search_movies.append(title)
                        k += 1

        if k < 1:
            print("No movies were found.")

    def main_movie():
        while True:
            print("----------------------------------------------")
            print("  -----  Welcome to Movies Recorder  -----    ")
            print("----------------------------------------------")
            print("01. Enter a movie to the database")
            print("02. Print the all the movies in the database")
            print("03. Search for a movie")
            print("04. Sort the movies alphabetically")
            print("05. Exit")
            print("----------------------------------------------")
            choice =  input("Enter your choice: ").strip().capitalize()
            print("\n----------------------------------------------")

            match choice:
                case "1"|"01":
                    print("You choose to add movies to the database")
                    print("----------------------------------------------")
                    add_movie()
                case "2"|"02":
                    print("You choose to see all movies in the database")
                    print("----------------------------------------------")
                    print_movies()
                case "3"|"03":
                    print("You choose to search for a movie")
                    print("-----------------------------------------------")
                    search()
                case "4"|"04":
                    print("You choose to sort the movies alphabetically.")
                    print("-----------------------------------------------")
                    sort_alphabetically()
                case "5"|"05":
                    print("You choose to exit from the program")
                    print("----------------------------------------------")
                    print("Bye bye!")
                    break
                case _:
                    print("Invalid input.\nPlease try again.")

    if __name__ == '__main__':
        main_movie()

def tv_series(current_type):

    if current_type == "tv":
        file = "TvSeries.csv"
        dict = TvSeries
    else:
        file = "AnimeShows.csv"
        dict = Anime

    def add_tv():
        read_tv()
        while True:
            try:
                count = input(f"How many {current_type} series do you want to add? ")
                print()
                if count.isdigit():
                    count = int(count)
                    if count > 0:
                        print(f"\nYou choose to add {count} {current_type} series to the database\n")
                        for i in range(count):
                            while True:

                                title = input(f"\n{i+1}). Enter a tv series title: ").strip()
                                if title.lower() in ["q", "quit"]:
                                    return

                                if title in dict:
                                    print(f"`{title}` {current_type} series already exists.")
                                else:
                                    while True:
                                        try:
                                            seasons = int(input("Enter number of seasons released from this series: "))
                                            break
                                        except ValueError:
                                            print("Please enter a number.")

                                    while True:
                                        begin_year = input(f"Enter a {current_type} series begin year: ").strip()
                                        print()
                                        if begin_year.isdigit() and len(begin_year) == 4:
                                            begin_year = int(begin_year)
                                            if begin_year < 1900:
                                                print(f"{current_type.capitalize()} series begin year must be at least after 1900.\n")
                                            else:
                                                print(f"The beginning year you entered is `{begin_year}`.")
                                                while True:
                                                    still_going = input("Is the series still going? (Y/N): ").lower()
                                                    if still_going in ["y","yes","1","01"]:
                                                        end_year = " /- "
                                                        adder(title,seasons,begin_year,end_year)
                                                        break
                                                    elif still_going in ["n","no","2","02"]:
                                                        end_year = input(f"Enter a {current_type} series end year: ").strip()
                                                        print()
                                                        if end_year.isdigit() and len(end_year) == 4:
                                                            end_year = int(end_year)
                                                            if end_year < begin_year:
                                                                print(f"{current_type.capitalize()} series end year must be after the begin year.\n")
                                                            else:
                                                                print(f"The ending year you entered is `{end_year}`.")
                                                                adder(title,seasons,begin_year,end_year)
                                                                break

                                                        else:
                                                            print("Please enter a valid end year.")
                                                    else:
                                                        print("Please enter a valid input.")
                                                        break
                                                break
                                        else:
                                            print("Please enter a valid begin year.")
                                    break
                    else:
                        print(f"Please enter a valid number of {current_type} series.\n")
                else:
                    print(f"Please enter a digit number of {current_type} series.\n")
            except ValueError:
                print(f"Please enter a digit number of {current_type} series.\n")

    def adder(title,seasons,begin_year,end_year):
        while True:
            print("\n  --- Country ---  ")
            for l in Country:
                print(f"{l}.  {Country[l]}")
            country = input("Enter country/s : ").strip()
            print()
            if country in Country.keys():
                con = country
                print(f"The series is from `{Country[con]}`.")
                break
            else:
                print("Please a number between 1 and 10.")

        while True:
            rate = input(f"Enter your rating for this {current_type} series : ").strip()
            print()
            if rate.lower() in ["q","quit"]:
                rat = "0"
                break
            elif rate in ["1", "2", "3", "4", "5"]:
                print(f"The rating you gave is `{Rating[rate]}`.")
                rat = rate
                break
            else:
                print("Please a number between 1 and 5.")

        while True:
            num = input("Enter the number of genres: ")
            if num.isdigit():
                num = int(num)
                if num > 0:
                    print("    ---- Genres ----    ")
                    for key, value in Genres.items():
                        i = int(key)
                        if i < 10:
                            print(f"0{key} : {value}")
                        else:
                            print(f"{key} : {value}")
                    selected_genres = []
                    for _ in range(num):
                        while True:
                            genre = input("Enter genre number: ").strip()
                            if genre.isdigit():
                                if genre in Genres.keys():
                                    if str(genre) in selected_genres:
                                        print(f"`{title}` is already in `{Genres[genre]}` genre.")
                                    else:
                                        selected_genres.append(str(genre))
                                        print(f"`{title}` series is added to `{Genres[genre]}` genre.")
                                        break
                                else:
                                    print("Please enter a valid genre number.")
                            else:
                                print("Please enter a valid number.")
                    print("\n----------------------------------------------")
                    print(f"`{title}` series added successfully!\n\n")
                    if current_type == "tv":
                        TvSeries[title] = [seasons, begin_year, end_year,con,rat] + selected_genres
                    elif current_type == "anime":
                        Anime[title] = [seasons, begin_year, end_year,con,rat] + selected_genres
                    write_tv()
                    break
                else:
                    print("Please enter a valid number of genres.")
            else:
                print("Please enter a valid number of genres.")

    def write_tv():
        with open(file, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for title in TvSeries:
                writer.writerow([title] + TvSeries[title])

    def read_tv():
        if current_type == "tv":
            TvSeries.clear()
        else:
            Anime.clear()

        with open(file, "r", newline="") as files:
            reader = csv.reader(files)
            for row in reader:
                if row:
                    title = row[0]
                    seasons = row[1]
                    begin_year = row[2]
                    end_year = row[3]
                    con = row[4]
                    rat = row[5]
                    genre_ids = [g.strip() for g in row[6:] if g.strip()]
                    if current_type == "tv":
                        TvSeries[title] = [seasons] + [begin_year] + [end_year] + [con] + [rat] + genre_ids
                    else:
                        Anime[title] = [seasons] + [begin_year] + [end_year] + [con] + [rat] + genre_ids

    def print_tv():
        read_tv()
        print("\n----------------------------------------------")
        print(f"    --- {current_type} Series in the movie database ---   \n")
        print("----------------------------------------------\n\n")

        name = f"{current_type} Series"
        ge = "Genre"
        y = "Years"
        s = "Seasons"
        c = "Country"
        r = "Rating"
        for j in range(125):
            print("-",end="")

        print(f"  {name:^45}  |  {s:^7}    |   {y:8} | {c:^10}|{r:^13}| {ge:^40}")

        for j in range(125):
            print("-",end="")
        print()

        i = 1
        if current_type == "tv":
            Dict = TvSeries
        else:
            Dict = Anime

        for title,data in Dict.items():
            season = data[0]
            begin_year = data[1]
            end_year = data[2]
            country = data[3]
            rating = data[4]
            genre_ids = data[5:]
            genre_name = [Genres[genre_id] for genre_id in genre_ids if genre_id in Genres]
            if rating != "0":
                num = 0
                printer(i,title,season,begin_year,end_year,country,rating,genre_name,num)
                i = i + 1
            else:
                num = 11
                printer(i,title,season,begin_year,end_year,country,rating,genre_name,num)
                i = i + 1

        for j in range(125):
            print("-", end="")
        print()

        count = i - 1
        print(f"Number of {current_type} seris in the database are {count}")

        for j in range(125):
            print("-", end="")
        print()

        input("Press enter to continue...\n\n")

    def printer(i,title,season,begin_year,end_year,country,rating,genre_name,num):
            if i < 10:
                print(
                    f" 0{i:1}. {title:35} {season:^3}       {begin_year:4}-{end_year:4}     {Country[country]:<8}   {Rating[rating]:{num}}   {', '.join(genre_name):<45}")
            else:
                print(
                    f"{i:3}. {title:35} {season:^3}       {begin_year:4}-{end_year:4}     {Country[country]:<8}   {Rating[rating]:{num}}   {', '.join(genre_name):<45}")

    def search_tv():
        print()
        print(f"Searching for {current_type} series...")
        print("-" * 30)
        while True:
            user_input = input("How do you want to search? \n01. By Name \n02. By Released Year \n03. By Genre \n04. By Country \n05. By Rating \n06. Super Search \n07. Exit Search \n - - - - -> ")
            match user_input:
                case "by name"|"name"|"1"|"01":
                    by_name()
                case "by released year"|"released year"|"year"|"02"|"2":
                    by_year("search")
                case "by genre"|"genre"|"3"|"03":
                    by_genre()
                case "by country"|"country"|"04"|"4":
                    by_country("search")
                case "by rating"|"rating"|"05"|"5":
                    by_rating("search")
                case "super search"|"super"|"06"|"6":
                    super_search_tv()
                case "exit search"|"exit"|"07"|"7":
                    break
                case _:
                    print("Please enter a valid number.")

    def by_name():
        print()
        print("Searching for series by name...")
        print("-" * 25)
        while True:
            name = input(f"Please enter the first letter of the name of the {current_type} series : ")
            print()
            if name in ["q","quit"]:
                break
            else:
                read_tv()
                for title,data in dict.items():
                    if name.lower() in title[0].lower():
                        print(title)
                    elif len(name) > 1:
                        if name.lower() in title.lower():
                            print(f"{current_type.capitalize()} Series : {title}\nNumber of Seasons : {data[0]}\nReleased Year : {data[1]}\nEnd Year : {data[2]}\nCountry : {data[3]}\nRating : {data[4]}\nGenre : {Country[data[5]]}\nRating : {Rating[data[6]]}\n")
                            input("Press enter to continue...")
                        elif not (name.lower() in title.lower()):
                            print(f"{title} not in the database.")
                            input("Press enter to continue...")
                    else:
                        print(f"{current_type.capitalize()} series with starting letter {title[0]} not found.")

    def by_year(search_type):
        read_tv()
        year = []
        for title,data in dict.items():
            if len(data[1]) == 4:
                year.append(data[1])
            elif len(data[2]) == 4:
                year.append(data[2])

        year.sort()
        beg_year = year[0]
        end_year = year[-1]


        while True:
            print()
            print("Search by Year...")
            print("-" * 25)
            choice = input(f"How do you want to search by year? (q to quit)\n01. Begin Year of the {current_type.capitalize()} shows \n02. End Year of the {current_type.capitalize()} shows \n03. {current_type.capitalize()} shows in a year range\n -----------------------------> ")
            if choice in ["01","1","02","2","03","3","begin year","ending year","begin","end","range","year range"]:

                match choice:
                    case "1"|"01"|"begin"|"begin year":
                        by_begin_or_end_year(search_type,"begin",beg_year, end_year)
                    case "2"|"02"|"end year"|"end":
                        by_begin_or_end_year(search_type,"end",beg_year, end_year)
                    case "3"|"03"|"range"|"year range":
                        by_year_range(search_type,beg_year,end_year)
                    case "q"|"quit"|"exit":
                        break
            else:
                print("Please enter a valid number.")

    def by_begin_or_end_year(search_type,begin_or_ending,beg_year,end_year):
        num = 0
        if search_type != "super search":
            read_tv()
        while True:
            if begin_or_ending == "begin":
                year_type = 1
            else:
                year_type = 2

            year = input(f"Please enter the released year of the {current_type} series (q to quit) : ")
            print()
            if year.lower() in ["q", "quit"]:
                break
            elif year.isdigit() and (int(beg_year) - 1) < int(year) < (int(end_year) + 1):
                print(f"{current_type.capitalize()} shows which {begin_or_ending} in {year}.")
                print("_" * 25)
                for title,data in dict.items():
                    if year == data[year_type]:
                        if search_type == "search":
                            print(title)
                        elif search_type == "super search":
                            year_shows.append(title)
                        num += 1  # Fixed: was num =+ 1
                print("_" * 25)
                print(f"Number of {current_type} shows : {num}")
                print("_" * 25)
                if search_type == "super search":
                    break
                input("Press enter to continue...")
                break
            else:
                print(f"Please enter a valid year between {beg_year} and {end_year}.\n")

    def by_year_range(search_type,beg_year,end_year):
        while True:
            year_range = input(f"Enter the year range({beg_year}-{end_year}) : ")
            if len(year_range) == 9:
                begin =  year_range[0:4]
                end = year_range[5:9]
                if begin > end:
                    begin_1 = end
                    end_1 = begin
                    print()
                    print("You must enter the begin year first.")
                    print("As default we'll switch the years")
                    while True:
                        print()
                        choice = input("Do you want to continue? (y/n) : ")
                        if choice in ["yes","y"]:
                            year_range_search_engine(search_type,begin_1,end_1)
                        elif choice in ["no","n"]:
                            print("We will direct you the main year range menu.")
                            break
                        else:
                            print("Please enter a valid input.")
                else:
                    year_range_search_engine(search_type,begin,end)
                break
            elif len(year_range) == 0:
                print(f"Please enter a valid years between {beg_year} and {end_year}.\n")

    def year_range_search_engine(search_type,beg_year,end_year):
        list_of_shows = []
        num = 0
        if search_type != "super search":
            read_tv()
        print()
        print("-" * 25)
        print(f"The {current_type} shows aired in between {beg_year} - {end_year}.")
        print("-" * 25)
        for title,data in dict.items():
            if beg_year <= data[1]:
                if end_year >= data[2]:
                    if search_type == "search":
                        list_of_shows.append(title)
                    elif search_type == "super search":
                        year_range_shows.append(title)
                    num += 1

        list_of_shows.sort()
        if search_type == "search":
            for i in list_of_shows:
                print(i)

            if list_of_shows.__len__() == 0:
                print("There are no shows available.")

            print("-" * 25)
            print(f"There are {num} of {current_type} shows.")
            print("-" * 25)
        elif search_type == "super search":
            print(f"Found {num} shows in year range {beg_year}-{end_year}")

    def by_genre():
        for i in Genres:
            print(f"{i}. {Genres[i]}")
        while True:
            read_tv()
            genre = input(f"Please enter the genre or the genre id of the {current_type} series (q to quit) : ")
            print()
            if genre.lower() in ["q", "quit"]:
                break

            elif genre.isdigit():
                if genre in Genres.keys():
                    print(f"\nThe {current_type} series with {Genres[genre]} genre.")
                    for title,data in dict.items():
                        if genre in data[5:]:
                            print(title)
                    input("Press enter to continue...")
                else:
                    print("Please enter a valid genre id.")

            elif genre.capitalize() in Genres.values():
                print(f"\nThe {current_type} series with {genre} genre.")
                for title,data in dict.items():
                    keys = [k for k, v in Genres.items() if v == genre.capitalize()]
                    if keys[0] in data[5:]:
                        print(title)
                input("Press enter to continue...")

            else:
                print("Please enter a valid genre.")

    def by_country(search_type):
        for i in Country:
            print(f"{i}. {Country[i]}")

        while True:
            if search_type != "super search":
                read_tv()
            country = input(f"Please enter the country or the country code of the {current_type} series (q to quit) : ")
            print()
            if country.lower() in ["q", "quit"]:
                break
            elif country.isdigit():
                if country in Country.keys():
                    for title,data in dict.items():
                        if country == data[3]:
                            if search_type == "search":
                                print(title)
                            elif search_type == "super search":
                                con_shows.append(title)
                    if search_type == "super search":
                        print(f"Found {len(con_shows)} shows from {Country[country]}")
                        break
                    input("Press enter to continue...")
                    break
                else:
                    print("Please enter a valid country code.")
            elif country.capitalize() in Country.values():
                # Find country code
                country_code = None
                for key, value in Country.items():
                    if value == country.capitalize():
                        country_code = key
                        break
                if country_code:
                    for title,data in dict.items():
                        if country_code == data[3]:
                            if search_type == "search":
                                print(title)
                            elif search_type == "super search":
                                con_shows.append(title)
                    if search_type == "super search":
                        print(f"Found {len(con_shows)} shows from {country}")
                        break
                    input("Press enter to continue...")
                    break
            else:
                print("Please enter a valid country code.")

    def by_rating(search_type):
        if search_type != "super search":
            read_tv()
        while True:
            rate = input("Enter the rating 1 to 5 (q to quit) : ")
            if rate.lower() in ["q", "quit"]:
                break
            elif rate.isdigit():
                print(f"\n{current_type.capitalize()} series with {Rating[rate]} rating.")
                for title,data in dict.items():
                    if rate == data[4]:
                        if search_type == "search":
                            print(title)
                        elif search_type == "super search":
                            rate_shows.append(title)
                if search_type == "super search":
                    print(f"Found {len(rate_shows)} shows with rating {Rating[rate]}")
                    break
                input("Press enter to continue...")
                break
            else:
                print("Please enter a valid rating.")

    def sort_alphabetically_tv():
        read_tv()
        print(f"Sorting alphabetically {current_type.capitalize()} series...\n")
        tv = []
        b = []
        for title, data in dict.items():
            try:
                tv.append(title)
            except IndexError:
                print()
            b.append(data[0:5])

        tv.sort()

        for i in b:
            print(f"{i}")
        for i in tv:
            print(f"{i}")

    # def super_search_tv():
    #     choose_right = False
    #     user = []
    #     print(f"These are the types of things you can include in your search for {current_type}?\n01. By multiple genre \n02. By Country \n03. By Rating \n04. By  Year")
    #     print("-" * 25)
    #     while True:
    #         user_in = input("How many of these you would like to include in your search? (q to quit) : ")
    #         if user_in.lower() in ["q", "quit"]:
    #             break
    #         elif user_in.isdigit():
    #             if user_in.lower() in ["1","2","3","4","01","02","03","04"]:
    #                 if len(user_in) == 2:
    #                     num_of_types = user_in[1]
    #                 else:
    #                     num_of_types = user_in
    #
    #                 for i in num_of_types:
    #                     while True:
    #                         print()
    #                         print("-" * 30)
    #                         users_search_types = input("What are the types you want to include in your search?\n01. By multiple genre \n02. By Country \n03. By Rating \n04. By  Year\n05. Quit super search")
    #                         print("-" * 30)
    #
    #                         if users_search_types in ["1","01","multiple genre"]:
    #                             user.append("1")
    #                             choose_right = True
    #                             break
    #                         elif users_search_types in ["2","02","country"]:
    #                             user.append("2")
    #                             choose_right = True
    #                             break
    #                         elif users_search_types in ["3","03","rating"]:
    #                             user.append("3")
    #                             choose_right = True
    #                             break
    #                         elif users_search_types in ["4","04","year"]:
    #                             user.append("4")
    #                             choose_right = True
    #                             break
    #                         elif users_search_types in ["5","05","quit","exit"]:
    #                             print(f"You're choosing to quit from super search search for {current_type.capitalize()} shows.\n")
    #                             return
    #                         else:
    #                             print("Please enter a valid number between 1 and 5.")
    #
    #     if choose_right:
    #         super_search_engine(user,"super search")


    #super search lists.

    con_shows = []
    gen_shows = []
    rate_shows = []
    year_shows = []
    year_range_shows = []

    def super_search_tv():
        choose_right = False
        user = []
        print(
            f"These are the types of things you can include in your search for {current_type}?\n01. By multiple genre \n02. By Country \n03. By Rating \n04. By Year")
        print("-" * 25)

        while True:
            user_in = input("How many of these you would like to include in your search? (q to quit) : ")
            if user_in.lower() in ["q", "quit"]:
                return

            if user_in.isdigit() and 1 <= int(user_in) <= 4:
                num_of_types = int(user_in)

                for i in range(num_of_types):
                    while True:
                        print()
                        print("-" * 30)
                        users_search_types = input(
                            f"What is type {i + 1} you want to include in your search?\n01. By multiple genre \n02. By Country \n03. By Rating \n04. By Year\n05. Quit super search\n -----------------------------> ")
                        print("-" * 30)

                        if users_search_types in ["1", "01", "multiple genre"]:
                            if "1" not in user:  # Avoid duplicates
                                user.append("1")
                                choose_right = True
                                break
                            else:
                                print("You already selected multiple genre.")
                        elif users_search_types in ["2", "02", "country"]:
                            if "2" not in user:  # Avoid duplicates
                                user.append("2")
                                choose_right = True
                                break
                            else:
                                print("You already selected country.")
                        elif users_search_types in ["3", "03", "rating"]:
                            if "3" not in user:  # Avoid duplicates
                                user.append("3")
                                choose_right = True
                                break
                            else:
                                print("You already selected rating.")
                        elif users_search_types in ["4", "04", "year"]:
                            if "4" not in user:  # Avoid duplicates
                                user.append("4")
                                choose_right = True
                                break
                            else:
                                print("You already selected year.")
                        elif users_search_types in ["5", "05", "quit", "exit"]:
                            print(f"You're choosing to quit from super search for {current_type.capitalize()} shows.\n")
                            return
                        else:
                            print("Please enter a valid number between 1 and 5.")
                break
            else:
                print("Please enter a number between 1 and 4.")

        if choose_right:
            super_search_engine(user, "super search")

    def super_search_engine(listing, search_type):
        # Clear all lists first
        con_shows.clear()
        gen_shows.clear()
        rate_shows.clear()
        year_shows.clear()
        year_range_shows.clear()

        # Load data once at the beginning for super search
        read_tv()

        # Process each criterion in the list
        for criterion in listing:
            if criterion == "1":  # Multiple genres
                multiple_genre = []
                print("\n" + "-" * 30)
                print("SELECT MULTIPLE GENRES")
                print("-" * 30)

                while True:
                    num = input("Enter the number of genres you want to search by: ")
                    if num.isdigit():
                        num = int(num)
                        if num > 0:
                            print("\n    ---- Available Genres ----    ")
                            for key, value in Genres.items():
                                i = int(key)
                                if i < 10:
                                    print(f"    0{key} : {value}")
                                else:
                                    print(f"    {key} : {value}")
                            print()

                            for number in range(num):
                                while True:
                                    try:
                                        genre = input(f"Enter genre {number + 1} code (01-20): ")
                                        if genre in Genres.keys():
                                            if genre not in multiple_genre:
                                                multiple_genre.append(genre)
                                                print(f"Added: {Genres[genre]}")
                                                break
                                            else:
                                                print("You have already entered this genre.")
                                        else:
                                            print("Please enter a valid genre code (01-20).")
                                    except ValueError:
                                        print("Please enter a valid genre code.")
                            break
                        else:
                            print("Please enter a number higher than 0")
                    else:
                        print("Please enter a valid number.")

                # Find shows matching ALL selected genres
                for title, data in dict.items():
                    show_genres = data[5:]  # Genres start at index 5
                    # Check if ALL selected genres are in this show's genres
                    if all(g in show_genres for g in multiple_genre):
                        gen_shows.append(title)

                print(f"\nFound {len(gen_shows)} shows matching ALL selected genres")

            elif criterion == "2":  # Country
                by_country(search_type)

            elif criterion == "3":  # Rating
                by_rating(search_type)

            elif criterion == "4":  # Year
                by_year(search_type)

        # After collecting all criteria, find the intersection
        print_super_search_results()

    def print_super_search_results():
        """Find and display shows that match ALL selected criteria"""
        print("\n" + "=" * 60)
        print("SUPER SEARCH RESULTS")
        print("=" * 60)

        # Combine year_shows and year_range_shows if both exist
        all_year_shows = []
        if year_shows:
            all_year_shows = year_shows.copy()
        if year_range_shows:
            if all_year_shows:
                # Find intersection of year_shows and year_range_shows
                all_year_shows = list(set(all_year_shows) & set(year_range_shows))
            else:
                all_year_shows = year_range_shows.copy()

        # Create a list of all non-empty result sets
        result_sets = []

        if gen_shows:
            result_sets.append(set(gen_shows))

        if con_shows:
            result_sets.append(set(con_shows))

        if rate_shows:
            result_sets.append(set(rate_shows))

        if all_year_shows:
            result_sets.append(set(all_year_shows))

        # Find the intersection of ALL sets (shows that match ALL criteria)
        if not result_sets:
            print("No criteria were selected.")
            print("=" * 60)
            return

        # Start with first set and intersect with others
        common_shows = result_sets[0]
        for i in range(1, len(result_sets)):
            common_shows = common_shows.intersection(result_sets[i])

        # Convert back to sorted list
        final_results = sorted(list(common_shows))

        # Display results
        if not final_results:
            print("No shows found matching ALL your criteria.")
            print("\nIndividual criteria matches:")
            print(f"  - Genre matches: {len(gen_shows) if gen_shows else 0} shows")
            print(f"  - Country matches: {len(con_shows) if con_shows else 0} shows")
            print(f"  - Rating matches: {len(rate_shows) if rate_shows else 0} shows")
            print(f"  - Year matches: {len(all_year_shows) if all_year_shows else 0} shows")
        else:
            print(f"Found {len(final_results)} show(s) matching ALL criteria:\n")

            for i, show_title in enumerate(final_results, 1):
                # Get show details from dictionary
                show_data = dict[show_title]

                # Format output
                if i < 10:
                    prefix = f"0{i}."
                else:
                    prefix = f"{i}."

                print(f"{prefix} {show_title}")
                print(f"   Years: {show_data[1]}-{show_data[2]} | Seasons: {show_data[0]}")
                print(f"   Country: {Country[show_data[3]]} | Rating: {Rating[show_data[4]]}")

                # Show genres
                if len(show_data) > 5:
                    genre_names = [Genres[g] for g in show_data[5:] if g in Genres]
                    print(f"   Genres: {', '.join(genre_names)}")

                print()

        print("=" * 60)
        input("\nPress Enter to continue...")

    def main_tv():
        while True:
            print("----------------------------------------------")
            print(f"  ---  Welcome to {current_type.capitalize()} Series Recorder  ----    ")
            print("----------------------------------------------")
            print(f"01. Enter a {current_type} series to the database")
            print(f"02. Print all the {current_type} series in the database")
            print(f"03. Search for a {current_type} series")
            print(f"04. Sort the {current_type} series alphabetically")
            print("05. Exit")
            print("----------------------------------------------")
            choose = input("Enter your choice: ").strip().capitalize()
            print("\n----------------------------------------------")

            if choose == "1" or choose == "01":
                print(f"You choose to add {current_type} series to the database")
                print("----------------------------------------------")
                add_tv()
            elif choose == "2" or choose == "02":
                print(f"You choose to see all {current_type} series in the database")
                print("----------------------------------------------")
                print_tv()
            elif choose == "3" or choose == "03":
                print(f"You choose to search for a {current_type} series")
                print("-----------------------------------------------")
                search_tv()
            elif choose == "4" or choose == "04":
                print(f"You choose to sort the {current_type} series alphabetically.")
                print("-----------------------------------------------")
                sort_alphabetically_tv()
            elif choose == "5" or choose == "05":
                print("You choose to exit from the program")
                print("----------------------------------------------")
                print("Bye bye!")
                break
            else:
                print("Invalid input.\nPlease try again.")

    if __name__ == '__main__':
        main_tv()

def main():
    while True:
        print("Welcome to Tv Series/Movies/Anime Recorder")
        choose = input("What do you want to add (movies/tv-series/anime)..?\n01. Movies\n02. Tv-Series\n03. Anime\n04. Exit main menu\n---------------------> ").strip().lower()

        if choose in ["01","1","movies"]:
            print("\nYou choose movies ")
            print("-----------------------------------------------\n\n")
            movies()
        elif choose in ["02","2","tv-series"]:
            print("\nYou choose tv-series ")
            print("------------------------------------------------\n\n")
            tv_series("tv")
        elif choose in ["03","3","anime"]:
            print("\nYou choose anime ")
            print("------------------------------------------------\n\n")
            tv_series("anime")
        elif choose in ["04","4","exit"]:
            print("\nYou choose to exit from the program")
            print("------------------------------------------------\n\n")
            print("Bye bye!")
            break
        else:
            print("\nInvalid input.\nPlease try again.")

if __name__ == '__main__':
   main()




#------------------------------------------------------------------------------------------
