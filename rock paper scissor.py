from numpy._core.multiarray import result_type
import streamlit as st
import random

st.markdown("""
     <style>
    .watermark {
        position: fixed;
        top: 50%;
        left: 47%;
        transform: translate(-50%, -50%) rotate(-25deg);
        font-size: 40px;
        color: rgba(255, 255, 255, 0.04);
        z-index: 0;
        pointer-events: none;
        user-select: none;
        white-space: nowrap;
        font-weight: bold;
        font-family: 'Brush Script MT', cursive;
    }
    .stApp > header {
        background: transparent;
    }
    </style>
    <div class="watermark">Created by Samiii 🫠 </div>
""", unsafe_allow_html=True)    
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'computer_score' not in st.session_state:
     st.session_state.computer_score = 0
if 'tie_score' not in st.session_state:
     st.session_state.tie_score = 0
st.title("Rock Paper Scissors Game")    

items=["rock", "paper", "scissors"]

st.write("**Make your choice:**")
col1, col2, col3 = st.columns(3)
user_choice = None

with col1:
    if st.button("rock 🪨"):
      user_choice = "rock"
with col2:
    if st.button("paper 📃"):
      user_choice = "paper"
with col3:
    if st.button("scissors ✂️"):
      user_choice = "scissors"

if user_choice:
  st.divider()
  computer_choice = random.choice(items)
  st.write(f"**you chose:** {user_choice}")
  st.write(f"**computer chose:** {computer_choice}")

  if user_choice == computer_choice:
    st.info("It's a tie! 😁")
    st.session_state.tie_score += 1
  elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
    st.success("You win! 🎉")
    st.toast("🎆🎇 Boom! Crackers Blasting! 🎆🎇")
    st.image("https://media.tenor.com/8X0g1k5J3mYAAAAC/fireworks.gif", width=200)
    st.session_state.user_score += 1
  else:
    st.error("computer wins! 😉")
    st.session_state.computer_score += 1

st.divider()
st.subheader("🏆 Scoreboard")
score_col1, score_col2, score_col3 = st.columns(3)
with score_col1:
   st.metric(label="😎 You", value=st.session_state.user_score)
with score_col2:
   st.metric(label="🤖 Computer", value=st.session_state.computer_score)
with score_col3:
   st.metric(label="🤝 Tie", value=st.session_state.tie_score)

st.divider()
st.subheader("📊 Game Statistics")
if st.session_state.user_score > st.session_state.computer_score:
    st.success("You are leading! 🏆")
elif st.session_state.user_score < st.session_state.computer_score:
   st.warning("Computer is leading! catch up! 🤖")
else:
    st.info("It's a neck-to-neck game! Both are Equal! ⚖️")

st.write("")
if st.button("Reset Scores 🔄️"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.tie_score = 0
    st.success("Scores have been reset! ✅")
