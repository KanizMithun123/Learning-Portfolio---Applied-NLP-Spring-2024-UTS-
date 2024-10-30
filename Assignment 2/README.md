# TravelMate - Your Virtual Travel Assistant

TravelMate is a Streamlit-based web application designed to enhance your travel planning experience. By interacting with Google Gemini AI, TravelMate helps you generate personalized travel itineraries. Simply input your preferences for destination, duration, activities, accommodation type, and budget, and TravelMate will craft a tailored trip plan, including recommendations and estimated costs, all while supporting multiple languages for a global audience.

Link of our application: Travel Mate: https://travelmate.streamlit.app/

## Features
- **Select Preferred Language**: Choose your language preference from the dropdown menu. 
- **Interactive Trip Planning**: Input your travel details such as destination, duration, number of people, and preferences to get a customized travel plan.
- **Multi-Level Prompting**: The app engages you in a multi-level input process to refine the travel plans based on activities, accommodations, and budget.
- **Real-Time AI Interaction**: Uses Google's Generative AI to generate travel plans and itineraries dynamically.

## Setup Instructions

### Prerequisites
- Python 3.8+
- Streamlit
- An API key for Google's Generative AI services

### Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SuyashTapase/TravelMate_NLP_AT2_Group9.git
   cd TravelMate_NLP_AT2_Group9
   
2. **Install dependencies:**
   ```bash
   Copy code
   pip install -r requirements.txt
   Set up environment variables:

3. **Create a .env file in the root directory of the project and add the following line:**
   ```bash
   plaintext
   Copy code
   GOOGLE_API_KEY=your_api_key_here
   Replace your_api_key_here with your actual API key for Google's Generative AI.

4. **Run the application:**
   ```bash
   Copy code
   streamlit run app.py

## How to Use

1. Select the preffered language 
   - Chooes the language, English, French, Spanish, German, Italian or Hindi from the drop down menu. 

2. Input Basic Information:
   - Specify the destination, duration, and number of people traveling.
   - Specify Preferences:

3. Choose the types of activities you are interested in.
   - Select your preferred type of accommodation.
   - Define your budget per person in USD.
  
4. Generate Itinerary:
   - Click on 'Plan my trip' to generate a detailed itinerary including expected expenses.

"# TravelMate_NLP_AT2_Group9" 


### Submitted By: Group 9 

- Archit Pradip Murgudkar: 14190286
- Jyoti Khurana: 14075648
- Kaniz Fatema Mithun: 25109810
- Molly Dignan: 24929263
- Suyash Santosh Tapase: 24678207
