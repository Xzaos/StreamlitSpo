import streamlit as st
import datetime
import random

# Mock song database
SONGS = [
    {"title": "Weightless", "artist": "Marconi Union", "mood": "stressed", "energy": "low"},
    {"title": "Levitating", "artist": "Dua Lipa", "mood": "happy", "energy": "high"},
    {"title": "Thunderstruck", "artist": "AC/DC", "mood": "energetic", "energy": "high"},
    {"title": "Lo-Fi Study Beat", "artist": "ChilledCow", "mood": "focused", "energy": "medium"},
    {"title": "Someone Like You", "artist": "Adele", "mood": "sad", "energy": "low"},
    {"title": "Happy", "artist": "Pharrell Williams", "mood": "happy", "energy": "high"},
    {"title": "Sunflower", "artist": "Post Malone", "mood": "happy", "energy": "medium"},
    {"title": "Clair de Lune", "artist": "Debussy", "mood": "relaxed", "energy": "low"},
    {"title": "Believer", "artist": "Imagine Dragons", "mood": "energetic", "energy": "high"},
    {"title": "River Flows in You", "artist": "Yiruma", "mood": "relaxed", "energy": "low"},
]

def detect_mood(user_input):
    user_input = user_input.lower()
    if any(word in user_input for word in ["sad", "down", "unhappy", "blue"]):
        return "sad"
    elif any(word in user_input for word in ["happy", "joy", "glad", "excited"]):
        return "happy"
    elif any(word in user_input for word in ["stress", "anxious", "overwhelmed"]):
        return "stressed"
    elif any(word in user_input for word in ["focus", "study", "work"]):
        return "focused"
    elif any(word in user_input for word in ["energy", "workout", "run", "gym", "party"]):
        return "energetic"
    elif any(word in user_input for word in ["relax", "calm", "chill"]):
        return "relaxed"
    else:
        return random.choice(["happy", "relaxed", "energetic", "stressed", "focused", "sad"])

def recommend_song(mood):
    matches = [song for song in SONGS if song["mood"] == mood]
    if matches:
        return random.choice(matches)
    else:
        return random.choice(SONGS)

st.set_page_config(page_title="Spotify Sonic Assistant", page_icon=":musical_note:", layout="centered")
st.title("🎵 Spotify Sonic Assistant")
st.write("Ask for music recommendations based on your mood, activity, or context!")

user_input = st.text_input("How are you feeling or what are you doing? (e.g., 'I'm stressed after work', 'I need workout music')")

if user_input:
    mood = detect_mood(user_input)
    song = recommend_song(mood)
    st.success(f"**Detected mood:** {mood.capitalize()}")
    st.write(f"**Recommended Song:**")
    st.markdown(f"🎶 **{song['title']}** by *{song['artist']}*")
    st.caption(f"({mood.capitalize()} mood, {song['energy']} energy)")
    st.write(f"_Why this song?_: It matches your current mood and energy needs!")

st.markdown("---")
st.caption("Try: 'I'm happy', 'I need to focus', 'I'm feeling sad', 'Give me energetic music', 'I want to relax'.")
