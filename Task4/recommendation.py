import pandas as pd

#  To Load dataset
movies = pd.read_csv("movies.csv", encoding="latin1")

# Show available genres
print("Available genres:")
print(movies['genre'].unique())

# Take user input
genre = input("Enter your favorite genre: ")

# Filter movies
result = movies[movies['genre'].str.lower() == genre.lower()]

# Display result
if not result.empty:
    print("\nRecommended Movies:")
    for movie in result["title"]:
        print(" -", movie)
else:
    print("No movies found")
