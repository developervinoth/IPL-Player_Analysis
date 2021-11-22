import pandas as pd
import streamlit as st
import numpy as np
# Match.csv file into DataFrame
team_details = pd.read_csv('Flat_files/Match.csv')

teamNames = team_details['Team1'].drop_duplicates()
teamOneChoice = st.sidebar.selectbox('Team 1',teamNames)
teamTwoChoice = st.sidebar.selectbox('Team 2',teamNames)

st.title('Team vs Team')

teamVsTeam = team_details[(((team_details['Team1'] == teamOneChoice) | 
(team_details['Team1'] == teamTwoChoice)) & ((team_details['Team2'] == teamTwoChoice) | (team_details['Team2'] == teamOneChoice)))]
teamVsTeam['S.No'] = np.arange(len(teamVsTeam))

totalMatches = teamVsTeam['Team1'].count()
st.text(totalMatches)

st.table(teamVsTeam[['S.No','match_date','Toss_Winner','match_winner','Toss_Name','ManOfMach','Venue_Name']])
