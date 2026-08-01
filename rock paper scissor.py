from numpy._core.multiarray import result_type
import streamlit as st
import random

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
    st.balloons()
    st.session_state.user_score += 1
  else:
    st.error("computer wins! 😉")
    st.session_state.computer_score += 1

st.divider()
st.write(f"**Your Score:** {st.session_state.user_score}")
st.write(f"**Computer Score:** {st.session_state.computer_score}")
st.write(f"**Tie Score:** {st.session_state.tie_score}")

if user_choice:
    st.divider()
    st.write(f"**You chose:** {user_choice}")
    st.write(f"**Computer chose:** {computer_choice}")
    if result_type == "win":
        st.success("You win! 🎉")
        st.balloons()
    elif result_type == "tie":
        st.info("It's a tie! 😁")
    else:
       st.info("Computer wins! 😉")

st.write("")
if st.button("Reset Scores 🔄️"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.tie_score = 0
    st.success("Scores have been reset! ✅")
    