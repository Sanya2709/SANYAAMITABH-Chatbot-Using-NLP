import streamlit as st
import pickle
import json
import random

st.title("🤖 NLP Chatbot")

with open("intents.json", "r") as f:
    intents = json.load(f)

with open("chatbot_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def get_response(user_input):
    user_vector = vectorizer.transform([user_input])
    intent_index = model.predict(user_vector)[0]
    for intent in intents["intents"]:
        if intent["tag"] == intent_index:
            return random.choice(intent["responses"])
    return "Sorry, I didn't understand."

user_input = st.text_input("You: ")
if user_input:
    response = get_response(user_input)
    st.write("Bot:", response)
