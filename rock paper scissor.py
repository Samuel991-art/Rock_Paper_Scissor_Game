import streamlit as st
import random
items=["rock", "paper", "scissors"]

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
  elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
    st.success("You win! 🎉")
    st.balloons()
  else:
    st.error("computer wins! 😉")
