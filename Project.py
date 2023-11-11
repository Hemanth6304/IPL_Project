import csv 
from matplotlib import pyplot as plt

scores_by_team={}
year_to_runs={}
id_to_year={}
batsmen_runs={}
extra_runs_by_team={}
max_toss_wins={}
winners_by_team={}
matches_by_team={}
matches_by_season={}
umpire_to_country={}
umpire_list =set()
bowlers_ball_bowled={}
bowlers_runs_conceeded={}

#Foriegn Umpire Analysis
with open('umpires.csv', encoding='utf') as csv_file:
        umpire_reader = csv.DictReader(csv_file)
        for umpires in umpire_reader:
            if umpires["umpire"] != '':
                umpire_to_country[umpires["umpire"]] = umpires[" country"]

with open('matches.csv', encoding='utf-8') as file:
    match_reader = csv.DictReader(file)
    for matches in match_reader:
        id_to_year[matches["id"]] = int(matches["season"])
        umpire_list.add(matches["umpire1"])
        umpire_list.add(matches["umpire2"])

# Matches played by team by season
        if matches['team1'] not in matches_by_team:
            game_by_season={'2008':0,'2009': 0, '2010': 0, '2011': 0,
                                  '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0}
            game_by_season[matches['season']]+=1 
            matches_by_team[matches['team1']]= game_by_season
        else:
            if matches['season'] not in matches_by_team[matches['team1']]:
                matches_by_team[matches['team1']][matches['season']]=1
            else:
                matches_by_team[matches['team1']][matches['season']]+=1 
        if matches['team2'] not in matches_by_team:
            game_by_season={'2008':0,'2009': 0, '2010': 0, '2011': 0,
                                  '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0}
            game_by_season[matches['season']]+=1
            matches_by_team[matches['team2']]=game_by_season
        else:
            if matches['season'] not in matches_by_team[matches['team2']]:
                matches_by_team[matches['team2']][matches['season']]=1 
            else:
                matches_by_team[matches['team2']][matches['season']]+=1


# Matches played per year for all the years
        if int(matches['season']) not in matches_by_season:
            matches_by_season[int(matches['season'])]=1
        else:
            matches_by_season[int(matches['season'])]+=1
    
# Toss winners
        if matches['season']=='2017':
            if matches['toss_winner'] not in max_toss_wins:
                max_toss_wins[matches['toss_winner']]=1 
            else:
                max_toss_wins[matches['toss_winner']]+=1


# Matches won per team per year in ipl

        if matches['winner'] not in winners_by_team:
            game_by_season={'2008':0,'2009': 0, '2010': 0, '2011': 0,
                                  '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0}
            game_by_season[matches['season']]+=1 
            winners_by_team[matches['winner']]=game_by_season
        else:
            if matches['season'] not in winners_by_team[matches['winner']]:
                winners_by_team[matches['winner']][matches['season']]=1 
            else:
                winners_by_team[matches['winner']][matches['season']]+=1
    
#print(winners_by_team)
#print(max_toss_wins)
#print(matches_by_season)

with open('deliveries.csv', encoding='utf-8') as file:
    deliveries_reader=csv.DictReader(file)
    for matches in deliveries_reader:

        #TOTAL RUNS SCORED BY EACH TEAM IN IPL

        if matches["batting_team"] not in scores_by_team:
                year_to_runs = {id_to_year[matches["match_id"]]: int(
                    matches["total_runs"])}
                scores_by_team[matches["batting_team"]] = year_to_runs
        else:
            if id_to_year[matches["match_id"]] not in scores_by_team[matches["batting_team"]]:
                scores_by_team[matches["batting_team"]][id_to_year[matches["match_id"]]] = int(
                    matches["total_runs"])
            else:
                scores_by_team[matches["batting_team"]][id_to_year[matches["match_id"]]] += int(
                    matches["total_runs"])
                
        
        # Top batsmen for royal challengers banglore
        if matches['batting_team'] =='Royal Challengers Bangalore':
            if matches['batsman'] not in batsmen_runs:
                batsmen_runs[matches['batsman']]=int(matches['total_runs'])
            else:
                batsmen_runs[matches['batsman']]+=int(matches['total_runs'])


        # Extras conceeded by each team in 2016
        if id_to_year[matches['match_id']]==2016:
            if matches['bowling_team'] not in extra_runs_by_team:
                extra_runs_by_team[matches['bowling_team']]=int(matches['extra_runs'])
            else:
                extra_runs_by_team[matches['bowling_team']]+=int(matches['extra_runs'])
        
        # TOP 10 Economical bowlers in 2015
        if id_to_year[matches["match_id"]]==2015:
            if matches['bowler'] not in bowlers_ball_bowled:
                bowlers_ball_bowled[matches['bowler']]=1
            else:
                bowlers_ball_bowled[matches['bowler']]+=1 
            if matches['bowler'] not in bowlers_runs_conceeded:
                bowlers_runs_conceeded[matches['bowler']]=int(matches['total_runs'])
            else:
                bowlers_runs_conceeded[matches['bowler']]+=int(matches['total_runs'])

#print(bowlers_ball_bowled) 
#print(bowlers_runs_conceeded)       
#print(scores_by_team)
#print(id_to_year)
#print(year_to_runs)
#print(batsmen_runs)
#print(extra_runs_by_team)
#print(max_toss_wins)

def plot_top_run_getter():
    a=sorted(batsmen_runs.items(),key=lambda x:x[1]) 
    b=a[::-1]
    c=b[:10]
    d=dict(c)
    batsmen=d.keys()
    runs=d.values()
    plt.bar(batsmen,runs)
    plt.xlabel("Batsman")
    plt.ylabel('Runs')
    plt.title("TOP RUN GETTER FOR RCB")
    plt.show()
#plot_top_run_getter()



def plot_total_runs():
    """Plots total tuns scored by teams over the years in form of a line chart"""
    print(scores_by_team)
    for team in scores_by_team.items():
        x_axis = list(team[1].keys())
        y_axis = list(team[1].values())
        x_axis, y_axis = zip(*sorted(zip(x_axis, y_axis)))
        plt.plot(x_axis, y_axis, label=team[0])
    plt.xlabel("Years")
    plt.ylabel("Total Runs")
    plt.title("Total runs scored by Teams over the years")
    plt.legend()
    plt.show()
#plot_total_runs()



def plot_matches_played_per_season():
    season=matches_by_season.keys()
    total_played_matches=matches_by_season.values()
    plt.title("Total Matches Played Every Season")
    plt.bar(season,total_played_matches)
    plt.xlabel('Seasons')
    plt.ylabel('Matches Played')
    plt.show()
#plot_matches_played_per_season()
    


def plot_extra_runs():
    teams=extra_runs_by_team.keys()
    extras=extra_runs_by_team.values()
    plt.bar(teams,extras,width=0.4)
    plt.title(
        'Extras Given By Each Team'
    )
    plt.xlabel('Teams')
    plt.ylabel('Extras')
    plt.show()
#plot_extra_runs()


def plot_toss_winning_teams():
    teams=max_toss_wins.keys()
    toss_wins=max_toss_wins.values()
    plt.bar(teams,toss_wins,width=0.4)
    plt.title('Teams With Most Toss Wins in 2017')
    plt.xlabel('Teams')
    plt.ylabel('No.of Toss Wins')
    plt.show()
#plot_toss_winning_teams()


def winner_by_season():
    """This function plots the stacked bar of winners by team by every season"""
    baseline = [0]*10
    team_list = list(winners_by_team.keys())
    for team in winners_by_team.items():
        seasons = list(team[1].keys())
        match = list(team[1].values())
        seasons, match = zip(*sorted(zip(seasons, match)))
        plt.bar(seasons, match, bottom=baseline)
       
    print(winners_by_team)
    plt.title("Stacked bar plot of winners by season by team")
    plt.legend(team_list)
    plt.xlabel("Years")
    plt.ylabel("Matches")
    plt.show()
#winner_by_season()



def plot_economical_bowler():
    
    bowler_economy_rate={}

    for bowler in bowlers_ball_bowled.items():
        bowler_economy_rate[bowler[0]]=(
            bowlers_ball_bowled[bowler[0]]/bowlers_runs_conceeded[bowler[0]]*6
        )
    
    a=sorted(bowler_economy_rate.items(), key=lambda x:x[1])
    b=a[:10]
    c=dict(b)

    bowlers=c.keys()
    economy=c.values()
    plt.bar(bowlers,economy)
    plt.xlabel('Bowlers')
    plt.ylabel('Economy_Rate')
    plt.title("Top 10 Economical Bowlers")
    plt.show()
#plot_economical_bowler()


def add_two_lists(list1,list2):
    for i in enumerate(list1):
        list1[i[0]]+=list2[i[0]]
    return list1

def games_by_season():
    """This function prints a stacked bar chart of games every season"""
    team_list = list(matches_by_team.keys())
    # print(matches_by_team)
    baseline = [0]*10
    for team in matches_by_team.items():
        seasons = list(team[1].keys())
        match = list(team[1].values())
        seasons, match = zip(*sorted(zip(seasons, match)))
        plt.bar(seasons, match, bottom=baseline)
        baseline =add_two_lists(baseline, match)

    print(matches_by_team)
    plt.ylabel("Matches")
    plt.xlabel("Years")
    plt.legend(team_list)
    plt.title("Stacked bar chart of number of games played, by team , by season")
    plt.show()
#games_by_season()


def umpire_by_country():
    """Plots a bar graph showcasing the number of different
      nationalities fo umpires and their frequencies"""
    #print(umpire_list)
    country_count = {}
    for i in umpire_list:
        if i == '':
            continue
        if umpire_to_country[i] == '':
            continue
        if umpire_to_country[i] != " India":
            if umpire_to_country[i] not in country_count:
                country_count[umpire_to_country[i]] = 1
            else:
                country_count[umpire_to_country[i]] += 1
    print(country_count)
    x_axis = list(country_count.keys())
    y_axis = list(country_count.values())
    plt.bar(x_axis, y_axis, width=0.4)
    plt.xlabel("Countries")
    plt.ylabel("Number of umpires")
    plt.title("Umpires by country")
    plt.legend()
    plt.show()
#umpire_by_country()