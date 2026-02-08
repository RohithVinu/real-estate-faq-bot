import streamlit as st
from bot_logic import get_bot_response

# Page config
st.set_page_config(page_title="Real Estate FAQ Bot", page_icon="🏠")

st.title("🏠 Real Estate FAQ Bot")
st.write("Ask any question related to property buying, pricing, or legal process.")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("Enter your question:")

if st.button("Ask"):
    if user_input:
        bot_reply = get_bot_response(user_input)

        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", bot_reply))

# Display chat history
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")
