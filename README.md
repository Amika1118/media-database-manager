# 🎬 Media Database Manager

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)

A comprehensive command-line application for managing your personal collection of **movies**, **TV series**, and **anime**. Built entirely in Python with no external dependencies, this tool helps you organize, search, and analyze your media library with powerful filtering and sorting capabilities.

## 📋 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage Guide](#-usage-guide)
- [Data Structure](#-data-structure)
- [Screenshots](#-screenshots)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

### 📁 **Multi-Type Media Management**
- **Movies**: Track films with comprehensive metadata
- **TV Series**: Manage television shows with seasons and airing status
- **Anime**: Specialized database for anime series

### 🔍 **Advanced Search System**
- **Basic Search**: Find by title, year, genre, or country
- **Super Search**: Combine multiple criteria for precise filtering
- **Alphabetical Sorting**: Browse your collection A-Z
- **Year-based Filtering**: Find media released in specific years
- **Partial Match**: Search with partial title matches

### 📊 **Rich Metadata Support**
- **20+ Genres**: Romantic, Action, Supernatural, Sci-Fi, Horror, and more
- **13+ Countries**: America, Japan, England, France, Germany, etc.
- **5-Star Rating**: Visual star rating system (⭐ to ⭐⭐⭐⭐⭐)
- **Detailed Info**: Years, seasons, status (ongoing/ended), multiple genres

### 💾 **Smart Data Management**
- CSV-based storage (easy to edit and backup)
- Automatic file creation and maintenance
- Persistent data between sessions
- Clear, formatted output display

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- No external dependencies required

### Quick Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/media-database-manager.git
cd media-database-manager

# Run directly
python Movie_record.py
```

## 🎯 Quick Start

1. **First Run**: The program will create necessary CSV files automatically
2. **Add Your First Movie**:
   ```
   Choose: 1 (Movies)
   Then: 1 (Add movies)
   Follow the prompts to enter your movie details
   ```
3. **Explore Features**:
   - Add different types of media
   - Use search functions to find content
   - View your formatted database

## 📖 Usage Guide

### Main Menu
```
Welcome to Tv Series/Movies/Anime Recorder
What do you want to add?
01. Movies
02. Tv-Series
03. Anime
04. Exit main menu
```

### For Each Media Type
```
1. Add media to the database
2. Print all media in the database
3. Search for media
4. Sort media alphabetically
5. Exit
```

### Search Options
- **By Year**: Find all releases from a specific year
- **By Name**: Search by title (first letter or partial match)
- **By Genre**: Filter by one or multiple genres
- **Super Search**: Combine genre, country, year, and rating

### Example: Adding a Movie
```
Enter the movie title: Inception
Enter the movie year: 2010
Enter the movie rating: 5
Enter the country: 5 (America)
How many genres? 3
Genre options displayed...
Enter genres: 2 (Action), 7 (Science Fiction), 12 (Thriller)
Successfully added!
```

## 🗃️ Data Structure

### CSV Files
- `Movies.csv`: Stores all movie entries
- `TvSeries.csv`: Stores all TV series entries
- `Anime.csv`: Stores all anime entries

### Dictionary Mappings
The application uses intelligent ID mapping systems:

**Genres (20 categories):**
```python
"1": "Romantic", "2": "Action", "3": "Supernatural",
"4": "Superhero", "5": "Comedy", "6": "Animated",
"7": "Science Fiction", "8": "Biography", ...
```

**Countries (13+):**
```python
"1": "England", "2": "France", "3": "Germany",
"4": "Italy", "5": "America", "6": "Australia", ...
```

**Ratings (1-5 stars):**
```python
"1": "⭐        ", "2": "⭐⭐      ", 
"3": "⭐⭐⭐    ", "4": "⭐⭐⭐⭐  ", 
"5": "⭐⭐⭐⭐⭐"
```

## 📸 Screenshots

### Main Interface
```
--------------------------------------------------
  -----  Welcome to Movies Recorder  -----    
--------------------------------------------------
01. Enter a movie to the database
02. Print the all the movies in the database
03. Search for a movie
04. Sort the movies alphabetically
05. Exit
--------------------------------------------------
```

### Database Display
```
--------------------------------------------------------------------------------------------------------------
  Movie                        |     Year      |     Country     |   Rating          |      Genre
--------------------------------------------------------------------------------------------------------------
  01. The Matrix               |     1999      |     America     |   ⭐⭐⭐⭐⭐   | Action, Science Fiction
  02. Spirited Away            |     2001      |     Japan       |   ⭐⭐⭐⭐⭐   | Animated, Fantasy
  03. Inception                |     2010      |     America     |   ⭐⭐⭐⭐     | Action, Sci-Fi, Thriller
  04. Before we go             |     2019      |     America     |   ⭐⭐⭐⭐     | Romantic
  05. Finding you              |     2021      |     America     |   ⭐⭐⭐⭐     | Romantic
---------------------------------------------------------------------------------------------------------------
Number of movies in the database: 5
```

## 📁 Project Structure

```
media-database-manager/
│
├── Movie_record.py          # Main application file
├── Movies.csv              # Movie database (auto-created)
├── TvSeries.csv           # TV series database (auto-created)
├── Anime.csv              # Anime database (auto-created)
├── README.md              # This file
└── requirements.txt       # Python requirements
```

## 🔧 Technical Details

### Key Functions
- `movies()`: Main movie management module
- `tv_series()`: TV series and anime management
- `read_movies()/write_movies()`: CSV file operations
- `search_by_*()`: Various search implementations
- `print_*()`: Formatted display functions

### Error Handling
- Input validation for all user entries
- File operation error handling
- Graceful exit options throughout
- Data integrity checks

## 🚀 Future Enhancements

Planned features and improvements:

- [ ] Web interface with Flask/Django
- [ ] Mobile app companion
- [ ] API integration (IMDb, TMDB, AniList)
- [ ] Advanced statistics and charts
- [ ] Watchlist and viewing history tracking
- [ ] Export to JSON/Excel/PDF formats
- [ ] Movie recommendations based on preferences
- [ ] Multi-user support with profiles
- [ ] Cloud synchronization
- [ ] Movie poster and trailer links

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report Bugs**: Open an issue with detailed description
2. **Suggest Features**: Share your ideas for improvement
3. **Code Contributions**: Fork and submit pull requests
4. **Documentation**: Help improve documentation and examples

### Development Setup
```bash
# Fork and clone the repository
git clone https://github.com/amika1118/media-database-manager.git

# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Make your changes and test
python Movie_record.py

# Submit a pull request
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Media Database Manager

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
...
```

## 🙏 Acknowledgments

- Built with pure Python and standard libraries
- Inspired by personal media collection needs

## 📞 Support

Having issues or questions?
1. Check the [Issues](https://github.com/yourusername/media-database-manager/issues) page
2. Review the usage examples above
3. Create a new issue with your question

---

**Perfect for**: Movie enthusiasts, TV series collectors, anime fans, media librarians, and anyone who wants to organize their entertainment in a smart, accessible way.

*Start building your personalized media empire today!* 🍿📺🎞️

---
*Last Updated: January 2026*
