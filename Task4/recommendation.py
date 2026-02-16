import pandas as pd

# Load dataset
movies = pd.read_csv("movies.csv")

# Show available genres
print("Available Genres:")
print(movies["genre"].unique())

# Take user input
genre = input("\nEnter your favorite genre: ")

# Filter movies
result = movies[movies["genre"].str.lower() == genre.lower()]

# Display result
if not result.empty:
    print("\nRecommended Movies:")
    for movie in result["title"]:
        print("- " + movie)
else:
    print("No movies found")