import os
import psycopg2

conn = psycopg2.connect(
        host="drhscit.org",
        database=os.environ['DB'],
        user=os.environ['DB_UN'],
        password=os.environ['DB_PW'])

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS scouting_report;')
cur.execute('DROP TABLE IF EXISTS game_report;')

cur.execute('CREATE TABLE scouting_report (id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,'
                                 'team TEXT NOT NULL,'
                                 'playstyle TEXT,'
                                 'corners TEXT,'
                                 'players_to_watch TEXT,'
                                 'goalkeeper TEXT,'                                 
                                 'team_notes TEXT,'
                                 'roster TEXT,'
                                 'date_added DATE DEFAULT CURRENT_DATE);'
                                 )
cur.execute('CREATE TABLE game_report (id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,'
                                 'team_game TEXT NOT NULL,'
                                 'level TEXT NOT NULL,'
                                 'home_goals Integer,'
                                 'opponent_goals Integer,'
                                 'goal_scorer text,'
                                 'assister text,'
                                 'goal_description TEXT,'
                                 'goalie_saves Integer,'
                                 'home_corner_kicks Integer,'
                                 'opponent_corner_kicks Integer,'
                                 'fouls Integer,'
                                 'home_goal_kicks Integer,'
                                 'opponent_goal_kicks Integer,'
                                 'lineup TEXT,'
                                 'field_conditions TEXT,'
                                 'weather_conditions TEXT,'                                 
                                 'date_added DATE DEFAULT CURRENT_DATE,'
                                'shots_on_goal Integer,'
                                'player_shots TEXT,'
                                'direct_kicks integer,'
                                'indirect_kicks integer,'
                                 'notes TEXT);'
                                 )
conn.commit()

cur.close()
conn.close()