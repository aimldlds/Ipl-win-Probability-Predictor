


# import streamlit as st
# import pickle
# import pandas as pd

# # Your Streamlit code without a separate function
# teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore', 'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings', 'Rajasthan Royals', 'Delhi Capitals']
# cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi', 'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala', 'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah', 'Mohali', 'Bengaluru']

# # ... (rest of your code)
# pipe = pickle.load(open('pipe.pkl','rb'))
# st.title('IPL Win Predictor')

# col1, col2 = st.columns(2)

# with col1:
#     batting_team = st.selectbox('Select the batting team',sorted(teams))
# with col2:
#     bowling_team = st.selectbox('Select the bowling team',sorted(teams))

# selected_city = st.selectbox('Select host city',sorted(cities))

# target = st.number_input('Target')

# col3,col4,col5 = st.columns(3)

# with col3:
#     score = st.number_input('Score')
# with col4:
#     overs = st.number_input('Overs completed')
# with col5:
#     wickets = st.number_input('Wickets out')

# if st.button('Predict Probability'):
#     runs_left = target - score
#     balls_left = 120 - (overs*6)
#     wickets = 10 - wickets
#     crr = score/overs
#     rrr = (runs_left*6)/balls_left

#     input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

#     result = pipe.predict_proba(input_df)
#     loss = result[0][0]
#     win = result[0][1]
#     st.header(batting_team + "- " + str(round(win*100)) + "%")
#     st.header(bowling_team + "- " + str(round(loss*100)) + "%")



# # ... (rest of your code)
# footer="""<style>
# a:link , a:visited{
# color: blue;
# background-color: transparent;
# text-decoration: underline;
# }

# a:hover,  a:active {
# color: red;
# background-color: transparent;
# text-decoration: underline;
# }

# .footer {
# position: fixed;
# left: 0;
# bottom: 0;
# width: 100%;
# background-color: white;
# color: black;
# text-align: center;
# }
# </style>
# <div class="footer">
# <p>Made with ❤ by <a style='display: block; text-align: center;' href="https://www.linkedin.com/in/mohsin37" target="_blank">Mohammad Mohsin</a></p>
# </div>
# """
# st.markdown(footer,unsafe_allow_html=True)


# # Wrap Streamlit app in a function
# def run():
#     teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore', 'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings', 'Rajasthan Royals', 'Delhi Capitals']
#     cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi', 'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala', 'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah', 'Mohali', 'Bengaluru']

#     # ... (rest of your code)
#     pipe = pickle.load(open('pipe.pkl','rb'))
#     st.title('IPL Win Predictor')
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         batting_team = st.selectbox('Select the batting team',sorted(teams))
#     with col2:
#         bowling_team = st.selectbox('Select the bowling team',sorted(teams))
    
#     selected_city = st.selectbox('Select host city',sorted(cities))
    
#     target = st.number_input('Target')
    
#     col3,col4,col5 = st.columns(3)
    
#     with col3:
#         score = st.number_input('Score')
#     with col4:
#         overs = st.number_input('Overs completed')
#     with col5:
#         wickets = st.number_input('Wickets out')
    
#     if st.button('Predict Probability'):
#         runs_left = target - score
#         balls_left = 120 - (overs*6)
#         wickets = 10 - wickets
#         crr = score/overs
#         rrr = (runs_left*6)/balls_left
    
#         input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})
    
#         result = pipe.predict_proba(input_df)
#         loss = result[0][0]
#         win = result[0][1]
#         st.header(batting_team + "- " + str(round(win*100)) + "%")
#         st.header(bowling_team + "- " + str(round(loss*100)) + "%")
    
    
    

#     footer = """<style>
#     a:link , a:visited{
#     color: blue;
#     background-color: transparent;
#     text-decoration: underline;
#     }

#     a:hover,  a:active {
#     color: red;
#     background-color: transparent;
#     text-decoration: underline;
#     }

#     .footer {
#     position: fixed;
#     left: 0;
#     bottom: 0;
#     width: 100%;
#     background-color: white;
#     color: black;
#     text-align: center;
#     }
#     </style>
#     <div class="footer">
#     <p>Made with ❤ by <a style='display: block; text-align: center;' href="https://www.linkedin.com/in/mohsin37" target="_blank">Mohammad Mohsin</a></p>
#     </div>
#     """
#     st.markdown(footer, unsafe_allow_html=True)

# # Define 'app' as the Streamlit app callable for Gunicorn
# app = run


import streamlit as st
import pickle
import pandas as pd

def run(a,b):
    teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore', 'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings', 'Rajasthan Royals', 'Delhi Capitals']
    cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi', 'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala', 'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah', 'Mohali', 'Bengaluru']

    pipe = pickle.load(open('pipe.pkl','rb'))
    st.title('IPL Win Predictor')

    col1, col2 = st.columns(2)

    with col1:
        batting_team = st.selectbox('Select the batting team',sorted(teams))
    with col2:
        bowling_team = st.selectbox('Select the bowling team',sorted(teams))

    selected_city = st.selectbox('Select host city',sorted(cities))

    target = st.number_input('Target')

    col3, col4, col5 = st.columns(3)

    with col3:
        score = st.number_input('Score')
    with col4:
        overs = st.number_input('Overs completed')
    with col5:
        wickets = st.number_input('Wickets out')

    if st.button('Predict Probability'):
        runs_left = target - score
        balls_left = 120 - (overs*6)
        wickets = 10 - wickets
        crr = score/overs
        rrr = (runs_left*6)/balls_left

        input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

        result = pipe.predict_proba(input_df)
        loss = result[0][0]
        win = result[0][1]
        st.header(batting_team + "- " + str(round(win*100)) + "%")
        st.header(bowling_team + "- " + str(round(loss*100)) + "%")

    footer="""<style>
    a:link , a:visited{
    color: blue;
    background-color: transparent;
    text-decoration: underline;
    }
    
    a:hover,  a:active {
    color: red;
    background-color: transparent;
    text-decoration: underline;
    }
    
    .footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: white;
    color: black;
    text-align: center;
    }
    </style>
    <div class="footer">
    <p>Made with ❤ by <a style='display: block; text-align: center;' href="https://www.linkedin.com/in/mohsin37" target="_blank">Mohammad Mohsin</a></p>
    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)

# 'app' as the Streamlit app callable for Gunicorn
app = run











