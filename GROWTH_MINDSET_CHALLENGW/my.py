import streamlit as st
import random
from datetime import date

# List of growth mindset challenges
challenges = [
    "Write down 3 things you learned today.",
    "Step out of your comfort zone and try something new.",
    "Give constructive feedback to someone.",
    "Reflect on a recent mistake and what you learned from it.",
    "Replace a negative thought with a positive one.",
    "Read or watch something that challenges your thinking.",
    "Practice gratitude: write down 3 things you're thankful for.",
    "Set a small goal and achieve it today.",
    "Teach someone something you know.",
    "Take a break and meditate for 5 minutes."
]

# Motivational quotes
quotes = [
    "Mistakes are proof that you are trying.",
    "Your brain is like a muscle—the more you use it, the stronger it gets.",
    "Challenges are opportunities to grow.",
    "Believe you can and you're halfway there.",
    "Growth is uncomfortable because you've never been here before."
]

# App title
st.title("🌱 Growth Mindset Challenge")

# Get today's challenge using date seed
random.seed(date.today().toordinal())
challenge = random.choice(challenges)
quote = random.choice(quotes)

st.header("✨ Today's Challenge")
st.success(challenge)

st.header("💬 Motivation")
st.info(f"“{quote}”")

st.markdown("---")
st.write("Come back tomorrow for a new challenge!")

