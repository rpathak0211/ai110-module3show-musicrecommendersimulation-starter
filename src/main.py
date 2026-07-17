"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs

# Stress-test profiles: three "normal" tastes plus one adversarial profile with
# conflicting signals (high target energy paired with a low-energy, melancholy
# genre/mood) to see how the scoring rule behaves when there's no clean match.
PROFILES = {
    "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9, "likes_acoustic": False},
    "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.3, "likes_acoustic": True},
    "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.85, "likes_acoustic": False},
    "Adversarial: High-Energy Melancholy": {
        "genre": "classical",
        "mood": "melancholy",
        "energy": 0.9,
        "likes_acoustic": False,
    },
}


def print_recommendations(profile_name: str, user_prefs: dict, songs, k: int = 5) -> None:
    recommendations = recommend_songs(user_prefs, songs, k=k)

    print(f"\n=== {profile_name} ===")
    print(f"User profile: {user_prefs}")
    print("\nTop recommendations:\n")
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{rank}. {song['title']} — {song['artist']} ({song['genre']}/{song['mood']})")
        print(f"   Score: {score:.2f}")
        print(f"   Because: {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")

    for profile_name, user_prefs in PROFILES.items():
        print_recommendations(profile_name, user_prefs, songs, k=5)


if __name__ == "__main__":
    main()
