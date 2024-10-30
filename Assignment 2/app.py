#Importing required libraries 
import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
from deep_translator import GoogleTranslator

# Setting page configuration with modern theming
st.set_page_config(page_title="TravelMate", page_icon="🌍", layout="wide")

# Loading environment variables
def configure():
    dotenv_path = r'D:\UTS\Applied Natural Language Processing\Assignment_2\NLP_A2\py.env'
    load_dotenv(dotenv_path=dotenv_path)

configure()

# Loading API key
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    st.error("Please set the GOOGLE_API_KEY environment variable with your Gemini API key.")
    exit()

# Configuring the Gemini API
genai.configure(api_key=API_KEY)

# Initialize chat session if not already present
if 'chat_session' not in st.session_state:
    model = genai.GenerativeModel('gemini-1.5-pro')
    st.session_state.chat_session = model.start_chat()
    st.session_state.chat_history = []

# Handling the chat response with translation
def handle_chat(question, lang_code):
    try:
        # Translate question to English before sending to AI
        translated_question = GoogleTranslator(source=lang_code, target='en').translate(question)
        
        with st.spinner("Generating your trip plan..."):  # Display a loading spinner
            response = st.session_state.chat_session.send_message(translated_question)
        
        # Translate AI response back to user's selected language
        translated_response = GoogleTranslator(source='en', target=lang_code).translate(response.text)
        return translated_response
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return "An error occurred. Please try again."

# Sidebar for language selection
st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
st.sidebar.markdown("### 🌐 Language Selection")
language_options = {'English': 'en', 'French': 'fr', 'Spanish': 'es', 'German': 'de', 'Italian': 'it', 'Hindi': 'hi'}
selected_language = st.sidebar.selectbox("Select your language", list(language_options.keys()), index=0)
lang_code = language_options[selected_language]

# Main section for trip planning interface
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌍 TravelMate</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Your Virtual Travel Assistant</h3>", unsafe_allow_html=True)

# Input fields using columns for a cleaner layout
with st.container():
    st.markdown("### Plan Your Trip:")
    col1, col2 = st.columns(2)
    with col1:
        place_input = st.text_input("📍 Destination", placeholder="e.g., Paris")
        duration_input = st.text_input("🕒 Duration (days)", placeholder="e.g., 5")
        people_input = st.text_input("👥 Number of People", placeholder="e.g., 2")
    with col2:
        activity_input = st.text_input("🎯 Activities", placeholder="e.g., hiking, city tour, beach")
        accommodation_input = st.text_input("🏨 Accommodation Type", placeholder="e.g., hotel, hostel")
        budget_input = st.text_input("💵 Budget per Person (USD)", placeholder="e.g., 1000")

    # Plan Trip Button
    if st.button("Plan My Trip ✈️"):
        if all([place_input, duration_input, people_input, activity_input, accommodation_input, budget_input]):
            basic_info = f"Plan a trip to {place_input} for {duration_input} days for {people_input} with a budget of {budget_input} USD."
            detailed_info = f"Activities include: {activity_input}. Accommodation type: {accommodation_input}."
            final_question = f"{basic_info} {detailed_info} Include itinerary and expected expenses."
            
            response = handle_chat(final_question, lang_code)
            
            # Save chat history
            st.session_state.chat_history.append({"type": "Question", "content": final_question})
            st.session_state.chat_history.append({"type": "Response", "content": response})
            
            st.markdown("### 🗺️ Your Trip Plan:")
            st.write(response)
        else:
            st.warning("Please fill in all fields to get a trip plan.")

# Display previous chat history in a chat format
if st.session_state.chat_history:
    st.markdown("### 📜 Chat History:")
    for entry in st.session_state.chat_history:
        if entry['type'] == 'Question':
            st.markdown(f"<div style='background-color: #f9f9f9; padding: 10px; border-radius: 5px;'><strong>🟢 You:</strong> {entry['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='background-color: #e6f7ff; padding: 10px; border-radius: 5px;'><strong>🔵 TravelMate:</strong> {entry['content']}</div>", unsafe_allow_html=True)

# Follow-up question section
def follow_up_question():
    st.markdown("### 💬 Ask a Follow-up Question:")
    follow_up = st.text_input("Your Question:")
    if st.button("Submit Follow-up"):
        if follow_up:
            response = handle_chat(follow_up, lang_code)
            st.session_state.chat_history.append({"type": "Question", "content": follow_up})
            st.session_state.chat_history.append({"type": "Response", "content": response})
            
            st.markdown("### Response:")
            st.write(response)
        else:
            st.warning("Please enter a follow-up question.")

# Display follow-up section
follow_up_question()

# Adding image for background
image_path = "./Img/Travel_img.png"

st.image(image_path, use_column_width=True)
