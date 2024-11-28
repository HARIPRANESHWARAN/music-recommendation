import random

# Sample music dataset (song name, genre)
music_data = [
    ("Shape of You", "Pop"),
    ("Blinding Lights", "Pop"),
    ("Bohemian Rhapsody", "Rock"),
    ("Hotel California", "Rock"),
    ("Rolling in the Deep", "Pop"),
    ("Stairway to Heaven", "Rock"),
    ("Uptown Funk", "Funk"),
    ("Superstition", "Funk"),
    ("Old Town Road", "Country"),
    ("Jolene", "Country")
]

# Function to recommend songs based on genre
def recommend_music(genre):
    # Filter songs by the given genre
    recommended_songs = [song for song, song_genre in music_data if song_genre.lower() == genre.lower()]
    
    if recommended_songs:
        print(f"Recommended songs for '{genre}' genre:")
        for song in recommended_songs:
            print(f"- {song}")
    else:
        print(f"Sorry, no songs found in the '{genre}' genre.")

# Function to recommend random songs (without genre)
def recommend_random_music():
    song = random.choice(music_data)[0]
    print(f"How about listening to '{song}' today?")

# Menu for the user to choose an option
def music_recommendation_system():
    print("Welcome to the Music Recommendation System!")
    print("1. Recommend songs by genre")
    print("2. Recommend a random song")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        genre = input("Enter the genre you like (e.g., Pop, Rock, Funk, Country): ")
        recommend_music(genre)
    elif choice == '2':
        recommend_random_music()
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run the system
if __name__ == "__main__":
    music_recommendation_system()
