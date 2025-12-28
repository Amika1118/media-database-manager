# import csv
# from typing import Dict, List, Tuple, Union
#
# # Constants
# GENRES = {
#     "1": "Romantic", "2": "Action", "3": "Supernatural", "4": "Superhero",
#     "5": "Comedy", "6": "Animated", "7": "Science Fiction", "8": "Biography",
#     "9": "Children's", "10": "Fantasy", "11": "Horror", "12": "Thriller",
#     "13": "Documentary", "14": "Drama", "15": "Musical", "16": "Historical",
#     "17": "Crime", "18": "SitCom", "19": "Western", "20": "Mystery"
# }
#
# COUNTRIES = {
#     "0": "N/A", "1": "England", "2": "France", "3": "Germany", "4": "Italy",
#     "5": "America", "6": "Australia", "7": "Canada", "8": "Japan", "9": "Türkiye",
#     "10": "India", "11": "Russia", "12": "Ireland", "13": "China"
# }
#
# RATINGS = {
#     "0": "N/A", "1": "⭐        ", "2": "⭐⭐      ", "3": "⭐⭐⭐    ",
#     "4": "⭐⭐⭐⭐  ", "5": "⭐⭐⭐⭐⭐"
# }
#
#
# class MediaRecorder:
#     def __init__(self, media_type: str):
#         self.media_type = media_type
#         self.file_name = "Movies.csv" if media_type == "movie" else "TvSeries.csv"
#         self.data = {}
#
#     def read_data(self):
#         """Read data from CSV file"""
#         self.data.clear()
#         try:
#             with open(self.file_name, "r", newline="") as csvfile:
#                 reader = csv.reader(csvfile)
#                 for row in reader:
#                     if row:
#                         if self.media_type == "movie":
#                             title, year, country, rating, *genre_ids = row
#                             self.data[title] = [year, country, rating] + genre_ids
#                         else:
#                             title, seasons, begin_year, end_year, country, rating, *genre_ids = row
#                             self.data[title] = [seasons, begin_year, end_year, country, rating] + genre_ids
#         except FileNotFoundError:
#             open(self.file_name, "w").close()
#
#     def write_data(self):
#         """Write data to CSV file"""
#         with open(self.file_name, "w", newline="") as csvfile:
#             writer = csv.writer(csvfile)
#             for title, details in self.data.items():
#                 writer.writerow([title] + details)
#
#     def get_valid_input(self, prompt: str, validation_func, error_msg: str = "Invalid input. Please try again."):
#         """Get validated input from user"""
#         while True:
#             user_input = input(prompt).strip()
#             if validation_func(user_input):
#                 return user_input
#             print(error_msg)
#
#     def add_media(self):
#         """Add a movie or TV series to the database"""
#         self.read_data()
#
#         media_count = int(self.get_valid_input(
#             f"How many {self.media_type}s do you want to add? : ",
#             lambda x: x.isdigit() and int(x) > 0,
#             "Please enter a positive integer."
#         ))
#
#         for _ in range(media_count):
#             title = self.get_valid_input(
#                 f"Enter the {self.media_type} title: ",
#                 lambda x: len(x) > 4 and x not in self.data,
#                 "Title is too short or already exists in database."
#             )
#
#             if title.lower() in ["q", "quit"]:
#                 print(f"You choose to quit from entering a {self.media_type} to the database.")
#                 return
#
#             if self.media_type == "movie":
#                 self._add_movie(title)
#             else:
#                 self._add_tv_series(title)
#
#             print(f"\nYou added ----> {title}")
#             self.write_data()
#
#     def _add_movie(self, title: str):
#         """Add a movie to the database"""
#         year = self.get_valid_input(
#             "Enter the movie year: ",
#             lambda x: x.isdigit() and len(x) == 4,
#             "Movie year must be a 4-digit number."
#         )
#
#         rating = self.get_valid_input(
#             "Enter the movie rating (1-5): ",
#             lambda x: x in ["1", "2", "3", "4", "5"],
#             "Movie rating must be between 1 and 5."
#         )
#
#         # Display countries and get selection
#         print("Available countries:")
#         for code, name in COUNTRIES.items():
#             if code != "0":  # Skip N/A
#                 print(f"{code}. {name}")
#
#         country = self.get_valid_input(
#             "Enter the country code: ",
#             lambda x: x in COUNTRIES,
#             "Please enter a valid country code."
#         )
#
#         # Get genres
#         genre_count = int(self.get_valid_input(
#             "How many genres does this movie have? ",
#             lambda x: x.isdigit() and 0 < int(x) <= 5,
#             "Please enter a number between 1 and 5."
#         ))
#
#         print("\nAvailable genres:")
#         for code, name in GENRES.items():
#             print(f"{code}. {name}")
#
#         selected_genres = []
#         for i in range(genre_count):
#             genre = self.get_valid_input(
#                 f"Enter genre {i + 1} code: ",
#                 lambda x: x in GENRES and x not in selected_genres,
#                 "Please enter a valid, unique genre code."
#             )
#             selected_genres.append(genre)
#             print(f"You added '{title}' to the '{GENRES[genre]}' genre.")
#
#         # Store movie data
#         self.data[title] = [year, country, rating] + selected_genres
#
#     def _add_tv_series(self, title: str):
#         """Add a TV series to the database"""
#         seasons = self.get_valid_input(
#             "Enter number of seasons: ",
#             lambda x: x.isdigit() and int(x) > 0,
#             "Please enter a positive integer."
#         )
#
#         begin_year = self.get_valid_input(
#             "Enter the series begin year: ",
#             lambda x: x.isdigit() and len(x) == 4 and int(x) > 1900,
#             "Please enter a valid year after 1900."
#         )
#
#         still_going = self.get_valid_input(
#             "Is the series still going? (Y/N): ",
#             lambda x: x.lower() in ["y", "n", "yes", "no"],
#             "Please enter Y or N."
#         ).lower() in ["y", "yes"]
#
#         end_year = "/-/" if still_going else self.get_valid_input(
#             "Enter the series end year: ",
#             lambda x: x.isdigit() and len(x) == 4 and int(x) >= int(begin_year),
#             f"End year must be a 4-digit number >= {begin_year}."
#         )
#
#         # Display countries and get selection
#         print("Available countries:")
#         for code, name in COUNTRIES.items():
#             if code != "0":  # Skip N/A
#                 print(f"{code}. {name}")
#
#         country = self.get_valid_input(
#             "Enter the country code: ",
#             lambda x: x in COUNTRIES,
#             "Please enter a valid country code."
#         )
#
#         rating = self.get_valid_input(
#             "Enter the series rating (1-5): ",
#             lambda x: x in ["1", "2", "3", "4", "5"],
#             "Rating must be between 1 and 5."
#         )
#
#         # Get genres
#         genre_count = int(self.get_valid_input(
#             "How many genres does this series have? ",
#             lambda x: x.isdigit() and 0 < int(x) <= 5,
#             "Please enter a number between 1 and 5."
#         ))
#
#         print("\nAvailable genres:")
#         for code, name in GENRES.items():
#             print(f"{code}. {name}")
#
#         selected_genres = []
#         for i in range(genre_count):
#             genre = self.get_valid_input(
#                 f"Enter genre {i + 1} code: ",
#                 lambda x: x in GENRES and x not in selected_genres,
#                 "Please enter a valid, unique genre code."
#             )
#             selected_genres.append(genre)
#             print(f"You added '{title}' to the '{GENRES[genre]}' genre.")
#
#         # Store TV series data
#         self.data[title] = [seasons, begin_year, end_year, country, rating] + selected_genres
#
#     def print_media(self):
#         """Print all media in the database"""
#         self.read_data()
#
#         if self.media_type == "movie":
#             self._print_movies()
#         else:
#             self._print_tv_series()
#
#     def _print_movies(self):
#         """Print all movies in a formatted table"""
#         if not self.data:
#             print("No movies in the database.")
#             return
#
#         print("\n" + "-" * 125)
#         print(f"{'Movie':^68}  | {'Year':^14} | {'Genre':^50}")
#         print("-" * 125)
#
#         for i, (title, data) in enumerate(self.data.items(), 1):
#             year, country, rating, *genre_ids = data
#             genre_names = [GENRES.get(gid, "Unknown") for gid in genre_ids]
#
#             num_str = f"{i:2d}." if i < 10 else f"{i:3d}"
#             print(f"{num_str} {title:58}  {year:13} {COUNTRIES[country]:<10} "
#                   f"{RATINGS[rating]} {', '.join(genre_names)}")
#
#         print("-" * 125)
#         print(f"Number of movies in the database: {len(self.data)}")
#         print("-" * 125)
#         input("Press enter to continue...\n\n")
#
#     def _print_tv_series(self):
#         """Print all TV series in a formatted table"""
#         if not self.data:
#             print("No TV series in the database.")
#             return
#
#         print("\n" + "-" * 125)
#         print(f"{'TV Series':^45}  | {'Seasons':^7} | {'Years':^8} | {'Country':^10} | {'Rating':^13} | {'Genre':^40}")
#         print("-" * 125)
#
#         for i, (title, data) in enumerate(self.data.items(), 1):
#             seasons, begin_year, end_year, country, rating, *genre_ids = data
#             genre_names = [GENRES.get(gid, "Unknown") for gid in genre_ids]
#
#             num_str = f"{i:2d}." if i < 10 else f"{i:3d}"
#             rating_display = RATINGS[rating] if rating != "0" else "Not rated"
#
#             print(f"{num_str} {title:35} {seasons:^7} {begin_year:4}-{end_year:4}     "
#                   f"{COUNTRIES[country]:<8}   {rating_display:13} {', '.join(genre_names):<45}")
#
#         print("-" * 125)
#         print(f"Number of TV series in the database: {len(self.data)}")
#         print("-" * 125)
#         input("Press enter to continue...\n\n")
#
#     def search_media(self):
#         """Search for media based on different criteria"""
#         search_options = {
#             "1": ("Search by year", self.search_by_year),
#             "2": ("Search by name", self.search_by_name),
#             "3": ("Search by genre", self.search_by_genre),
#             "4": ("Super search", self.super_search),
#             "5": ("Exit search menu", lambda: None)
#         }
#
#         while True:
#             print("\n" + "-" * 50)
#             print("          -----  Search Menu  -----           ")
#             print("-" * 50)
#             for key, (desc, _) in search_options.items():
#                 print(f"{key}. {desc}")
#
#             choice = input("Enter your choice: ").strip()
#
#             if choice == "5":
#                 print("Exiting search menu.")
#                 break
#
#             if choice in search_options:
#                 search_options[choice][1]()
#             else:
#                 print("Invalid choice. Please try again.")
#
#     def search_by_year(self):
#         """Search media by release year"""
#         year = self.get_valid_input(
#             "Enter the year to search for: ",
#             lambda x: x.isdigit() and len(x) == 4,
#             "Please enter a valid 4-digit year."
#         )
#
#         self.read_data()
#         results = []
#
#         if self.media_type == "movie":
#             for title, data in self.data.items():
#                 if data[0] == year:  # Year is first element for movies
#                     results.append(title)
#         else:
#             for title, data in self.data.items():
#                 if data[1] == year:  # Begin year is second element for TV series
#                     results.append(title)
#
#         print(f"\n{self.media_type.capitalize()}s released in {year}:")
#         if results:
#             for i, title in enumerate(results, 1):
#                 print(f"{i}. {title}")
#         else:
#             print("No results found.")
#
#         input("\nPress enter to continue...")
#
#     def search_by_name(self):
#         """Search media by name"""
#         self.read_data()
#         letter = input("Enter the first letter or part of the name: ").strip().capitalize()
#
#         if not letter:
#             print("Invalid input.")
#             return
#
#         results = []
#         for title in self.data.keys():
#             if len(letter) == 1 and title.startswith(letter):
#                 results.append(title)
#             elif len(letter) > 1 and letter.lower() in title.lower():
#                 results.append(title)
#
#         print(f"\nSearch results for '{letter}':")
#         if results:
#             for i, title in enumerate(results, 1):
#                 print(f"{i}. {title}")
#         else:
#             print("No results found.")
#
#         input("\nPress enter to continue...")
#
#     def search_by_genre(self):
#         """Search media by genre"""
#         print("\nAvailable genres:")
#         for code, name in GENRES.items():
#             print(f"{code}. {name}")
#
#         genre_code = self.get_valid_input(
#             "Enter the genre code: ",
#             lambda x: x in GENRES,
#             "Please enter a valid genre code."
#         )
#
#         self.read_data()
#         results = []
#
#         for title, data in self.data.items():
#             # Genre IDs are stored from index 3 for movies and 5 for TV series
#             start_index = 3 if self.media_type == "movie" else 5
#             if genre_code in data[start_index:]:
#                 results.append(title)
#
#         print(f"\n{self.media_type.capitalize()}s in the '{GENRES[genre_code]}' genre:")
#         if results:
#             for i, title in enumerate(results, 1):
#                 print(f"{i}. {title}")
#         else:
#             print("No results found.")
#
#         input("\nPress enter to continue...")
#
#     def super_search(self):
#         """Advanced search with multiple criteria"""
#         print("Super search functionality not fully implemented in this refactoring.")
#         input("Press enter to continue...")
#
#     def sort_alphabetically(self):
#         """Sort and display media alphabetically"""
#         self.read_data()
#         sorted_titles = sorted(self.data.keys())
#
#         current_letter = ""
#         for title in sorted_titles:
#             first_letter = title[0].upper()
#             if first_letter != current_letter:
#                 current_letter = first_letter
#                 print(f"\n{current_letter}\n{'-' * 20}")
#             print(title)
#
#         input("\nPress enter to continue...")
#
#     def run(self):
#         """Main loop for the media recorder"""
#         menu_options = {
#             "1": (f"Add a {self.media_type} to the database", self.add_media),
#             "2": (f"Print all {self.media_type}s in the database", self.print_media),
#             "3": (f"Search for a {self.media_type}", self.search_media),
#             "4": (f"Sort {self.media_type}s alphabetically", self.sort_alphabetically),
#             "5": ("Exit", lambda: None)
#         }
#
#         while True:
#             print("\n" + "-" * 50)
#             print(f"  -----  Welcome to {self.media_type.capitalize()}s Recorder  -----    ")
#             print("-" * 50)
#
#             for key, (desc, _) in menu_options.items():
#                 print(f"{key}. {desc}")
#
#             choice = input("Enter your choice: ").strip()
#
#             if choice == "5":
#                 print("Goodbye!")
#                 break
#
#             if choice in menu_options:
#                 menu_options[choice][1]()
#             else:
#                 print("Invalid choice. Please try again.")
#
#
# def main():
#     """Main function to run the program"""
#     while True:
#         print("\nWelcome to Media Recorder")
#         print("1. Movies")
#         print("2. TV Series")
#         print("3. Exit")
#
#         choice = input("Select an option: ").strip()
#
#         if choice == "1":
#             movie_recorder = MediaRecorder("movie")
#             movie_recorder.run()
#         elif choice == "2":
#             tv_recorder = MediaRecorder("tv")
#             tv_recorder.run()
#         elif choice == "3":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")
#
#
# if __name__ == "__main__":
#     main()

numbers = []
while True:
    user = input("How many inputs are there? ")
    if user.isdigit():
        user = int(user)
        break
    else:
        print("Please enter a valid number")

count = 0

for i in range(user):
    user_in = input("Enter your input: ")
    numbers.append(user_in)

for input_str in numbers:
    i = 0
    while i <= len(input_str) - 4:
        if input_str[i:i + 4] in "1101":
            count += 1
            i += 4
        else:
            i += 1

    print(input_str,count)

