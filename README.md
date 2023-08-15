# CAPSTON-PROJECT
# About Dataset
# Context
IPL is one of the most-attended cricket league. We have collected data of almost every match from 2008 to 2022. The collected data is well processed and cleaned using Python tool. With the help of this dataset we can analyze the status of each team whether it is going to win or lose. We can apply various machine learning and deep learning algorithms to predict the probability of win. We have chosen very real features which are used for predicting the probability of win based on current score, balls left, current run rate, wickets left etc.

# Content
This dataset consists of two seperate CSV files: match.csv and delivery.csv . These files contain the information of each match summary and ball-by-ball details, respectively.

# The dataset contains the following columns:
# Columns which we require in match.csv
1. venue :- Specifies the name of the venue where the match was held.
2. method :- It will show if match result came with duckworth lewis method
3. winner :- Specifies the winning team of the match.
4. city :- Specifies the name of the city where the match was held.
5. team1 :- First team.
6 .team2 :- Second team.
7. matchId : - This represents a unique identifier for each match, enabling easy referencing and tracking.
   
# Columns which we require in delivery.csv
1. matchId :- This represents a unique identifier for each match, enabling easy referencing and tracking.
2. over_ball :- It shows howmany overs and balls are played.
3. batting_team :-(current) team for batting in 2nd inning.
4. bowling_team :-(previous) team for bowling in 2nd inning.
5. batsman_runs :- It show runs scored by batsman.
6. extras :- It show extra runs.
7. total_runs :- It show total runs after every ball.
8. isWide :- It show if the ball is wide if it is then it show runs of that ball.
9. isNoBall :- It show if the ball is Noball if it is then it show runs of that ball.
10. Byes :- Shows the runs for Byes.
11. LegByes :- shows the runs of legbyes.
12. dismissal_kind :- It show how the player is out.
13. player_dismissed :- It show if the player dismissed or not after every ball
   
# From the data i also created some new columns
1. runs_left :- It show how many runs left to score after every ball.
2. balls_left :- It show how many balls left after every ball.
3. wickets_left :- It show how many wickets left.
4. Target :- It show the target score for batting team in second inning.
5. current_runrate :- It show what is the current runrate after every ball.
6. required_rr :- It show what is the required runrate after every ball.
7. result :- It show 1 if team 2 (currently batting team) won otherwise 0.

# Conclusion :
This project predict the outcome of an Indian Premier League (IPL) cricket match. Users can select the batting and bowling teams, the host city, and input match details such as the target score, current score, overs completed, and wickets fallen. The application trained machine learning model to calculate and display the predicted probabilities of each team winning the match.
