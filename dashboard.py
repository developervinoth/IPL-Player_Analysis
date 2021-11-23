#Importing Packages
import pandas as pd
import streamlit as st
import numpy as np
from datetime import date

# Reading CSV Files From Directory
team_details = pd.read_csv('Flat_files/Match.csv')
player_details = pd.read_csv('Flat_files/Player.csv')
player_matches = pd.read_csv('Flat_files/Player_match.csv')
ballByBall = pd.read_csv('Ball_By_Ball.csv')

#Page Configuration
st.set_page_config(  # Alternate names: setup_page, page, layout
	layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
	initial_sidebar_state="collapsed",  # Can be "auto", "expanded", "collapsed"
	page_title=None,  # String or None. Strings get appended with "• Streamlit". 
	page_icon=None,  # String, anything supported by st.image, or None.
)

page_select = st.selectbox('Choose Page', ['Team vs Team', 'Player vs Player'],)

col1, col2, col3 = st.columns(3)

cl1,cl2 = st.columns(2)

#Function to Calculate Batting Strike Rate
def battingStrikeRate(runs_scored, balls_faced):
     return round(((runs_scored / balls_faced) * 100),2)

#Function to Calculate Bowling Strike Rate
def bowlingStrikeRate(ballsBowled, wicketsTaken):
    return round((ballsBowled/wicketsTaken),2)



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
    col1.subheader(totalMatches)
    col2.text(teamOneChoice)
    col2.subheader(team1Wins)
    col3.text(teamTwoChoice)
    col3.subheader(team2Wins)
    st.table(teamVsTeam[['S.No','match_date','Toss_Winner','match_winner','Toss_Name','ManOfMach','Venue_Name']])

if page_select == 'Player vs Player':
    playerNames = player_details['Player_Name'].drop_duplicates()
    playerOne = cl1.selectbox('Select Player One',playerNames)
    playerTwo = cl2.selectbox('Select Player Two',playerNames)

#Player One Data
    cl1.text('Country')
    cl1.subheader(player_details[player_details['Player_Name'] == playerOne]['Country_Name'].values[0])

    cl1.text('Batting Style')
    cl1.subheader(player_details[player_details['Player_Name'] == playerOne]['Batting_hand'].values[0])
    
    cl1.text('Bowling Style')
    cl1.subheader(player_details[player_details['Player_Name'] == playerOne]['Bowling_skill'].values[0])
    
    cl1.text('Total Matches')
    cl1.subheader(player_matches[(player_matches['Player_Name'] == playerOne)]['Player_Name'].count())
    
    ballByBall_Runs = pd.merge(player_details,ballByBall,left_on='Player_Id', right_on='Striker')
    ballByBall_Wickets = pd.merge(player_details,ballByBall,left_on='Player_Id', right_on='Bowler')
    
    cl1.text('Runs Scored')
    
    runs_scored_one = ballByBall_Runs[ballByBall_Runs['Player_Name'] == playerOne]['Runs_Scored'].sum()
    balls_faced_one = ballByBall_Runs[ballByBall_Runs['Player_Name'] == playerOne]['Ball_id'].count()
    wicket_taken_one = ballByBall_Wickets[ballByBall_Wickets['Player_Name'] == playerOne]['Bowler_Wicket'].sum()
    balls_bowled_one = ballByBall_Wickets[ballByBall_Wickets['Player_Name'] == playerOne]['Ball_id'].count()
    
    cl1.subheader(runs_scored_one)
    
    cl1.text('Wickets Taken')
    cl1.subheader(wicket_taken_one)
    
    cl1.text('Batting Strike Rate')
    cl1.subheader(battingStrikeRate(runs_scored_one,balls_faced_one))
    
    cl1.text('Bowling Strike Rate')
    cl1.subheader(bowlingStrikeRate(balls_bowled_one, wicket_taken_one))

    cl1.text('Man Of Match')
    cl1.subheader(team_details[team_details['ManOfMach'] == playerOne]['ManOfMach'].count())


#Player Two Data
    cl2.text('Country')
    cl2.subheader(player_details[player_details['Player_Name'] == playerTwo]['Country_Name'].values[0])

    cl2.text('Batting Style')
    cl2.subheader(player_details[player_details['Player_Name'] == playerTwo]['Batting_hand'].values[0])

    cl2.text('Bowling Style')
    cl2.subheader(player_details[player_details['Player_Name'] == playerTwo]['Bowling_skill'].values[0])
    

    cl2.text('Total Matches')
    cl2.subheader(player_matches[(player_matches['Player_Name'] == playerTwo)]['Player_Name'].count())
    runs_scored_two = ballByBall_Runs[ballByBall_Runs['Player_Name'] == playerTwo]['Runs_Scored'].sum()
    balls_faced_two = ballByBall_Runs[ballByBall_Runs['Player_Name'] == playerTwo]['Ball_id'].count()
    wicket_taken_two = ballByBall_Wickets[ballByBall_Wickets['Player_Name'] == playerTwo]['Bowler_Wicket'].sum()
    balls_bowled_two = ballByBall_Wickets[ballByBall_Wickets['Player_Name'] == playerTwo]['Ball_id'].count()
    
    cl2.text('Total Runs Scored')
    cl2.subheader(runs_scored_two)

    cl2.text('Wickets Taken')
    cl2.subheader(ballByBall_Wickets[ballByBall_Wickets['Player_Name'] == playerTwo]['Bowler_Wicket'].sum())

    cl2.text('Batting Strike Rate')
    cl2.subheader(battingStrikeRate(runs_scored_two,balls_faced_two))

    cl2.text('Bowling Strike Rate')
    cl2.subheader(bowlingStrikeRate(balls_bowled_two, wicket_taken_two))

    cl2.text('Man Of Match')
    cl2.subheader(team_details[team_details['ManOfMach'] == playerTwo]['ManOfMach'].count())
