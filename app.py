# Import the Streamlit library for creating web applications
import streamlit as st

# Import the pickle module for loading saved objects
import pickle

# Import the pandas library for data manipulation
import pandas as pd

# List of cricket team names
teams = ['Sunrisers Hyderabad',
         'Mumbai Indians',
         'Royal Challengers Bangalore', 'Kolkata Knight Riders',  'Kings XI Punjab', 'Chennai Super Kings', 'Rajasthan Royals', 'Delhi Capitals']

# List of cities where matches were played
cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
          'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
          'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
          'Sharjah', 'Mohali', 'Bengaluru']

# Load the saved pipeline using pickle
pipe = pickle.load(open('pipe.pkl', 'rb'))
# Set the title of the Streamlit web application
st.title('IPL Win Predictor')

# Split the page into two columns
col1, col2 = st.columns(2)
# Within the first column (col1)
with col1:
    # Create a selectbox for choosing the batting team
    batting_team = st.selectbox('Select the batting team', sorted(teams))
# Within the second column (col2)
with col2:
    # Create a selectbox for choosing the bowling team
    bowling_team = st.selectbox('Select the bowling team', sorted(teams))

    # Validate that batting_team and bowling_team are not the same
    if bowling_team == batting_team:
        st.warning("Please select different teams for batting and bowling.")
        st.stop()

# Create a selectbox for choosing the host city
selected_city = st.selectbox('Select host city', sorted(cities))
# Create a number input for entering the target
target = st.number_input('Target')
# Split the page into three columns
col3, col4, col5 = st.columns(3)
# Within the first column (col3)
with col3:
    # Create a number input for entering the score
    score = st.number_input('Score')
# Within the second column (col4)
with col4:
    # Create a number input for entering the overs completed
    overs = st.number_input('Overs completed')
# Within the third column (col5)
with col5:
    # Create a number input for entering the wickets out
    wickets = st.number_input('Wickets out')

# Create a button labeled 'Predict Probability'
if st.button('Predict Probability'):
    # Calculate derived values for prediction
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left

# Create an input DataFrame for prediction
    input_df = pd.DataFrame({'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [selected_city], 'runs_left': [runs_left], 'balls_left': [balls_left], 'wickets_left': [wickets], 'Target': [target], 'current_runrate': [crr], 'required_rr': [rrr]})
# Use the trained pipeline to predict probabilities
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    # Display predicted probabilities as headers
    st.header(batting_team + "- " + str(round(win*100)) + "%")
    st.header(bowling_team + "- " + str(round(loss*100)) + "%")
