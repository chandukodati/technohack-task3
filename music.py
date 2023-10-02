import pygame
import os

# Initialize pygame
pygame.init()


# Function to create a playlist
def create_playlist():
    playlist_name = input("Enter the playlist name: ")
    with open(playlist_name + ".txt", "w") as playlist_file:
        print(f"Playlist '{playlist_name}' created.")


# Function to add songs to a playlist
def add_to_playlist():
    playlist_name = input("Enter the playlist name: ")
    song_name = input("Enter the song name (MP3 file): ")

    if not os.path.exists(playlist_name + ".txt"):
        print(f"Playlist '{playlist_name}' does not exist.")
        return

    with open(playlist_name + ".txt", "a") as playlist_file:
        playlist_file.write(song_name + "\n")
        print(f"Song '{song_name}' added to '{playlist_name}'.")


# Function to play a playlist
def play_playlist():
    playlist_name = input("Enter the playlist name: ")

    if not os.path.exists(playlist_name + ".txt"):
        print(f"Playlist '{playlist_name}' does not exist.")
        return

    with open(playlist_name + ".txt", "r") as playlist_file:
        songs = playlist_file.readlines()
        songs = [song.strip() for song in songs]

        for song in songs:
            try:
                pygame.mixer.music.load(song)
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.5)
                print(f"Now playing: {song}")

                # Wait for the song to finish
                while pygame.mixer.music.get_busy():
                    continue
            except pygame.error:
                print(f"Error playing '{song}'")


# Main loop
while True:
    print("\nOptions:")
    print("1. Create a Playlist")
    print("2. Add Song to Playlist")
    print("3. Play Playlist")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_playlist()
    elif choice == "2":
        add_to_playlist()
    elif choice == "3":
        play_playlist()
    elif choice == "4":
        pygame.quit()
        break
    else:
        print("Invalid choice. Please try again.")
