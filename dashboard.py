import pandas as pd
import streamlit as st
import numpy as np
# Match.csv file into DataFrame
team_details = pd.read_csv('Flat_files/Match.csv')
player_details = pd.read_csv('Flat_files/Player.csv')
player_matches = pd.read_csv('Flat_files/Player_match.csv')

st.set_page_config(  # Alternate names: setup_page, page, layout
	layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
	initial_sidebar_state="collapsed",  # Can be "auto", "expanded", "collapsed"
	page_title=None,  # String or None. Strings get appended with "• Streamlit". 
	page_icon=None,  # String, anything supported by st.image, or None.
)


page_select = st.selectbox('Choose Page', ['Team vs Team', 'Player Comparision', 'Season Comparision'],)

col1, col2, col3 = st.columns(3)

cl1,cl2 = st.columns(2)

if page_select == 'Team vs Team':

    teamNames = team_details['Team1'].drop_duplicates()
    teamOneChoice = st.sidebar.selectbox('Team 1',teamNames)
    teamTwoChoice = st.sidebar.selectbox('Team 2',teamNames)


    teamVsTeam = team_details[(((team_details['Team1'] == teamOneChoice) | 
    (team_details['Team1'] == teamTwoChoice)) & ((team_details['Team2'] == teamTwoChoice) | (team_details['Team2'] == teamOneChoice)))]
    teamVsTeam['S.No'] = np.arange(len(teamVsTeam))



    totalMatches = teamVsTeam['Team1'].count()
    team1Wins = teamVsTeam[(teamVsTeam['match_winner'] == teamOneChoice)]['match_winner'].count()
    team2Wins = teamVsTeam[(teamVsTeam['match_winner'] == teamTwoChoice)]['match_winner'].count()

    col1.text('Number of Matches')
    col1.title(totalMatches)
    col2.text(teamOneChoice)
    col2.title(team1Wins)
    col3.text(teamTwoChoice)
    col3.title(team2Wins)
    st.table(teamVsTeam[['S.No','match_date','Toss_Winner','match_winner','Toss_Name','ManOfMach','Venue_Name']])

if page_select == 'Player Comparision':
    playerNames = player_details['Player_Name'].drop_duplicates()
    playerOne = cl1.selectbox('Select Player Two',playerNames)
    playerTwo = cl2.selectbox('Select Player One',playerNames)

#Player One Data
    cl1.text('Country')
    cl1.title(player_details[player_details['Player_Name'] == playerOne]['Country_Name'].values[0])
    cl1.text('Batting Style')
    cl1.title(player_details[player_details['Player_Name'] == playerOne]['Batting_hand'].values[0])
    cl1.text('Total Matches')
    cl1.title(player_matches[(player_matches['Player_Name'] == playerOne)]['Player_Name'].count())
#Player Two Data
    cl2.text('Country')
    cl2.title(player_details[player_details['Player_Name'] == playerTwo]['Country_Name'].values[0])
    cl2.text(' Batting Style')
