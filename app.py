import streamlit as st
import json
import random

# Load medical knowledge
with open('medical_knowledge.json', 'r') as f:
    knowledge = json.load(f)

st.set_page_config(page_title="Dr. Sanowar Medical Chatbot", page_icon="🦷")

st.title("🦷 Dr. Sanowar's Medical Assistant")
st.write("Ask your dental or medical questions:")

user_input = st.text_input("Type your question here...")

if user_input:
    input_lower = user_input.lower()
    response = "Please ask about dental or medical topics."
    
    for category, data in knowledge.items():
        for pattern in data['patterns']:
            if any(word in input_lower for word in pattern.lower().split()):
                response = random.choice(data['responses'])
                break
    
    st.write(f"**Assistant:** {response}")

st.warning("For educational purposes only. Consult doctors for medical advice.")
